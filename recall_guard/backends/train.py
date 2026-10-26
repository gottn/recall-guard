"""LoRA repair training: the only module that runs backward passes. Loss only on answer tokens (labels = -100
elsewhere). The adapter is the dependency-free one in `lora.py`; `hf.load` merges it back for evaluation."""

import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer

from recall_guard.backends import hf, lora
from recall_guard.filler import filler_sentences
from recall_guard.real_data import Pool, disjoint, eval_strings, hotpot_pool, real_segments, squad_pool
from recall_guard.train_data import Segment, training_segments

LOSS_CHUNK = 1024  # labelled positions per logits chunk: a replay window labels every token (16K x 128K logits = 8 GiB at once)


@dataclass(frozen=True)
class TrainConfig:
    model_id: str
    out_dir: str
    n_docs: int
    lengths: tuple[int, ...]
    seed: int
    lr: float
    rank: int
    alpha: int
    grad_accum: int
    max_steps: int
    trust_remote_code: bool
    targets: str = ""  # regex on leaf names; empty = every linear outside the MLPs
    weight_decay: float = 0.0  # on the adapter only: decays A/B toward zero, i.e. toward the base model
    replay_text: str = ""  # path to natural long text; when set, every other example is a window of it with full LM loss
    replay_frac: float = 0.5
    real_dir: str = ""  # SQuAD v2 train + HotpotQA train JSON; when set, every other example is a real-document QA (real_data.py)
    exclude_dir: str = ""  # evaluation case JSONL: its paragraphs and questions never enter the real pools


def tokenize_segments(tok: AutoTokenizer, segs: tuple[Segment, ...]) -> tuple[torch.Tensor, torch.Tensor]:
    ids: list[int] = []
    labels: list[int] = []
    for s in segs:
        t = tok(s.text, add_special_tokens=False).input_ids
        ids += t
        labels += t if s.train else [-100] * len(t)
    return torch.tensor([ids]), torch.tensor([labels])


def checkpoint_custom_layers(model: torch.nn.Module) -> int:
    """transformers >= 5 checkpoints only layers that subclass GradientCheckpointingLayer; layers swapped in by a loader
    (Mamba-2 blocks in Mamba-in-the-Llama) are plain modules and would keep full activations. Wrap their forward."""
    import torch.utils.checkpoint as cp
    from transformers.modeling_layers import GradientCheckpointingLayer

    wrapped = 0
    for layer in getattr(getattr(model, "model", None), "layers", ()):
        if isinstance(layer, GradientCheckpointingLayer):
            continue
        fwd = layer.forward

        def wrapped_forward(*args, _fwd=fwd, **kwargs):
            return cp.checkpoint(_fwd, *args, use_reentrant=False, **kwargs)

        layer.forward = wrapped_forward
        wrapped += 1
    return wrapped


def replay_example(text: str, tok: AutoTokenizer, window_tokens: int, seed: int) -> tuple[torch.Tensor, torch.Tensor]:
    """A random window of natural text with labels on every token (ordinary LM loss), the anti-forgetting replay."""
    import random

    rng = random.Random(seed)
    start = rng.randrange(0, max(1, len(text) - window_tokens * 6))
    ids = tok(text[start : start + window_tokens * 6], add_special_tokens=False, return_tensors="pt").input_ids[:, :window_tokens]
    return ids, ids.clone()


def load_real_pools(real_dir: str, exclude_dir: str) -> tuple[Pool, ...]:
    """The two train-split pools minus every paragraph and question of the evaluation cases, with the counts logged."""
    prompts = [json.loads(line)["prompt"] for f in sorted(Path(exclude_dir).glob("*.jsonl")) for line in f.read_text().splitlines() if line]
    banned = eval_strings(prompts)
    raw = (squad_pool(json.loads((Path(real_dir) / "train-v2.0.json").read_text())),
           hotpot_pool(json.loads((Path(real_dir) / "hotpot_train_v1.1.json").read_text())))
    out = tuple(disjoint(p, banned) for p in raw)
    for a, b in zip(raw, out, strict=True):
        print(f"  real pool {a.name}: {len(b.paragraphs):,} of {len(a.paragraphs):,} paragraphs and {sum(len(g.qas) for g in b.groups):,} of "
              f"{sum(len(g.qas) for g in a.groups):,} questions remain after banning {len(banned):,} strings from {len(prompts)} evaluation prompts", file=sys.stderr)
    return out


def answer_loss(model: torch.nn.Module, ids: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    """Cross-entropy on answer positions only, applying lm_head just there: full-sequence logits at 16K x 152K
    vocab in float32 are 9.3 GiB, which is what OOMed the first smoke."""
    hidden = model.model(input_ids=ids).last_hidden_state[0]
    pos = (labels[0, 1:] != -100).nonzero().squeeze(-1)
    targets = labels[0, 1:][pos]
    if len(pos) <= LOSS_CHUNK:
        return F.cross_entropy(model.lm_head(hidden[pos]).float(), targets)
    import torch.utils.checkpoint as cp

    def chunk_sum(h: torch.Tensor, y: torch.Tensor) -> torch.Tensor:  # recomputed in backward: one chunk of logits alive at a time
        return F.cross_entropy(model.lm_head(h).float(), y, reduction="sum")

    total = sum(
        cp.checkpoint(chunk_sum, hidden[pos[i : i + LOSS_CHUNK]], targets[i : i + LOSS_CHUNK], use_reentrant=False)
        for i in range(0, len(pos), LOSS_CHUNK)
    )
    return total / len(pos)


def train(cfg: TrainConfig) -> dict:
    torch.manual_seed(cfg.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tok, model = hf.load(cfg.model_id, "sdpa", cfg.trust_remote_code)  # same registry path as evaluation
    targets = lora.target_names(model)
    if cfg.targets:
        targets = tuple(n for n in targets if re.search(cfg.targets, n))
    wrapped = lora.inject(model, targets, cfg.rank, cfg.alpha)
    params = lora.trainable(model)
    n_train, n_all = sum(p.numel() for p in params), sum(p.numel() for p in model.parameters())
    print(f"  lora targets: {targets}; wrapped {len(wrapped)} layers; trainable {n_train:,} / {n_all:,} ({100 * n_train / n_all:.2f}%)", file=sys.stderr)
    if device == "cuda":
        model.gradient_checkpointing_enable()
        model.enable_input_require_grads()
        print(f"  checkpointed {checkpoint_custom_layers(model)} non-transformers layers", file=sys.stderr)
    opt = torch.optim.AdamW(params, lr=cfg.lr, weight_decay=cfg.weight_decay)
    replay = Path(cfg.replay_text).read_text() if cfg.replay_text else ""
    if cfg.real_dir and not cfg.exclude_dir:
        raise ValueError("--real-dir needs --exclude-dir (the evaluation cases to keep out of training)")
    pools = load_real_pools(cfg.real_dir, cfg.exclude_dir) if cfg.real_dir else ()
    def count(text: str) -> int:
        return len(tok(text, add_special_tokens=False).input_ids)

    tps = count(" ".join(filler_sentences(256, 0))) / 256
    model.train()
    t0, tokens, losses, step = time.perf_counter(), 0, [], 0
    n = min(cfg.n_docs, cfg.max_steps * cfg.grad_accum) if cfg.max_steps else cfg.n_docs
    for i in range(n):
        j = i // 2 if pools else i  # real and synthetic alternate, each stream keeping its own count: kinds, lengths and pools cycle as before
        length = cfg.lengths[j % len(cfg.lengths)]
        period = round(1 / cfg.replay_frac) if cfg.replay_frac > 0 else 0  # 0.5 -> every 2nd example, 0.25 -> every 4th
        if replay and period and i % period == period - 1:
            ids, labels = replay_example(replay, tok, length, cfg.seed * 100_000 + i)
        elif pools and i % 2:
            ids, labels = tokenize_segments(tok, real_segments(pools[j // 2 % len(pools)], cfg.seed * 100_000 + j, length, count))
        else:
            ids, labels = tokenize_segments(tok, training_segments(cfg.seed * 100_000 + j, length, count, tps))
        loss = answer_loss(model, ids.to(device), labels.to(device))
        (loss / cfg.grad_accum).backward()
        losses.append(loss.item())
        tokens += ids.shape[1]
        if (i + 1) % cfg.grad_accum == 0:
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            opt.zero_grad(set_to_none=True)
            step += 1
            if step % 5 == 0 or step == 1:
                recent = sum(losses[-cfg.grad_accum * 5 :]) / len(losses[-cfg.grad_accum * 5 :])
                mem = torch.cuda.max_memory_allocated() / 2**30 if device == "cuda" else 0.0
                print(f"  step {step} doc {i + 1}/{n} loss {recent:.3f} tok/s {tokens / (time.perf_counter() - t0):.0f} maxmem {mem:.1f}G", file=sys.stderr)
    lora.save(model, cfg.out_dir, cfg.rank, cfg.alpha)
    return {"docs": n, "steps": step, "tokens": tokens, "wall_s": time.perf_counter() - t0, "final_loss": sum(losses[-8:]) / max(1, len(losses[-8:])), "targets": targets}

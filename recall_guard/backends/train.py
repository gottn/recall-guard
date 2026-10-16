"""LoRA repair training: the only module that runs backward passes. Loss only on answer tokens (labels = -100
elsewhere). Adapter saved with PEFT; `hf.load` merges it back for evaluation."""

import sys
import time
from dataclasses import dataclass

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer

from recall_guard.backends import hf, lora
from recall_guard.filler import filler_sentences
from recall_guard.train_data import Segment, training_segments


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


def tokenize_segments(tok: AutoTokenizer, segs: tuple[Segment, ...]) -> tuple[torch.Tensor, torch.Tensor]:
    ids: list[int] = []
    labels: list[int] = []
    for s in segs:
        t = tok(s.text, add_special_tokens=False).input_ids
        ids += t
        labels += t if s.train else [-100] * len(t)
    return torch.tensor([ids]), torch.tensor([labels])


def answer_loss(model: torch.nn.Module, ids: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    """Cross-entropy on answer positions only, applying lm_head just there: full-sequence logits at 16K x 152K
    vocab in float32 are 9.3 GiB, which is what OOMed the first smoke."""
    hidden = model.model(input_ids=ids).last_hidden_state[0]
    pos = (labels[0, 1:] != -100).nonzero().squeeze(-1)
    logits = model.lm_head(hidden[pos]).float()
    return F.cross_entropy(logits, labels[0, 1:][pos])


def train(cfg: TrainConfig) -> dict:
    torch.manual_seed(cfg.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tok, model = hf.load(cfg.model_id, "sdpa", cfg.trust_remote_code)  # same registry path as evaluation
    targets = lora.target_names(model)
    wrapped = lora.inject(model, targets, cfg.rank, cfg.alpha)
    params = lora.trainable(model)
    n_train, n_all = sum(p.numel() for p in params), sum(p.numel() for p in model.parameters())
    print(f"  lora targets: {targets}; wrapped {len(wrapped)} layers; trainable {n_train:,} / {n_all:,} ({100 * n_train / n_all:.2f}%)", file=sys.stderr)
    if device == "cuda":
        model.gradient_checkpointing_enable()
        model.enable_input_require_grads()
    opt = torch.optim.AdamW(params, lr=cfg.lr, weight_decay=0.0)
    def count(text: str) -> int:
        return len(tok(text, add_special_tokens=False).input_ids)

    tps = count(" ".join(filler_sentences(256, 0))) / 256
    model.train()
    t0, tokens, losses, step = time.perf_counter(), 0, [], 0
    n = min(cfg.n_docs, cfg.max_steps * cfg.grad_accum) if cfg.max_steps else cfg.n_docs
    for i in range(n):
        segs = training_segments(cfg.seed * 100_000 + i, cfg.lengths[i % len(cfg.lengths)], count, tps)
        ids, labels = tokenize_segments(tok, segs)
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

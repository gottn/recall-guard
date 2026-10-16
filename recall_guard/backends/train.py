"""LoRA repair training: the only module that runs backward passes. Loss only on answer tokens (labels = -100
elsewhere). Adapter saved with PEFT; `hf.load` merges it back for evaluation."""

import sys
import time
from dataclasses import dataclass

import torch
import torch.nn.functional as F
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

from recall_guard.backends.hf import DTYPE_KWARG
from recall_guard.filler import filler_sentences
from recall_guard.train_data import Segment, training_segments

SKIP_IN_NAME = ("mlp", "lm_head", "embed")


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


def lora_targets(model: torch.nn.Module) -> tuple[str, ...]:
    """Every nn.Linear outside the MLPs, head and embeddings: attention and linear-attention projections."""
    names = {
        name.rsplit(".", 1)[-1]
        for name, m in model.named_modules()
        if isinstance(m, torch.nn.Linear) and not any(s in name for s in SKIP_IN_NAME)
    }
    return tuple(sorted(names))


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
    base = model.get_base_model() if hasattr(model, "get_base_model") else model
    hidden = base.model(input_ids=ids).last_hidden_state[0]
    pos = (labels[0, 1:] != -100).nonzero().squeeze(-1)
    logits = base.lm_head(hidden[pos]).float()
    return F.cross_entropy(logits, labels[0, 1:][pos])


def train(cfg: TrainConfig) -> dict:
    torch.manual_seed(cfg.seed)
    tok = AutoTokenizer.from_pretrained(cfg.model_id, trust_remote_code=cfg.trust_remote_code)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = {DTYPE_KWARG: torch.bfloat16 if device == "cuda" else torch.float32}
    model = AutoModelForCausalLM.from_pretrained(cfg.model_id, trust_remote_code=cfg.trust_remote_code, device_map=device, **dtype)
    targets = lora_targets(model)
    print(f"  lora targets: {targets}", file=sys.stderr)
    model = get_peft_model(model, LoraConfig(r=cfg.rank, lora_alpha=cfg.alpha, target_modules=list(targets), lora_dropout=0.0, bias="none"))
    if device == "cuda":
        model.gradient_checkpointing_enable()
        model.enable_input_require_grads()
    model.print_trainable_parameters()
    opt = torch.optim.AdamW((p for p in model.parameters() if p.requires_grad), lr=cfg.lr, weight_decay=0.0)
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
    model.save_pretrained(cfg.out_dir)
    return {"docs": n, "steps": step, "tokens": tokens, "wall_s": time.perf_counter() - t0, "final_loss": sum(losses[-8:]) / max(1, len(losses[-8:])), "targets": targets}

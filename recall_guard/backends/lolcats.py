"""LoLCATs linearized Llama-3.1-8B (Zhang et al. 2024, github.com/HazyResearch/lolcats, branch lolcats-scaled): every
softmax attention becomes 64-token window softmax + Hedgehog linear attention; q/k/v/o then LoRA-tuned.

Weights: meta-llama/Llama-3.1-8B + feature maps and window factors (hazyresearch/lolcats-llama-3.1-8b-distill) + the
LoRA of the -ft-lora repo (r=8, alpha=16) merged into the projections in fp32 (no peft).
Attention re-implemented from their lolcats_llama_window_tk attention and LinearAttentionTKWindowCache, whose prefill
materialises the full fp32 score matrix (128 GB at 32K) and needs transformers 4.4x + flash_attn. Same function:
- prefill: query t takes softmax over its own and the previous 64-token block (blocks end at the last prompt token, as
  their cropped "terrace" mask does) and linear attention over all older keys; one shared normaliser; softmax terms are
  sigmoid(window_factor) * exp(s - row max), linear terms f(q).f(k).
- decode: softmax over the last 64 keys (current included), linear over everything older, state kept in the model dtype.
f(x) = clamp(cat(softmax(xW), softmax(-xW)), 1e-12) per head with W: (head_dim, 64), on rotated, kv-repeated q and k."""

import torch
import torch.nn.functional as F
from torch import Tensor

WINDOW = 64


def feature_map(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    """(b, h, n, d) x (h, d, f) -> (b, h, n, 2f), computed in the input dtype as theirs is."""
    y = torch.einsum("hdf,bhnd->bhnf", w, x)
    return torch.cat([torch.softmax(y, -1), torch.softmax(-y, -1)], -1).clamp(min=1e-12)


def with_previous_block(t: torch.Tensor) -> torch.Tensor:
    """(b, h, blocks, w, x) -> (b, h, blocks, 2w, x): each block preceded by the one before it (zeros for block 0)."""
    return torch.cat([F.pad(t, (0, 0, 0, 0, 1, 0))[:, :, :-1], t], 3)


def prefill(q: Tensor, k: Tensor, v: Tensor, fq: Tensor, fk: Tensor, wf: Tensor, window: int = WINDOW) -> Tensor:
    """Terrace window softmax + linear attention over a whole prompt in O(n * window) memory; (b, h, n, d) in v.dtype."""
    n, d, dtype = q.shape[2], q.shape[3], v.dtype
    pad = -n % window  # blocks are aligned to end at the last token: pad on the left
    q, k, v, fq, fk = (F.pad(t.float(), (0, 0, pad, 0)).unflatten(2, (-1, window)) for t in (q, k, v, fq, fk))
    nb = q.shape[2]
    pos = torch.arange(nb * window, device=q.device).view(nb, window)
    fk = fk * (pos >= pad)[..., None]  # padded keys contribute nothing to the linear sums
    key_pos = torch.cat([pos - window, pos], 1)  # (nb, 2w) positions of the window keys
    ok = (key_pos[:, None, :] <= pos[:, :, None]) & (key_pos[:, None, :] >= pad)  # causal, no pads, no block -1
    s = torch.einsum("bhcid,bhcjd->bhcij", q, with_previous_block(k)) * d**-0.5
    s = s.masked_fill(~ok, -1e8)
    a = wf.float()[..., None] * torch.exp(s - s.amax(-1, keepdim=True))
    kv = F.pad(torch.einsum("bhcjf,bhcjd->bhcfd", fk, v).cumsum(2), (0, 0, 0, 0, 2, 0))[:, :, :nb]  # blocks <= c-2
    z = F.pad(fk.sum(3).cumsum(2), (0, 0, 2, 0))[:, :, :nb]
    y = torch.einsum("bhcij,bhcjd->bhcid", a, with_previous_block(v)) + torch.einsum("bhcif,bhcfd->bhcid", fq, kv)
    y = y / (a.sum(-1) + torch.einsum("bhcif,bhcf->bhci", fq, z))[..., None]
    return y.flatten(2, 3)[:, :, pad:].to(dtype)


def decode_state(k: Tensor, v: Tensor, fk: Tensor, window: int = WINDOW) -> tuple[Tensor, ...]:
    """(last-window keys, values, linear kv state, linear k state) after a prompt; states in v.dtype like theirs."""
    old = max(k.shape[2] - window, 0)
    kv = torch.einsum("bhnf,bhnd->bhfd", fk[:, :, :old].float(), v[:, :, :old].float()).to(v.dtype)
    return k[:, :, old:], v[:, :, old:], kv, fk[:, :, :old].float().sum(2, keepdim=True).to(v.dtype)


def decode_step(
    q: Tensor, k: Tensor, v: Tensor, fq: Tensor, state: tuple, wf: Tensor, wk: Tensor, window: int = WINDOW
) -> tuple[Tensor, tuple]:
    """One token: evict the oldest window key into the linear state, then window softmax + linear; (y, new state)."""
    kc, vc, kv, ks = state
    if kc.shape[2] >= window:
        f_old = feature_map(kc[:, :, :1], wk)
        kv = kv + torch.einsum("bhnf,bhnd->bhfd", f_old.float(), vc[:, :, :1].float()).to(kv.dtype)
        ks, kc, vc = ks + f_old, kc[:, :, 1:], vc[:, :, 1:]
    kc, vc = torch.cat([kc, k], 2), torch.cat([vc, v], 2)
    s = torch.einsum("bhmd,bhnd->bhmn", q.float(), kc.float()) * q.shape[-1] ** -0.5
    a = wf * torch.exp(s - s.amax(-1, keepdim=True))
    y = a @ vc.float() + fq.float() @ kv.float()
    y = y / (a.sum(-1, keepdim=True) + (fq.float() * ks.float()).sum(-1, keepdim=True))
    return y.to(v.dtype), (kc, vc, kv, ks)


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

import re

import torch
import torch.nn.functional as F
from huggingface_hub import hf_hub_download
from torch import Tensor
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.models.llama.modeling_llama import apply_rotary_pos_emb, repeat_kv

BASE = "meta-llama/Llama-3.1-8B"
WINDOW = 64
LORA_SCALE = 16 / 8
KEY = re.compile(r"layers\.(\d+)\.self_attn\.(feature_map_[qk]\.mlp\.layer|window_factors|[qkvo]_proj\.lora_[AB])(?:\.default)?(?:\.weight)?$")


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


class LolcatsAttention(torch.nn.Module):
    """Drop-in for LlamaAttention (same projections and call); the decode state lives in the HF cache of the call."""

    def __init__(self, base: torch.nn.Module, layer_idx: int, heads: int, kv_heads: int, feature_dim: int = 64):
        super().__init__()
        self.q_proj, self.k_proj, self.v_proj, self.o_proj = base.q_proj, base.k_proj, base.v_proj, base.o_proj
        self.layer_idx, self.heads, self.kv_heads = layer_idx, heads, kv_heads
        self.head_dim = self.q_proj.out_features // heads
        like = {"device": self.q_proj.weight.device, "dtype": self.q_proj.weight.dtype}
        self.fmap_q = torch.nn.Parameter(torch.empty(heads, self.head_dim, feature_dim, **like))
        self.fmap_k = torch.nn.Parameter(torch.empty(heads, self.head_dim, feature_dim, **like))
        self.window_factors = torch.nn.Parameter(torch.empty(1, heads, 1, 1, **like))

    def forward(self, hidden_states: torch.Tensor, position_embeddings: tuple, past_key_values: object = None, **_: object):
        b, n, _ = hidden_states.shape
        split = lambda x, h: x.view(b, n, h, self.head_dim).transpose(1, 2)  # noqa: E731
        q, k = apply_rotary_pos_emb(split(self.q_proj(hidden_states), self.heads),
                                    split(self.k_proj(hidden_states), self.kv_heads), *position_embeddings)
        k, v = (repeat_kv(x, self.heads // self.kv_heads) for x in (k, split(self.v_proj(hidden_states), self.kv_heads)))
        fq, wf = feature_map(q, self.fmap_q), torch.sigmoid(self.window_factors)
        states = vars(past_key_values).setdefault("rg_lolcats", {}) if past_key_values is not None else {}
        if self.layer_idx in states:
            y, states[self.layer_idx] = decode_step(q, k, v, fq, states[self.layer_idx], wf, self.fmap_k)
        else:
            fk = feature_map(k, self.fmap_k)
            y = prefill(q, k, v, fq, fk, wf)
            if past_key_values is not None:
                states[self.layer_idx] = decode_state(k, v, fk)
        if past_key_values is not None:  # one-wide dummies keep the HF cache length right
            dummy = hidden_states.new_zeros(b, 1, n, 1)
            past_key_values.update(dummy, dummy, self.layer_idx)
        return self.o_proj(y.transpose(1, 2).reshape(b, n, -1)), None


def checkpoint_tensors(repo_id: str) -> dict[tuple[int, str], torch.Tensor]:
    """{(layer, name): tensor} from a LoLCATs model.pt, whatever prefix (peft or plain) its keys carry."""
    sd = torch.load(hf_hub_download(repo_id, "model.pt"), map_location="cpu", weights_only=True)
    sd = sd.get("model_state_dict", sd)
    out = {(int(m[1]), m[2]): t for key, t in sd.items() if (m := KEY.search(key))}
    if len(out) != len(sd):
        raise ValueError(f"{repo_id}: unrecognised keys, e.g. {sorted(set(sd) - {k for k in sd if KEY.search(k)})[:3]}")
    return out


def load(model_id: str, attn: str) -> tuple[AutoTokenizer, torch.nn.Module]:
    distill = model_id.replace("-ft-lora", "-distill")
    tok = AutoTokenizer.from_pretrained(BASE)
    model = AutoModelForCausalLM.from_pretrained(BASE, dtype=torch.bfloat16, attn_implementation=attn, device_map="cuda")
    cfg = model.config
    fmaps = checkpoint_tensors(distill)
    lora = checkpoint_tensors(model_id) if model_id != distill else {}
    if {n for _, n in fmaps} != {"feature_map_q.mlp.layer", "feature_map_k.mlp.layer", "window_factors"} or any(
        "lora" not in n for _, n in lora
    ):
        raise ValueError(f"unexpected tensors: distill {sorted({n for _, n in fmaps})}, ft {sorted({n for _, n in lora})}")
    for i, layer in enumerate(model.model.layers):
        new = LolcatsAttention(layer.self_attn, i, cfg.num_attention_heads, cfg.num_key_value_heads)
        with torch.no_grad():
            new.fmap_q.copy_(fmaps[i, "feature_map_q.mlp.layer"])
            new.fmap_k.copy_(fmaps[i, "feature_map_k.mlp.layer"])
            new.window_factors.copy_(fmaps[i, "window_factors"])
            for p in ("q_proj", "k_proj", "v_proj", "o_proj") if lora else ():
                w = getattr(new, p).weight
                delta = lora[i, f"{p}.lora_B"].float().to(w.device) @ lora[i, f"{p}.lora_A"].float().to(w.device)
                w.copy_((w.float() + LORA_SCALE * delta).to(w.dtype))
        layer.self_attn = new
    print(f"lolcats: {len(fmaps)} feature-map tensors from {distill}, {len(lora)} LoRA tensors from {model_id}")
    return tok, model

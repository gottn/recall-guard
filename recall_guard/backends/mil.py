"""Mamba-in-the-Llama hybrids (Wang et al. 2024, github.com/jxiw/MambaInLlama): Llama-3.1 with the attention layers
outside `attn_layers` replaced by Mamba-2 layers distilled from them.

Mirrors the authors' evaluation path (mamba2/hybrid_wrapper.py, used by their lm-eval and needle scripts): HF Llama
attention layers, MambaInLlama Mamba-2 decoder layers, the whole model cast to bf16 as theirs is (rotary inv_freq
included). The skeleton is built from the checkpoint's own config, so Llama-3.1-8B-Instruct is never downloaded.
Their eval decodes with use_cache=False (a full recompute per token); here the Mamba layers keep their recurrent state
in the HF cache of the generate call instead, which is the same function computed incrementally.
No CUDA extension is needed: Mamba-2 runs on mamba_ssm's Triton kernels and the depthwise conv on torch."""

import importlib.util
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import torch
import torch.nn.functional as F
from huggingface_hub import hf_hub_download
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer


def causal_conv1d_torch(
    x: torch.Tensor, weight: torch.Tensor, bias: torch.Tensor | None = None, activation: str | None = None, seq_idx: None = None
) -> torch.Tensor:
    """causal_conv1d_fn semantics on (batch, dim, length): depthwise, left-padded, optional SiLU. MambaInLlama's own
    torch fallback keeps the last d_conv-1 positions instead of the first `length`, so it cannot be used."""
    assert seq_idx is None, "packed sequences need the causal_conv1d kernel"
    y = F.conv1d(x, weight.unsqueeze(1), bias, padding=weight.shape[1] - 1, groups=x.shape[1])[..., : x.shape[-1]]
    return F.silu(y) if activation in ("silu", "swish") else y


def cached_mixer_layer(base: type[torch.nn.Module]) -> type[torch.nn.Module]:
    """Subclass of a recurrent decoder layer (called as layer(h, inference_params=p), state in p.key_value_memory_dict,
    p.seqlen_offset > 0 meaning one-token steps) that takes HF decoder-layer keywords. Its state lives in the HF cache
    object of the current forward/generate call, so it is born and dies with that call. One-wide dummy key/values keep
    the cache's sequence length right: HF reads it from layer 0, which may be a recurrent layer."""

    class CachedMixerLayer(base):
        def forward(self, hidden_states: torch.Tensor, past_key_values: object = None, **_: object) -> torch.Tensor:
            if past_key_values is None:
                return super().forward(hidden_states)
            states = vars(past_key_values).setdefault("rg_mixer_states", {})
            params = states.setdefault(self.layer_idx, SimpleNamespace(seqlen_offset=0, key_value_memory_dict={}))
            out = super().forward(hidden_states, inference_params=params)
            params.seqlen_offset += hidden_states.shape[1]
            dummy = hidden_states.new_zeros(hidden_states.shape[0], 1, hidden_states.shape[1], 1)
            past_key_values.update(dummy, dummy, self.layer_idx)
            return out

    return CachedMixerLayer


def register_without_init(package: str) -> None:
    """Make `package` importable without running its __init__: mamba_ssm's imports the Mamba-1 CUDA extension
    (selective_scan_cuda), which Mamba-2 never uses and which is not built here."""
    if package not in sys.modules:
        sys.modules[package] = importlib.util.module_from_spec(importlib.util.find_spec(package))


def load(model_id: str, attn: str) -> tuple[AutoTokenizer, torch.nn.Module]:
    register_without_init("mamba_ssm")
    import mamba2.hybrid_mamba_layer as mamba_layer
    from mamba2.hybrid_mamba_config import MambaConfig
    from mamba2_inference.hybrid_model import MambaDecoderLayer

    if mamba_layer.causal_conv1d_fn is None:
        mamba_layer.causal_conv1d_fn = causal_conv1d_torch
    tok = AutoTokenizer.from_pretrained(model_id)
    mamba_cfg = MambaConfig(**json.loads(Path(hf_hub_download(model_id, "mamba_config.json")).read_text()))
    layer_cls = cached_mixer_layer(MambaDecoderLayer)
    with torch.device("cuda"):
        cfg = AutoConfig.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_config(cfg, dtype=torch.bfloat16, attn_implementation=attn)
        for i in sorted(set(range(mamba_cfg.n_layer)) - set(mamba_cfg.attn_layers)):
            model.model.layers[i] = layer_cls(mamba_cfg, i, device="cuda", dtype=torch.bfloat16)
    ckpt = hf_hub_download(model_id, "pytorch_model.bin")
    model.load_state_dict(torch.load(ckpt, map_location="cpu", mmap=True, weights_only=True), strict=True)
    return tok, model.to(torch.bfloat16)

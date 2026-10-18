"""Training-free baseline: copy the conversion source's query and key projections into the hybrid's retained
softmax-attention layers (QK-Restore of Attention Amnesia, arXiv 2606.11052, with the source transformer as the
reference checkpoint). Tensors are matched by name; a name whose shape differs is skipped, which excludes
Jet-Nemotron's linear-attention blocks, whose projections are also called q_proj/k_proj."""

import re

PATTERN = r"self_attn\.[qk]_proj\.(weight|bias)$"


def restorable(hybrid: dict[str, tuple[int, ...]], source: dict[str, tuple[int, ...]], pattern: str = PATTERN) -> tuple[str, ...]:
    """Names in `hybrid` that match `pattern` and exist in `source` with the same shape, sorted."""
    return tuple(sorted(n for n, s in hybrid.items() if re.search(pattern, n) and source.get(n) == s))


def restore(model, source_id: str, pattern: str = PATTERN) -> tuple[str, ...]:
    """Copy the matching tensors of `source_id` (its safetensors shards, read lazily) into `model`; returns the names."""
    from pathlib import Path

    import torch
    from huggingface_hub import snapshot_download
    from safetensors import safe_open

    params = dict(model.named_parameters())
    shapes = {n: tuple(p.shape) for n, p in params.items()}
    done: list[str] = []
    with torch.no_grad():
        for f in sorted(Path(snapshot_download(source_id, allow_patterns=["*.safetensors"])).glob("*.safetensors")):
            with safe_open(str(f), "pt", device="cpu") as h:
                source = {k: tuple(h.get_slice(k).get_shape()) for k in h.keys()}
                for n in restorable(shapes, source, pattern):
                    params[n].copy_(h.get_tensor(n).to(params[n].device, params[n].dtype))
                    done.append(n)
    return tuple(sorted(done))

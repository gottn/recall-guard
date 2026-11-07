"""Copy tensors of another checkpoint into a loaded model, by name. The training-free baseline: the conversion source's
query and key projections copied into the hybrid's retained softmax-attention layers (QK-Restore of Attention Amnesia,
arXiv 2606.11052, with the source transformer as the reference checkpoint). Tensors are matched by name; a name whose
shape differs is skipped, which excludes Jet-Nemotron's linear-attention blocks, whose projections are also called
q_proj/k_proj. exp10 moves a tensor only part of the way, to W + scale * (W_source - W) (scale 1 is the copy), and can
apply that change only while the model reads its prompt or only while it generates."""

import re

PATTERN = r"self_attn\.[qk]_proj\.(weight|bias)$"
PHASES = ("all", "prompt", "answer")  # in place; prefill calls only; one-token (generation) calls only


def module_name(key: str) -> str:
    """Checkpoint key -> parameter name: multimodal Qwen3.5 checkpoints nest the text model under `language_model.`,
    which transformers drops when it loads the text-only model."""
    return key.replace(".language_model.", ".")


def restorable(hybrid: dict[str, tuple[int, ...]], source: dict[str, tuple[int, ...]], pattern: str = PATTERN) -> tuple[str, ...]:
    """Names in `hybrid` that match `pattern` and exist in `source` (keys read through module_name) with the same shape."""
    source = {module_name(k): s for k, s in source.items()}
    return tuple(sorted(n for n, s in hybrid.items() if re.search(pattern, n) and source.get(n) == s))


def apply(model, name: str, source, scale: float = 1.0, phase: str = "all") -> None:
    """Move parameter `name` to W + scale * (source - W): in place (phase "all"), or through a forward hook on its Linear
    that adds scale * (source - W) x to calls over several positions ("prompt") or over one position ("answer")."""
    import torch

    p = model.get_parameter(name)
    target = torch.lerp(p.detach().float(), source.to(p.device, torch.float32), scale)  # exactly `source` at scale 1
    if phase == "all":
        with torch.no_grad():
            p.copy_(target)
        return
    if phase not in PHASES or not name.endswith(".weight"):
        raise ValueError(f"phase {phase!r} on {name}: phases other than 'all' take one of {PHASES} on a Linear weight")
    delta = (target - p.detach().float()).to(p.dtype)
    on_prefill = phase == "prompt"

    def hook(module, args, out):  # generate() reads the prompt in one call, then one token per call
        return out + torch.nn.functional.linear(args[0], delta) if (args[0].shape[-2] > 1) == on_prefill else out

    model.get_submodule(name.rsplit(".", 1)[0]).register_forward_hook(hook)


def restore(model, source_id: str, pattern: str = PATTERN, scale: float = 1.0, phase: str = "all") -> tuple[str, ...]:
    """Apply the matching tensors of `source_id` (its safetensors shards, read lazily) to `model`; returns the names."""
    from pathlib import Path

    import torch
    from huggingface_hub import snapshot_download
    from safetensors import safe_open

    shapes = {n: tuple(p.shape) for n, p in model.named_parameters()}
    done: list[str] = []
    with torch.no_grad():
        for f in sorted(Path(snapshot_download(source_id, allow_patterns=["*.safetensors"])).glob("*.safetensors")):
            with safe_open(str(f), "pt", device="cpu") as h:
                keys = {module_name(k): k for k in h.keys()}
                for n in restorable(shapes, {k: tuple(h.get_slice(k).get_shape()) for k in h.keys()}, pattern):
                    apply(model, n, h.get_tensor(keys[n]), scale, phase)
                    done.append(n)
    return tuple(sorted(done))

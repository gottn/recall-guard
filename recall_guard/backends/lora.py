"""Minimal LoRA, dependency-free: wrap chosen nn.Linear modules, train only the A/B factors, merge for evaluation.
Written because PEFT >= 0.21 refuses the cluster image's torchao 0.13 while torchao >= 0.16 needs torch >= 2.10."""

import json
import math
from pathlib import Path

import torch

SKIP_IN_NAME = ("mlp", "lm_head", "embed")


class LoRALinear(torch.nn.Module):
    """y = W x + (B A x) * alpha / r. A, B are float32; the base layer keeps its dtype and stays frozen."""

    def __init__(self, base: torch.nn.Linear, r: int, alpha: int):
        super().__init__()
        self.base, self.scale = base, alpha / r
        dev = base.weight.device
        self.A = torch.nn.Parameter(torch.empty(r, base.in_features, dtype=torch.float32, device=dev))
        self.B = torch.nn.Parameter(torch.zeros(base.out_features, r, dtype=torch.float32, device=dev))
        torch.nn.init.kaiming_uniform_(self.A, a=math.sqrt(5))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        delta = (x.to(torch.float32) @ self.A.T @ self.B.T) * self.scale
        return self.base(x) + delta.to(x.dtype)


def target_names(model: torch.nn.Module) -> tuple[str, ...]:
    """Leaf names of every nn.Linear outside the MLPs, head and embeddings (attention and linear-attention projections)."""
    return tuple(sorted({
        name.rsplit(".", 1)[-1]
        for name, m in model.named_modules()
        if isinstance(m, torch.nn.Linear) and not any(s in name for s in SKIP_IN_NAME)
    }))


def inject(model: torch.nn.Module, targets: tuple[str, ...], r: int, alpha: int) -> tuple[str, ...]:
    """Replace matching Linear modules in place; returns the full module paths that were wrapped."""
    for p in model.parameters():
        p.requires_grad_(False)
    wrapped = []
    for name, m in list(model.named_modules()):
        leaf = name.rsplit(".", 1)[-1]
        if isinstance(m, torch.nn.Linear) and leaf in targets and not any(s in name for s in SKIP_IN_NAME):
            parent = model.get_submodule(name.rsplit(".", 1)[0]) if "." in name else model
            setattr(parent, leaf, LoRALinear(m, r, alpha))
            wrapped.append(name)
    return tuple(wrapped)


def trainable(model: torch.nn.Module) -> list[torch.nn.Parameter]:
    return [p for p in model.parameters() if p.requires_grad]


def save(model: torch.nn.Module, out_dir: str, r: int, alpha: int) -> int:
    """Writes adapter.pt (A/B per wrapped module) and adapter_config.json; returns the number of adapter tensors."""
    state = {f"{n}.{k}": getattr(m, k).detach().cpu() for n, m in model.named_modules() if isinstance(m, LoRALinear) for k in ("A", "B")}
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    torch.save(state, Path(out_dir) / "adapter.pt")
    (Path(out_dir) / "adapter_config.json").write_text(json.dumps({"r": r, "alpha": alpha, "modules": sorted({k.rsplit(".", 1)[0] for k in state})}))
    return len(state)


@torch.no_grad()
def merge(model: torch.nn.Module, adapter_dir: str) -> int:
    """Fold B A * alpha / r into each wrapped Linear's weight; returns the number of merged layers."""
    cfg = json.loads((Path(adapter_dir) / "adapter_config.json").read_text())
    state = torch.load(Path(adapter_dir) / "adapter.pt", map_location="cpu")
    scale = cfg["alpha"] / cfg["r"]
    for name in cfg["modules"]:
        lin = model.get_submodule(name)
        delta = (state[f"{name}.B"] @ state[f"{name}.A"]) * scale
        lin.weight += delta.to(lin.weight.device, lin.weight.dtype)
    return len(cfg["modules"])


@torch.no_grad()
def attach(model: torch.nn.Module, adapter_dir: str) -> int:
    """Wrap the saved modules with LoRALinear and load A/B, leaving base weights untouched (unmerged inference)."""
    cfg = json.loads((Path(adapter_dir) / "adapter_config.json").read_text())
    state = torch.load(Path(adapter_dir) / "adapter.pt", map_location="cpu")
    leaves = tuple(sorted({n.rsplit(".", 1)[-1] for n in cfg["modules"]}))
    inject(model, leaves, cfg["r"], cfg["alpha"])
    for name in cfg["modules"]:
        m = model.get_submodule(name)
        m.A.copy_(state[f"{name}.A"].to(m.A.device))
        m.B.copy_(state[f"{name}.B"].to(m.B.device))
    return len(cfg["modules"])

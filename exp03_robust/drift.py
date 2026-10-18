"""How far each hybrid's retained attention projections sit from the source transformer's (float64 cosine and
relative Frobenius distance, per projection, over the retained layers). Reads the HF cache directly; run on the cluster:
  srun --partition=prioritized --qos=normal --cpus-per-task=4 --mem=64G --time=00:20:00 \
    singularity exec /home/container/pytorch/pytorch_25.09.sif python3 exp03_robust/drift.py"""

import glob
import os
from collections.abc import Callable

import torch
from safetensors import safe_open

HUB = os.path.expanduser("~/hf_cache/hub")


def safetensors_weights(repo: str, keep: Callable[[str], bool]) -> dict[str, torch.Tensor]:
    root = glob.glob(f"{HUB}/models--{repo.replace('/', '--')}/snapshots/*")[0]
    out = {}
    for f in sorted(glob.glob(root + "/*.safetensors")):
        with safe_open(f, "pt", device="cpu") as h:
            out.update({n: h.get_tensor(n).double() for n in h.keys() if keep(n)})
    return out


def cos(a: torch.Tensor, b: torch.Tensor) -> float:
    return float(torch.nn.functional.cosine_similarity(a.flatten(), b.flatten(), dim=0))


def rel(a: torch.Tensor, b: torch.Tensor) -> float:
    return float((a - b).norm() / b.norm())


def summary(tag: str, hyb: dict, src: dict, layers: tuple[int, ...]) -> None:
    for p in ("q_proj", "k_proj", "v_proj", "o_proj"):
        pairs = [(hyb[f"model.layers.{i}.self_attn.{p}.weight"], src[f"model.layers.{i}.self_attn.{p}.weight"]) for i in layers]
        c = [cos(a, b) for a, b in pairs]
        r = [rel(a, b) for a, b in pairs]
        print(f"{tag} {p}: cos min {min(c):.3f} mean {sum(c) / len(c):.3f} max {max(c):.3f} | "
              f"reldist min {min(r):.3f} mean {sum(r) / len(r):.3f} max {max(r):.3f}", flush=True)
    for name in (f"model.layers.{layers[0]}.mlp.up_proj.weight", "model.embed_tokens.weight"):
        print(f"{tag} {name}: cos {cos(hyb[name], src[name]):.3f} reldist {rel(hyb[name], src[name]):.3f}", flush=True)


def keep_for(layers: tuple[int, ...]) -> Callable[[str], bool]:
    return lambda n: any(f".layers.{i}.self_attn." in n or f".layers.{i}.mlp.up_proj" in n for i in layers) or n == "model.embed_tokens.weight"


if __name__ == "__main__":
    jet_layers = (14, 19, 20, 21)  # Jet-Nemotron-2B's softmax layers: two full, two sliding-window
    summary("jet-vs-qwen", safetensors_weights("jet-ai/Jet-Nemotron-2B", keep_for(jet_layers)),
            safetensors_weights("Qwen/Qwen2.5-1.5B", keep_for(jet_layers)), jet_layers)
    mil_layers = tuple(range(1, 32, 2))  # Mamba-in-the-Llama 8B keeps the odd layers as attention
    root = glob.glob(f"{HUB}/models--JunxiongWang--Llama3.1-Mamba2-8B-dpo/snapshots/*")[0]
    sd = torch.load(root + "/pytorch_model.bin", map_location="cpu", mmap=True, weights_only=True)
    keep = keep_for(mil_layers)
    summary("mil-vs-llama", {n: sd[n].double() for n in sd if keep(n)},
            safetensors_weights("meta-llama/Llama-3.1-8B-Instruct", keep), mil_layers)

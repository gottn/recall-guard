"""Premise checks behind exp10's design, run before any job (RESULTS.md, Premise). No GPU:
1. the edit's structure, from the two edited down_proj tensors of both checkpoints (range requests, ~30 MB);
2. exp08's multi-value losses against its 64-token cap, from exp08's stored completions.
python exp10_wsp_tradeoff/premise.py"""

import json
import re
import struct
import urllib.request
from pathlib import Path

import torch
from transformers import AutoTokenizer

FILE = "model.safetensors-00001-of-00001.safetensors"
BASE = "https://huggingface.co/Qwen/Qwen3.5-0.8B/resolve/2fc06364715b967f1860aea9cf38778875588b17/" + FILE
EDIT = "https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming/resolve/d1671a178705bcab7644806d23c535517f35723b/" + FILE
X8 = Path(__file__).parent.parent / "exp08_wsp_gate/results/raw/robust"
TOK = AutoTokenizer.from_pretrained("Qwen/Qwen3.5-0.8B", revision="2fc06364715b967f1860aea9cf38778875588b17")


def fetch(url: str, start: int, end: int) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Range": f"bytes={start}-{end - 1}"})) as r:
        data = r.read()
    assert len(data) == end - start, f"short read from {url}"
    return data


def tensor(url: str, name: str) -> torch.Tensor:
    n = struct.unpack("<Q", fetch(url, 0, 8))[0]
    meta = json.loads(fetch(url, 8, 8 + n))[name]
    start, end = meta["data_offsets"]
    return torch.frombuffer(bytearray(fetch(url, 8 + n + start, 8 + n + end)), dtype=torch.bfloat16).reshape(meta["shape"]).float()


units = {}
for layer in (15, 19):
    name = f"model.language_model.layers.{layer}.mlp.down_proj.weight"
    w, e = tensor(BASE, name), tensor(EDIT, name)
    cols = ((e - w).abs().sum(0) > 0).nonzero().flatten()
    u, s, _ = torch.linalg.svd((e - w)[:, cols], full_matrices=False)
    units[layer] = u[:, 0]
    ratio = (u[:, 0] @ e[:, cols]) / (u[:, 0] @ w[:, cols])  # edited / base component along the change's direction
    print(f"layer {layer}: {len(cols)} columns changed; first singular value holds {float(s[0] ** 2 / (s**2).sum()):.6f} of the "
          f"change; each column's component along it is x{float(ratio.mean()):.4f} the base's (range {float(ratio.min()):.4f} "
          f"to {float(ratio.max()):.4f}); the change is {float((e - w).norm() / w.norm()):.3f} of the tensor's norm")
print(f"cosine between the two layers' directions: {float(abs(units[15] @ units[19])):.3f}")

for length in (16384, 32768):
    rows = {m: [json.loads(x) for x in open(X8 / f"ruler-{length}-base-{m}.jsonl")]
            for m in ("Qwen_Qwen3.5-0.8B", "RikiyaT_Qwen3.5-0.8B-weight-space-programming")}
    pairs = [(b, e) for b, e in zip(*rows.values(), strict=True) if b["task"] == "ruler_niah_multivalue"]
    lost = [(b, e) for b, e in pairs if b["contains"] and not e["contains"]]
    tokens = [len(TOK(e["output"], add_special_tokens=False).input_ids) for _, e in lost]
    capped = sum(n >= 64 for n in tokens)  # the completion re-encodes to the cap: cut off mid-list
    three = sum(n < 64 and len(re.findall(r"\d{7}", e["output"])) == 3 for n, (_, e) in zip(tokens, lost, strict=True))
    bold = sum(re.search(r"numbers for \*\*[a-z-]+\*\*", e["output"]) is not None for _, e in lost)
    base_cut = sum(not b["contains"] and re.search(r"\d{1,6}\**$", b["output"]) is not None for b, _ in pairs)
    print(f"multi-value {length}: {len(lost)} lost, {sum(e['contains'] and not b['contains'] for b, e in pairs)} gained; "
          f"{capped} end at the 64-token cap, {three} stop after three values; {bold} bold the key; the base's own "
          f"{sum(not b['contains'] for b, _ in pairs)} misses end in a cut-off number in {base_cut}")
    single = [e for b, e in zip(*rows.values(), strict=True) if b["task"] == "ruler_niah_single_1"]
    print(f"single needle {length}: {sum(e['output'].startswith('The grass is green.') for e in single)} of {len(single)} edited "
          f"answers open with the haystack, {sum(bool(re.search(r'[0-9]{7}', e['output'])) for e in single)} contain a seven-digit number")

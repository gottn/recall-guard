"""Premise check: the published edited checkpoint has the base's tensor layout, and its two edited tensors match the
model card's sha256 and differ from the base only in the claimed columns. Range requests only (~30 MB, no full download):
python exp08_wsp_gate/edit_check.py"""

import hashlib
import json
import struct
import urllib.request
from array import array

FILE = "model.safetensors-00001-of-00001.safetensors"
BASE = "https://huggingface.co/Qwen/Qwen3.5-0.8B/resolve/2fc06364715b967f1860aea9cf38778875588b17/" + FILE
EDIT = "https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming/resolve/d1671a178705bcab7644806d23c535517f35723b/" + FILE
CARD_SHA256 = {  # sha256 of the raw bfloat16 bytes, from the edited model card
    "model.language_model.layers.15.mlp.down_proj.weight": "82e2d733ea64feaeb4af93a1e065641d3df98b494a8b7576ef2f52e90fe2ee53",
    "model.language_model.layers.19.mlp.down_proj.weight": "8ef3c61bc36af113ad58e89dbb0a4a14dcba5a45cb750c15ab515c82ddd12eb2",
}


def fetch(url: str, start: int, end: int) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"Range": f"bytes={start}-{end - 1}"})) as r:
        data = r.read()
    assert len(data) == end - start, f"short read from {url}: {len(data)} of {end - start} bytes"
    return data


def header(url: str) -> tuple[int, dict]:
    """(byte offset of the tensor data, header JSON) of a safetensors file."""
    n = struct.unpack("<Q", fetch(url, 0, 8))[0]
    return 8 + n, json.loads(fetch(url, 8, 8 + n))


(b0, hb), (e0, he) = header(BASE), header(EDIT)
mb, me = hb.pop("__metadata__", {}), he.pop("__metadata__", {})
same = {k: (v["dtype"], v["shape"]) for k, v in hb.items()} == {k: (v["dtype"], v["shape"]) for k, v in he.items()}
print(f"{len(hb)} / {len(he)} tensors, same names, dtypes and shapes: {same}; metadata base {mb}, edited {me}")
for name, want in CARD_SHA256.items():
    (bs, be), (es, ee) = hb[name]["data_offsets"], he[name]["data_offsets"]  # the two files order their tensors differently
    cols = he[name]["shape"][1]
    raw = fetch(EDIT, e0 + es, e0 + ee)
    a, b = array("H", fetch(BASE, b0 + bs, b0 + be)), array("H", raw)  # bf16 compared as raw 16-bit words
    diff = [i for i in range(len(a)) if a[i] != b[i]]
    print(f"{name} {he[name]['dtype']} {he[name]['shape']}: sha256 matches card {hashlib.sha256(raw).hexdigest() == want}, "
          f"{len(diff)} weights differ from base in {len({i % cols for i in diff})} columns x {len({i // cols for i in diff})} rows")

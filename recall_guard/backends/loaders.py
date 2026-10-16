"""Model families AutoModelForCausalLM cannot build: model-id prefix -> "module:function" of their loader.

Targets are strings so this table imports nothing heavy. Every loader has the signature (model_id, attn) and returns
(tokenizer, model) with the hf.load contract: model.generate(input_ids, max_new_tokens=..., do_sample=False,
pad_token_id=...) returns prompt + completion ids, model.device is set, and model(input_ids=...).logits works."""

import importlib
from collections.abc import Callable

LOADERS: tuple[tuple[str, str], ...] = (
    ("JunxiongWang/Llama3.1-Mamba2-", "recall_guard.backends.mil:load"),
    ("JunxiongWang/Llama3.2-Mamba2-", "recall_guard.backends.mil:load"),
    ("hazyresearch/lolcats-llama-3.1-8b-", "recall_guard.backends.lolcats:load"),
)


def loader_for(model_id: str) -> str:
    """The target registered for the longest prefix of `model_id`, or "" when the AutoModel path applies."""
    hits = sorted((p for p, _ in LOADERS if model_id.startswith(p)), key=len)
    return dict(LOADERS)[hits[-1]] if hits else ""


def resolve(target: str) -> Callable:
    """Import a "module:function" target lazily (the loader's dependencies exist only in its cluster env)."""
    module, fn = target.split(":")
    return getattr(importlib.import_module(module), fn)

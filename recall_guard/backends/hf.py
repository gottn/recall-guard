"""HuggingFace completion backend: the only code that loads a model or touches a GPU.
Greedy decoding, one prompt at a time (prompts up to 32K tokens; batching would only add padding)."""

import time

import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

DTYPE_KWARG = "dtype" if int(transformers.__version__.split(".")[0]) >= 5 else "torch_dtype"


def load(model_id: str, attn: str, trust_remote_code: bool) -> tuple[AutoTokenizer, AutoModelForCausalLM]:
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=trust_remote_code)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    kwargs = {DTYPE_KWARG: torch.bfloat16 if device == "cuda" else torch.float32}
    model = AutoModelForCausalLM.from_pretrained(
        model_id, attn_implementation=attn, trust_remote_code=trust_remote_code, device_map=device, **kwargs
    )
    return tok, model.eval()


@torch.inference_mode()
def complete(tok: AutoTokenizer, model: AutoModelForCausalLM, prompt: str, max_new_tokens: int) -> tuple[str, float]:
    """(completion text, wall seconds) for one prompt; the prompt itself is excluded from the text."""
    ids = tok(prompt, return_tensors="pt").input_ids.to(model.device)
    t0 = time.perf_counter()
    out = model.generate(
        ids, max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=tok.pad_token_id or tok.eos_token_id
    )
    if model.device.type == "cuda":
        torch.cuda.synchronize()
    return tok.decode(out[0, ids.shape[1] :], skip_special_tokens=True), time.perf_counter() - t0

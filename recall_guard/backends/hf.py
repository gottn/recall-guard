"""HuggingFace completion backend: the only code that loads a model or touches a GPU.
Greedy decoding, one prompt at a time (prompts up to 32K tokens; batching would only add padding)."""

import math
import time

import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

DTYPE_KWARG = "dtype" if int(transformers.__version__.split(".")[0]) >= 5 else "torch_dtype"


def load(
    model_id: str, attn: str, trust_remote_code: bool, adapter: str = "", adapter_mode: str = "merge"
) -> tuple[AutoTokenizer, AutoModelForCausalLM]:
    """Base model, or base + adapter: merged into the weights (default) or attached unmerged (a check that merging is exact)."""
    tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=trust_remote_code)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    kwargs = {DTYPE_KWARG: torch.bfloat16 if device == "cuda" else torch.float32}
    model = AutoModelForCausalLM.from_pretrained(
        model_id, attn_implementation=attn, trust_remote_code=trust_remote_code, device_map=device, **kwargs
    )
    if adapter:
        from recall_guard.backends import lora

        (lora.merge if adapter_mode == "merge" else lora.attach)(model, adapter)
    return tok, model.eval()


@torch.inference_mode()
def no_think_prefill(tok: AutoTokenizer) -> str:
    """The official empty reasoning block for models with a <think> token (Qwen3 family); empty otherwise."""
    return "<think>\n\n</think>\n\n" if "<think>" in tok.get_vocab() else ""


def chat_wrap(tok: AutoTokenizer, prompt: str) -> str:
    """Render the prompt as a single user turn with the model's chat template (an alternative-explanation check)."""
    return tok.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True)


def complete(
    tok: AutoTokenizer, model: AutoModelForCausalLM, prompt: str, prefill: str, max_new_tokens: int, chat: bool = False
) -> tuple[str, float, int]:
    """(completion text, wall seconds, prompt tokens) for one prompt; prompt and prefill are excluded from the text."""
    text = (chat_wrap(tok, prompt) if chat else prompt) + prefill
    ids = tok(text, return_tensors="pt", add_special_tokens=not chat).input_ids.to(model.device)
    t0 = time.perf_counter()
    out = model.generate(
        ids, max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=tok.pad_token_id or tok.eos_token_id
    )
    if model.device.type == "cuda":
        torch.cuda.synchronize()
    return tok.decode(out[0, ids.shape[1] :], skip_special_tokens=True), time.perf_counter() - t0, int(ids.shape[1])


@torch.inference_mode()
def bits_per_byte(tok: AutoTokenizer, model: AutoModelForCausalLM, text: str, window_tokens: int) -> float:
    """Bits per byte of `text` over one window of `window_tokens` tokens: a long-context language-modelling damage check."""
    ids = tok(text, return_tensors="pt", add_special_tokens=False).input_ids[:, :window_tokens].to(model.device)
    logits = model(input_ids=ids).logits[0, :-1].float()
    nll = torch.nn.functional.cross_entropy(logits, ids[0, 1:], reduction="sum").item()
    n_bytes = len(tok.decode(ids[0, 1:]).encode("utf-8"))
    return nll / math.log(2) / n_bytes

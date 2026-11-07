"""HuggingFace completion backend: the only code that loads a model or touches a GPU.
Greedy decoding, one prompt at a time (prompts up to 32K tokens; batching would only add padding)."""

import math
import sys
import time

import torch
import transformers
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    LogitsProcessor,
    LogitsProcessorList,
    TemperatureLogitsWarper,
    TopKLogitsWarper,
    TopPLogitsWarper,
)

from recall_guard.backends import loaders

DTYPE_KWARG = "dtype" if int(transformers.__version__.split(".")[0]) >= 5 else "torch_dtype"


def load(
    model_id: str, attn: str, trust_remote_code: bool, adapter: str = "", adapter_mode: str = "merge",
    restore_from: str = "", restore_pattern: str = "", restore_scale: float = 1.0, restore_phase: str = "all",
) -> tuple[AutoTokenizer, AutoModelForCausalLM]:
    """Base model, or base + adapter: merged into the weights (default) or attached unmerged (a check that merging is exact).
    Families registered in loaders.py (converted hybrids AutoModel cannot build) go through their own loader."""
    target = loaders.loader_for(model_id)
    if target:
        tok, model = loaders.resolve(target)(model_id, attn)
    else:
        tok = AutoTokenizer.from_pretrained(model_id, trust_remote_code=trust_remote_code)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        kwargs = {DTYPE_KWARG: torch.bfloat16 if device == "cuda" else torch.float32}
        model = AutoModelForCausalLM.from_pretrained(
            model_id, attn_implementation=attn, trust_remote_code=trust_remote_code, device_map=device, **kwargs
        )
    if restore_from:  # training-free baseline or exp10's partial edit, applied before any adapter
        from recall_guard.backends import restore

        pattern = restore_pattern or restore.PATTERN
        names = restore.restore(model, restore_from, pattern, restore_scale, restore_phase)
        if not names:  # a silent no-op would make every edit variant look like the base model
            sys.exit(f"recall-guard: {pattern!r} matches no tensor of {restore_from} with the model's name and shape")
        layers = sorted({int(x) for n in names for x in n.split(".") if x.isdigit()})
        print(f"  restored {len(names)} tensors from {restore_from} in layers {layers}, scale {restore_scale:g}, "
              f"phase {restore_phase}: {', '.join(names)}", file=sys.stderr)
    if adapter:  # the adapter names modules by path, which is the same structure whichever loader built the model
        from recall_guard.backends import lora

        (lora.merge if adapter_mode == "merge" else lora.attach)(model, adapter)
    return tok, model.eval()


def peak_memory_gib() -> float:
    """Peak memory torch allocated on the GPU in this process, GiB (0 on CPU)."""
    return torch.cuda.max_memory_allocated() / 2**30 if torch.cuda.is_available() else 0.0


@torch.inference_mode()
def no_think_prefill(tok: AutoTokenizer) -> str:
    """The official empty reasoning block for models with a <think> token (Qwen3 family); empty otherwise."""
    return "<think>\n\n</think>\n\n" if "<think>" in tok.get_vocab() else ""


def chat_wrap(tok: AutoTokenizer, prompt: str, thinking: bool = False) -> str:
    """Render the prompt as a single user turn with the model's chat template (an alternative-explanation check).
    `thinking`: Qwen3.5-0.8B's template opens an empty think block unless `enable_thinking` is passed as true."""
    return tok.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True,
                                   **({"enable_thinking": True} if thinking else {}))


class PresencePenalty(LogitsProcessor):
    """vLLM's presence penalty: every token generated so far loses `penalty` from its logit (the prompt does not count)."""

    def __init__(self, penalty: float, prompt_tokens: int):
        self.penalty, self.prompt_tokens = penalty, prompt_tokens

    def __call__(self, input_ids: torch.LongTensor, scores: torch.FloatTensor) -> torch.FloatTensor:
        return scores - self.penalty * torch.zeros_like(scores).scatter_(1, input_ids[:, self.prompt_tokens :], 1.0)


@torch.inference_mode()
def sample(
    tok: AutoTokenizer, model: AutoModelForCausalLM, prompts: list[str], max_new_tokens: int, seed: int,
    stop: tuple[int, ...], temperature: float, top_p: float, top_k: int, presence_penalty: float,
) -> list[list[int]]:
    """Generated ids per prompt, one left-padded batch, sampled in vLLM's order: presence penalty, then temperature,
    top-k, top-p. A row ends at any id in `stop` and is padded after it."""
    tok.padding_side = "left"
    enc = tok(prompts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
    n = enc.input_ids.shape[1]
    procs = LogitsProcessorList([PresencePenalty(presence_penalty, n), TemperatureLogitsWarper(temperature),
                                 TopKLogitsWarper(top_k), TopPLogitsWarper(top_p)])
    torch.manual_seed(seed)
    out = model.generate(**enc, max_new_tokens=max_new_tokens, do_sample=True, temperature=1.0, top_k=0, top_p=1.0,
                         logits_processor=procs, eos_token_id=list(stop), pad_token_id=tok.pad_token_id)
    return [row[n:].tolist() for row in out]


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

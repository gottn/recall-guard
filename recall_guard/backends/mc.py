"""Multiple-choice log-likelihood benchmarks (ARC-Easy, HellaSwag) to check a repair did no general damage.
acc = argmax of summed log-prob; acc_norm = argmax of log-prob per character (lm-eval's convention)."""

import math

import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

BENCHES = ("arc_easy", "hellaswag")


def load_items(bench: str, n: int, seed: int) -> tuple[tuple[str, tuple[str, ...], int], ...]:
    """(prompt, choices, gold index) triples, a fixed random subset of the validation split."""
    if bench == "arc_easy":
        ds = load_dataset("allenai/ai2_arc", "ARC-Easy", split="validation")
        items = tuple(
            (f"Question: {r['question']}\nAnswer:", tuple(" " + c for c in r["choices"]["text"]), r["choices"]["label"].index(r["answerKey"]))
            for r in ds
        )
    elif bench == "hellaswag":
        ds = load_dataset("Rowan/hellaswag", split="validation")
        items = tuple((r["ctx"], tuple(" " + e for e in r["endings"]), int(r["label"])) for r in ds)
    else:
        raise ValueError(bench)
    g = torch.Generator().manual_seed(seed)
    idx = torch.randperm(len(items), generator=g)[:n].tolist()
    return tuple(items[i] for i in idx)


@torch.inference_mode()
def choice_logprobs(tok: AutoTokenizer, model: AutoModelForCausalLM, prompt: str, choices: tuple[str, ...]) -> tuple[float, ...]:
    p_ids = tok(prompt, add_special_tokens=False).input_ids
    out = []
    for c in choices:
        c_ids = tok(c, add_special_tokens=False).input_ids
        ids = torch.tensor([p_ids + c_ids], device=model.device)
        logits = model(input_ids=ids).logits[0, len(p_ids) - 1 : -1].float()
        lp = torch.log_softmax(logits, -1).gather(1, torch.tensor(c_ids, device=model.device)[:, None]).sum().item()
        out.append(lp)
    return tuple(out)


def accuracy(tok: AutoTokenizer, model: AutoModelForCausalLM, items: tuple[tuple[str, tuple[str, ...], int], ...]) -> dict:
    acc = acc_norm = 0
    for prompt, choices, gold in items:
        lps = choice_logprobs(tok, model, prompt, choices)
        acc += int(max(range(len(lps)), key=lambda i: lps[i]) == gold)
        acc_norm += int(max(range(len(lps)), key=lambda i: lps[i] / max(1, len(choices[i]))) == gold)
    n = len(items)
    return {"n": n, "acc": acc / n, "acc_norm": acc_norm / n, "se": math.sqrt(0.25 / n)}

"""Two audits of the scoring (RESULTS.md item 32). Reads the committed raw
outputs only. Run on the Mac: .venv/bin/python exp03_robust/ruler_budget.py

1. RULER multi-value and multi-query completions against the 64-new-token budget. The Qwen2.5 tokenizer encodes one
   digit per token, so a four-number answer with a formatted list can exceed the budget. Per cell: completions that reach
   the budget, misses, and misses that end inside a number (an upper bound on answers cut off), repeat a value (a loop),
   or list four or more distinct numbers (wrong values).
2. Suite scoring at 32K: the `contains` rule (answer among the codes on the first line) against `exact` (first code is
   the answer), and the share of first lines carrying more than one code."""

import glob
import json
import re
from collections import Counter
from pathlib import Path

RAW = Path(__file__).resolve().parent / "results/raw"
QWEN_TOKENIZER = "Qwen/Qwen2.5-1.5B"
LLAMA_TOKENIZER = "unsloth/Llama-3.1-8B-Instruct"  # ungated mirror of meta-llama/Llama-3.1-8B-Instruct's tokenizer files
BUDGET = 64
PAIRS = (
    ("2B", "Qwen_Qwen2.5-1.5B", QWEN_TOKENIZER, ("base", "repair-seed1", "repair-seed2")),
    ("2B", "jet-ai_Jet-Nemotron-2B", QWEN_TOKENIZER, ("base", "repair-seed1", "repair-seed2", "repair-seed3")),
    ("8B", "meta-llama_Llama-3.1-8B-Instruct", LLAMA_TOKENIZER, ("base",)),
    ("8B", "JunxiongWang_Llama3.1-Mamba2-8B-dpo", LLAMA_TOKENIZER, ("base", "repair-seed1-gentle", "repair-seed2-gentle", "repair-seed3-gentle")),
)
MULTI_TASKS = ("ruler_niah_multivalue", "ruler_niah_multiquery")
SUITE_TASKS = ("needle", "many_random", "many_similar", "updated", "multihop", "heldout_many")
SEVEN = re.compile(r"\d{7}")
SIX = re.compile(r"\d{6}")
ENDS_IN_NUMBER = re.compile(r"(?<!\d)\d{1,6}$")
THINK = re.compile(r"<think>.*?(</think>|$)", re.DOTALL)


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.open() if line.strip()]


def tokenizer(name: str):
    try:
        from transformers import AutoTokenizer

        return AutoTokenizer.from_pretrained(name)
    except Exception as e:
        print(f"(no tokenizer {name}: {str(e).splitlines()[0][:60]}; budget hits not counted)")
        return None


STILL_LISTING = 40  # characters after the last seven-digit value: within this, a budget-cut completion was still listing values


def classify(output: str, tok) -> tuple[bool, str]:
    """(reached the budget, kind of miss): 'wrong' lists >= 4 distinct numbers, 'loop' repeats one, 'open' reached the
    budget with fewer than four values while still listing them (ends inside a number, or at most STILL_LISTING
    characters after the last value), so it could be an answer cut short; 'other' stopped early or drifted into prose."""
    numbers = SEVEN.findall(output)
    at_budget = tok is not None and len(tok(output, add_special_tokens=False).input_ids) >= BUDGET
    tail = len(output.rstrip()) - output.rfind(numbers[-1]) - 7 if numbers else len(output)
    if len(set(numbers)) >= 4:
        kind = "wrong"
    elif max(Counter(numbers).values(), default=0) >= 2:
        kind = "loop"
    elif at_budget and (ENDS_IN_NUMBER.search(output.rstrip()) or tail <= STILL_LISTING):
        kind = "open"
    else:
        kind = "other"
    return at_budget, kind


def budget_table() -> None:
    print("| scale | model | state | length | task | n | recalled | at budget | misses | wrong | loop | open | other |")
    print("|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    worst = {}
    for scale, model, tok_name, tags in PAIRS:
        tok = tokenizer(tok_name)
        for tag in tags:
            for length in (16384, 32768):
                path = RAW / f"ruler-{length}-{tag}-{model}.jsonl"
                if not path.exists():
                    continue
                for task in MULTI_TASKS:
                    rs = [r for r in rows(path) if r["task"] == task]
                    hits = sum(r["contains"] for r in rs)
                    kinds, at_budget = Counter(), 0
                    for r in rs:
                        b, kind = classify(r["output"], tok)
                        at_budget += b
                        if not r["contains"]:
                            kinds[kind] += 1
                    print(f"| {scale} | {model} | {tag} | {length} | {task[10:]} | {len(rs)} | {hits / len(rs):.2f} | {at_budget} "
                          f"| {len(rs) - hits} | {kinds['wrong']} | {kinds['loop']} | {kinds['open']} | {kinds['other']} |")
                    key = f"{scale} {'untrained' if tag == 'base' else 'repaired'}"
                    worst[key] = max(worst.get(key, 0), kinds["open"] / len(rs))
    print("\nlargest share of possibly cut-off answers ('open') in any cell: " + ", ".join(f"{k} {v:.2f}" for k, v in worst.items()))


def scoring_table() -> None:
    """Every (model, adapter, task, length) cell of the exp03 suites: the cells where `exact` differs from `contains`."""
    cells = differing = 0
    print("\n| model | adapter | task | length | n | contains | exact | first lines with > 1 code |")
    print("|---|---|---|---:|---:|---:|---:|---:|")
    for _, model, _, _ in PAIRS:
        tags = sorted({Path(f).name.split(f"-{model}")[0].split("-", 2)[2] for f in glob.glob(str(RAW / f"suite-s?-*-{model}.jsonl"))})
        for tag in tags:
            for task in SUITE_TASKS:
                for length in (16384, 32768):
                    rs = [r for f in glob.glob(str(RAW / f"suite-s?-{tag}-{model}.jsonl")) for r in rows(Path(f))
                          if r["task"] == task and r["length_bucket"] == length]
                    if not rs:
                        continue
                    cells += 1
                    contains, exact = sum(r["contains"] for r in rs) / len(rs), sum(r["exact"] for r in rs) / len(rs)
                    if contains != exact:
                        differing += 1
                        multi = sum(len(SIX.findall(first_line(r["output"]))) > 1 for r in rs)
                        print(f"| {model} | {tag} | {task} | {length} | {len(rs)} | {contains:.2f} | {exact:.2f} | {multi / len(rs):.2f} |")
    print(f"\n{differing} of {cells} cells differ between the two rules")


def first_line(output: str) -> str:
    return next((ln.strip() for ln in THINK.sub("", output).splitlines() if ln.strip()), "")


if __name__ == "__main__":
    budget_table()
    scoring_table()

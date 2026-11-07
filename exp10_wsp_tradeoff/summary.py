"""Every exp10 number: reads results/raw (and, for item counts, the git-ignored case files in results/cases), applies
the rules pre-registered in RESULTS.md and prints markdown. Run by `run_all.sh report`; a missing file skips its rows.
python exp10_wsp_tradeoff/summary.py [raw dir] [cases dir]   (other directories: the dry run on stand-in files)"""

import json
import sys
from collections import defaultdict
from pathlib import Path

from recall_guard.aggregate import binomial_tail_half, deltas, regressions, rows
from recall_guard.types import Result

HERE = Path(__file__).parent
RAW = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "results/raw"
CASES = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "results/cases"
X8 = HERE.parent / "exp08_wsp_gate/results/raw"
BASE, EDIT = "Qwen_Qwen3.5-0.8B", "RikiyaT_Qwen3.5-0.8B-weight-space-programming"
VARIANTS = {"c1": "base", "c0": "removal", "cm1": "reflection", "cm3": "c = -3", "cm5": "published", "cm5-L15": "layer 15 only",
            "cm5-L19": "layer 19 only", "cm5-prompt": "edit while reading", "cm5-answer": "edit while generating"}
GATED = ("c0", "cm1", "cm3", "cm5-L15", "cm5-L19")  # c1 and cm5 are exp08's base and edited runs
SETS = ("suite-s1", "suite-s2", "heldout", "multihop25", "step1", "qa")
QA = (4096, 16384, 32768)
CELLS = ("hay_p1_k1", "hay_p5_k1", "hay_p50_k1", "hay_r50_k1", "hay_filler_k1", "hay_filler_k2", "hay_filler_k4", "hay_filler_k8")
ECHO = "The grass is green."


def jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.open()] if path.exists() else []


def results(paths: list[Path]) -> tuple[Result, ...]:
    return tuple(Result(**d) for p in paths for d in jsonl(p))


def x8(model: str, name: str) -> list[Path]:
    if name == "step1":
        return [X8 / f"step1/{model}.jsonl"]
    if name == "qa":
        return [X8 / f"qa/ruler-{n}-base-{model}.jsonl" for n in QA]
    return [X8 / f"robust/{name}-base-{model}.jsonl"]


def gate(tag: str) -> tuple[int, int, float, list[str]] | None:
    """Base -> tag on exp08's six sets: pooled lost, gained, candidate recall, failing checks; None if a file is missing."""
    lost = gained = recalled = n = 0
    fails: list[str] = []
    for name in SETS:
        cand = x8(EDIT, name) if tag == "cm5" else [RAW / f"qa-ruler-{q}-{tag}.jsonl" for q in QA] if name == "qa" else [RAW / f"{name}-{tag}.jsonl"]
        if not all(p.exists() for p in x8(BASE, name) + cand):
            return None
        table = deltas(results(x8(BASE, name)), results(cand))
        lost, gained, n = lost + table[0].lost, gained + table[0].gained, n + table[0].n
        recalled += round(table[0].candidate_rate * table[0].n)
        fails += [f"{name} {d.task}@{d.length_bucket}" if d.length_bucket else f"{name} pooled" for d in regressions(table)]
    return lost, gained, recalled / n, fails


def two_sided(b: int, c: int) -> float:
    return min(1.0, 2 * binomial_tail_half(max(b, c), b + c)) if b + c else 1.0


def items(output: str, answer: str) -> int:
    return sum(v in output for v in answer.split("|"))


niah = {t: jsonl(RAW / f"niah-16384-{t}.jsonl") for t in VARIANTS}
loops = {t: {d["id"]: d for d in jsonl(RAW / f"loops-{t}.jsonl")} for t in VARIANTS}
sweep = {t: results([RAW / f"sweep-{t}.jsonl"]) for t in VARIANTS}
ruler_cases = defaultdict(list)
for d in jsonl(CASES / "ruler-16384.jsonl"):
    ruler_cases[d["id"]].append(d["answer"])
ruler_answers = {i: a[0] for i, a in ruler_cases.items() if len(a) == 1}  # RULER repeats some ids: those are not counted
sweep_answers = {d["id"]: d["answer"] for d in jsonl(CASES / "sweep.jsonl")}
ran = [t for t in VARIANTS if niah[t] or loops[t] or sweep[t]]

print("## V1: reproduction of exp08 (first 64 tokens of the 192-token answers)\n")
for tag, model in (("c1", BASE), ("cm5", EDIT)):
    old = defaultdict(list)
    for d in jsonl(X8 / f"robust/ruler-16384-base-{model}.jsonl"):
        if d["task"] in ("ruler_niah_single_1", "ruler_niah_multivalue"):
            old[d["case_id"]].append(d["output"])
    new = defaultdict(list)
    for d in niah[tag]:
        new[d["case_id"]].append(d["output"])
    pairs = [(o, n) for cid in old for o, n in zip(sorted(old[cid]), sorted(new.get(cid, [])), strict=False)]
    print(f"- {tag}: {sum(n.startswith(o) for o, n in pairs)} of {len(pairs)} exp10 answers start with exp08's {model} answer")

print("\n## Needles at 16K, 192 new tokens (RULER's exp08 file)\n")
print("| variant | | single recall | echo | echo, then the answer | multi-value all four | mean values found (unique ids) |")
print("|---|---|---:|---:|---:|---:|---:|")
E, MV = {}, {}
for t in ran:
    single = [d for d in niah[t] if d["task"] == "ruler_niah_single_1"]
    multi = [d for d in niah[t] if d["task"] == "ruler_niah_multivalue"]
    if not single:
        continue
    E[t] = sum(not d["contains"] and ECHO in d["output"] for d in single) / len(single)
    MV[t] = sum(d["contains"] for d in multi) / max(1, len(multi))
    found = [items(d["output"], ruler_answers[d["case_id"]]) for d in multi if d["case_id"] in ruler_answers]
    print(f"| {t} | {VARIANTS[t]} | {sum(d['contains'] for d in single) / len(single):.2f} | {E[t]:.2f} | "
          f"{sum(d['contains'] and ECHO in d['output'] for d in single) / len(single):.2f} | {MV[t]:.2f} | "
          f"{sum(found) / len(found) if found else float('nan'):.2f} (n {len(found)}) |")

print("\n## Haystack sweep at 16K: recall / echo per cell (n = 50), and check from the base\n")
cells = [c for c in CELLS if any(r.task == c for t in ran for r in sweep[t])]
print("| variant | " + " | ".join(c.removeprefix("hay_") for c in cells) + " | check c1 -> variant |")
print("|---|" + "---:|" * len(cells) + "---|")
S = {}
for t in ran:
    if not sweep[t]:
        continue
    by = {r.task: r for r in rows(sweep[t])}
    S[t] = {c: (by[c].contains_rate, by[c].stale_rate) for c in cells if c in by}
    fails = [f"{d.task}" for d in regressions(deltas(sweep["c1"], sweep[t])) if d.length_bucket] if sweep["c1"] and t != "c1" else []
    print(f"| {t} | " + " | ".join(f"{S[t][c][0]:.2f} / {S[t][c][1]:.2f}" if c in S[t] else "" for c in cells)
          + f" | {'FAIL ' + ', '.join(fails) if fails else 'pass' if t != 'c1' else ''} |")
for t in ("c1", "cm5"):
    found = defaultdict(list)
    for r in sweep[t]:
        if r.case_id in sweep_answers and "|" in sweep_answers[r.case_id]:
            found[r.task].append(items(r.output, sweep_answers[r.case_id]))
    if found:
        print(f"- {t} mean values found: " + ", ".join(f"{c} {sum(v) / len(v):.2f}" for c, v in sorted(found.items())))

print("\n## MATH-500 loops: 100 problems, thinking on, 16,384 new tokens\n")
print("| variant | | n | hit the limit | accuracy | mean tokens, finished | hit only in c1 / only here | p, two-sided |")
print("|---|---|---:|---:|---:|---:|---:|---:|")
H, P = {}, {}
for t in ran:
    m = loops[t]
    if not m:
        continue
    H[t] = sum(not d["finished"] for d in m.values()) / len(m)
    shared = [i for i in m if i in loops["c1"]]
    b = sum(not loops["c1"][i]["finished"] and m[i]["finished"] for i in shared)
    c = sum(loops["c1"][i]["finished"] and not m[i]["finished"] for i in shared)
    P[t] = two_sided(b, c)
    fin = [d["new_tokens"] for d in m.values() if d["finished"]]
    print(f"| {t} | {VARIANTS[t]} | {len(m)} | {H[t]:.2f} | {sum(d['correct'] for d in m.values()) / len(m):.2f} | "
          f"{sum(fin) / len(fin) if fin else 0:.0f} | {b} / {c} | {P[t]:.2g} |")

print("\n## Gate: exp08's six sets, base -> variant\n")
print("| variant | | recall, pooled | lost / gained | verdict |\n|---|---|---:|---:|---|")
G = {}
for t in ("cm5", *GATED):
    g = gate(t)
    if g:
        G[t] = not g[3]
        print(f"| {t} | {VARIANTS[t]} | {g[2]:.3f} | {g[0]} / {g[1]} | {'FAIL: ' + '; '.join(g[3]) if g[3] else 'pass'} |")

print("\n## Pre-registered readings\n")
if {"c1", "cm5"} <= H.keys() & E.keys():
    benefit_ok = H["c1"] - H["cm5"] >= 0.20 and P["cm5"] < 0.01
    damage_ok = E["cm5"] - E["c1"] >= 0.5
    print(f"- V2 benefit measurable: {benefit_ok} (hit rate {H['c1']:.2f} -> {H['cm5']:.2f}, p {P['cm5']:.2g}); "
          f"V3 damage measurable: {damage_ok} (echo {E['c1']:.2f} -> {E['cm5']:.2f})")
    if benefit_ok and damage_ok:
        beta = {t: (H["c1"] - H[t]) / (H["c1"] - H["cm5"]) for t in H if t in E and t not in ("c1", "cm5")}
        delta = {t: (E[t] - E["c1"]) / (E["cm5"] - E["c1"]) for t in beta}
        corner = [t for t in beta if beta[t] >= 0.75 and delta[t] <= 0.25]
        weights = [t for t in corner if G.get(t)]
        phase = [t for t in corner if t.endswith(("prompt", "answer"))]
        print("- benefit share / damage share: " + ", ".join(f"{t} {beta[t]:.2f} / {delta[t]:.2f}" for t in beta))
        verdict = ("separable by weights: " + ", ".join(weights) if weights else "separable by phase only: " + ", ".join(phase)
                   if phase else "one mechanism" if all(delta[t] >= beta[t] - 0.25 for t in beta) else "mixed")
        print(f"- **outcome: {verdict}**" + (f" (corner without a passed gate: {', '.join(set(corner) - set(weights) - set(phase))})"
                                              if set(corner) - set(weights) - set(phase) else ""))
if {"cm5-prompt", "cm5-answer"} <= E.keys():
    ep, ea = E["cm5-prompt"], E["cm5-answer"]
    print(f"- locus of the echo: {'reading' if ep >= 0.5 and ea <= 0.1 else 'answering' if ea >= 0.5 and ep <= 0.1 else 'both or neither'}"
          f" (echo {ep:.2f} while reading, {ea:.2f} while generating)")
if {"c1", "cm5"} <= S.keys():
    echo = {c.split("_")[1]: S["cm5"][c][1] for c in S["cm5"] if c.endswith("_k1")}
    anchor = echo.get("p5", 0) >= 0.8 and S["c1"].get("hay_p5_k1", (0, 1))[1] <= 0.1
    reading = ("exact period" if echo.get("p50", 0) >= 0.5 and echo.get("r50", 1) <= 0.1 else "repetition, no period needed"
               if echo.get("r50", 0) >= 0.5 else "a short period" if max(echo.get("p1", 0), echo.get("p5", 0)) >= 0.5
               and echo.get("p50", 1) <= 0.1 else "none of the three")
    print(f"- sweep anchor (p5 echoes like RULER's file): {anchor}; the echo needs: {reading} "
          f"({', '.join(f'{k} {v:.2f}' for k, v in echo.items())})")
    lists = [d.task for d in regressions(deltas(sweep["c1"], sweep["cm5"])) if d.task.startswith("hay_filler_k") and not d.task.endswith("k1")]
    print(f"- list tracking (filler k = 2 / 4 / 8): {'lost in ' + ', '.join(lists) if lists else 'no deficit'}")
if {"c1", "cm5"} <= MV.keys():
    print(f"- multi-value with 192 tokens: all four {MV['c1']:.2f} -> {MV['cm5']:.2f}; truncation reading "
          f"{'holds' if abs(MV['cm5'] - MV['c1']) <= 0.06 else 'fails'}")
print(f"\nvariants with files: {', '.join(ran) or 'none'}; case files: {len(ruler_answers)} unique RULER ids, {len(sweep_answers)} sweep ids")

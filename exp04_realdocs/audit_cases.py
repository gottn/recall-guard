"""Audit the exp04 cases; the numbers in RULER-PROVENANCE.md come from here.
Run: .venv/bin/python exp04_realdocs/audit_cases.py exp04_realdocs/results/cases
Per (task, length): n, rule, prompts ending in RULER's answer prefix, prompts containing a reference answer (the oracle: a
model that reads the gold paragraph can answer), ref_tokens range, documents per prompt; then whether every length asks
the same questions."""

import json
import sys
from collections import defaultdict
from pathlib import Path

cells = defaultdict(list)
for f in sorted(Path(sys.argv[1]).glob("ruler-*.jsonl")):
    for line in f.open():
        c = json.loads(line)
        cells[(c["task"], c["length_bucket"])].append(c)
print("| task | ref tokens | n | rule | ends with ' Answer:' | answer in prompt | ref_tokens min-max | docs/prompt |")
print("|---|---:|---:|---|---:|---:|---|---:|")
for (task, length), cs in sorted(cells.items()):
    prefix = sum(c["prompt"].endswith(" Answer:") for c in cs)
    oracle = sum(any(p.lower() in c["prompt"].lower() for p in c["answer"].split("|")) for c in cs)
    docs = sum(c["prompt"].count("\nDocument ") for c in cs) / len(cs)
    rules = ",".join(sorted({c["rule"] for c in cs}))
    print(f"| {task} | {length} | {len(cs)} | {rules} | {prefix} | {oracle} | {min(c['ref_tokens'] for c in cs)}-{max(c['ref_tokens'] for c in cs)} | {docs:.0f} |")
for task in sorted({t for t, _ in cells}):
    per_length = [[c["prompt"].rsplit("Question: ", 1)[1] for c in cells[k]] for k in sorted(cells) if k[0] == task]
    print(f"{task}: same questions at every length: {all(q == per_length[0] for q in per_length)}")

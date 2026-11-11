#!/usr/bin/env bash
# Experiment 12: does a rerun reproduce the stored answers? exp11's realmix seed 2 job again at 192 tokens, and at 64.
# Outcomes in RESULTS.md. No training and no code change: step1.sbatch runs `cli run` with JOB_ARGS on a linked suite.
# Cluster, from ~/projects/recall-guard (V / T = rerun192 / 192, cap64 / 64):
#   A=~/runs/rg/robust/20261101-183230-8b5abb6/adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix
#   D=~/runs/rg/rescore/20261108-rerun/$V; mkdir -p $D && ln -sf ~/data/rg/ruler-mvmq/ruler-mvmq.jsonl $D/suite.jsonl
#   RUN_IN=$D MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet JOB_ARGS="--max-new-tokens $T --adapter $A" infra/cluster/submit.sh step1 \
#     --partition=prioritized --qos=normal --gres=gpu:a40:1 --mem=32G --time=01:00:00
# Mac: rsync -a --exclude suite.jsonl --exclude 'slurm-*' --exclude '*.md' aau:runs/rg/rescore/20261108-rerun/ exp12_rerun_noise/results/raw/ && exp12_rerun_noise/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
case "${1:-report}" in
  report)
    $PY - <<'EOF'
import json, statistics as st
# Exact comparisons against exp11's realmix seed 2 run (192 tokens) and the stored exp05 run (64 tokens).
J, TASKS = "jet-ai_Jet-Nemotron-2B", ("ruler_niah_multivalue", "ruler_niah_multiquery")
load = lambda p: [json.loads(l) for l in open(p)]
ids = lambda rows: [(r["case_id"], r["task"], r["length_bucket"]) for r in rows]
exp11 = load(f"exp11_ruler_cap/results/raw/realmix-s2/{J}.jsonl")
stored = [r for L in (16384, 32768) for r in load(f"exp05_realmix/results/raw/damage/ruler-{L}-repair-seed2-realmix-{J}.jsonl")
          if r["task"] in TASKS]
rerun, cap = (load(f"exp12_rerun_noise/results/raw/{v}/{J}.jsonl") for v in ("rerun192", "cap64"))
assert ids(stored) == ids(rerun) == ids(cap) == ids(exp11), "case order differs"

def compare(name, a, b, prefix=False):
    same = [y["output"].startswith(x["output"].rstrip()) if prefix else x["output"] == y["output"] for x, y in zip(a, b)]
    at = [next((i for i, (p, q) in enumerate(zip(x["output"], y["output"])) if p != q), min(len(x["output"]), len(y["output"])))
          for x, y, s in zip(a, b, same) if not s]
    moved = sum(x["contains"] != y["contains"] for x, y in zip(a, b))
    print(f"{name}: {sum(same)} of 200 {'prefixes' if prefix else 'identical'}, {moved} verdicts differ"
          + (f", median divergence at char {st.median(at):.0f}" if at else ""))
    return sum(same)

r = compare("rerun192 vs exp11 (192)", rerun, exp11)
c = compare("cap64 vs stored (64)", cap, stored)
p = compare("cap64 as prefix of exp11 (192)", cap, exp11, prefix=True)
compare("stored (64) as prefix of exp11 (192)", stored, exp11, prefix=True)
print("outcome:", "noise" if r < 200 else "token limit" if c == 200 else "surroundings" if p == 200 else "mixed")

# Post-hoc (2026-11-11): where the diverging outputs sit, by length. cap64 against the stored run, then exp11's eleven runs
# against their stored ones by the prefix test (the base and synthetic seeds were stored on A100s, the other seven on A40s).
def by_length(a, b, prefix):
    return {L: sum(not (y["output"].startswith(x["output"].rstrip()) if prefix else x["output"] == y["output"])
                   for x, y in zip(a, b) if x["length_bucket"] == L) for L in (16384, 32768)}

print("diverging of 100 per length, cap64 vs stored:", by_length(stored, cap, False))
E3, E5 = "exp03_robust/results/raw", "exp05_realmix/results/raw/damage"
E6, E7 = "exp06_budget/results/raw/damage", "exp07_len32k/results/raw/damage"
OLD = {"base": f"{E3}/ruler-{{L}}-base-{J}.jsonl"} | {f"synthetic-s{s}": f"{E3}/ruler-{{L}}-repair-seed{s}-{J}.jsonl" for s in (1, 2, 3)}
OLD |= {f"realmix-s{s}": f"{E5}/ruler-{{L}}-repair-seed{s}-realmix-{J}.jsonl" for s in (1, 2, 3)}
OLD |= {f"budget-s{s}": f"{E6}/ruler-{{L}}-repair-seed{s}-budget-{J}.jsonl" for s in (1, 2, 3)}
OLD["syn1200"] = f"{E7}/ruler-{{L}}-repair-seed1-syn1200-{J}.jsonl"
for v, pat in OLD.items():
    old = [r for L in (16384, 32768) for r in load(pat.format(L=L)) if r["task"] in TASKS]
    print(f"diverging of 100 per length, {v} stored vs exp11:", by_length(old, load(f"exp11_ruler_cap/results/raw/{v}/{J}.jsonl"), True))
EOF
    ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

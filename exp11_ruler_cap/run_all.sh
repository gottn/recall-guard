#!/usr/bin/env bash
# Experiment 11: the stored 2B RULER multi-value / multi-query cases re-decoded with 192 new tokens instead of 64.
# Predictions in RESULTS.md. No training and no code change: step1.sbatch runs `cli run` with JOB_ARGS on a linked suite.
# Cluster, once (the two tasks from the exp03 RULER suites, lines kept byte for byte):
#   cd ~/data/rg && mkdir -p ruler-mvmq && for L in 16384 32768; do grep -E '"task": ?"ruler_niah_multi(value|query)"' ruler/ruler-$L.jsonl; done > ruler-mvmq/ruler-mvmq.jsonl
# Cluster, one run dir per variant (A = adapter dir, empty for the base; RS = ~/runs/rg/robust):
#   D=~/runs/rg/rescore/20261107-ruler192/$V; mkdir -p $D && ln -sf ~/data/rg/ruler-mvmq/ruler-mvmq.jsonl $D/suite.jsonl
#   RUN_IN=$D MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet JOB_ARGS="--max-new-tokens 192 ${A:+--adapter $A}" infra/cluster/submit.sh step1 \
#     --partition=prioritized --qos=normal --gres=gpu:a40:1 --mem=32G --time=02:00:00
#   V / A: base / -; synthetic-s{1,2,3} / RS/20261016-171229-9f67d4b/adapter-jet-ai_Jet-Nemotron-2B-seed{s};
#   realmix-s{s} / RS/20261101-183230-8b5abb6/adapter-...-seed{s}-realmix; budget-s{s} / RS/20261102-145806-8b5abb6/adapter-...-seed{s}-budget;
#   syn1200 / RS/20261106-103327-50ade98/adapter-...-seed1-syn1200
# Mac: rsync -a --exclude suite.jsonl --exclude 'slurm-*' aau:runs/rg/rescore/20261107-ruler192/ exp11_ruler_cap/results/raw/ && exp11_ruler_cap/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
OUT=exp11_ruler_cap/results
case "${1:-report}" in
  report)
    $PY -m recall_guard.cli report --results $OUT/raw/*/jet-ai_Jet-Nemotron-2B.jsonl --out $OUT/tables-192.md
    $PY - <<'EOF'
import json, re, statistics as st
# Readout against the stored 64-token outputs: verdict changes, prefix validity, seed means and the pre-registered gap.
J, OUT = "jet-ai_Jet-Nemotron-2B", "exp11_ruler_cap/results/raw"
OLD = {"base": "exp03_robust/results/raw/ruler-{L}-base-" + J + ".jsonl"}
OLD |= {f"synthetic-s{s}": f"exp03_robust/results/raw/ruler-{{L}}-repair-seed{s}-{J}.jsonl" for s in (1, 2, 3)}
OLD |= {f"realmix-s{s}": f"exp05_realmix/results/raw/damage/ruler-{{L}}-repair-seed{s}-realmix-{J}.jsonl" for s in (1, 2, 3)}
OLD |= {f"budget-s{s}": f"exp06_budget/results/raw/damage/ruler-{{L}}-repair-seed{s}-budget-{J}.jsonl" for s in (1, 2, 3)}
OLD["syn1200"] = f"exp07_len32k/results/raw/damage/ruler-{{L}}-repair-seed1-syn1200-{J}.jsonl"
TASKS = ("ruler_niah_multivalue", "ruler_niah_multiquery")
CUT = re.compile(r"^\s*(?:[\*\-]|\d+\.)?\s*\**\s*\d{0,6}\s*$")  # last line an unfinished list item
cut = lambda r: not r["contains"] and len(r["output"]) > 40 and bool(CUT.match(r["output"].rstrip("\n").split("\n")[-1]))
key = lambda r: (r["task"], r["length_bucket"])
score = {}
n_prefix = n_all = n_cut = n_cut_fixed = n_other_changed = 0
for v, pat in OLD.items():
    new = [json.loads(l) for l in open(f"{OUT}/{v}/{J}.jsonl")]
    old = [json.loads(l) for L in (16384, 32768) for l in open(pat.format(L=L)) if json.loads(l)["task"] in TASKS]
    assert [(r["case_id"], key(r)) for r in old] == [(r["case_id"], key(r)) for r in new], f"{v}: case order differs"
    for o, n in zip(old, new):
        n_all += 1; n_prefix += n["output"].startswith(o["output"].rstrip())
        if cut(o): n_cut += 1; n_cut_fixed += n["contains"]
        elif o["contains"] != n["contains"]: n_other_changed += 1
    for k in {key(r) for r in new}:
        score[v, k] = (sum(r["contains"] for r in old if key(r) == k) / 50, sum(r["contains"] for r in new if key(r) == k) / 50)
print(f"V: {n_prefix} of {n_all} new outputs begin with the stored one ({n_prefix / n_all:.0%}); "
      f"{n_other_changed} verdicts changed outside the cut-off misses")
print(f"P1: {n_cut_fixed} of {n_cut} cut-off misses become correct ({n_cut_fixed / max(n_cut, 1):.0%})")
for t in TASKS:
    for L in (16384, 32768):
        row = " | ".join(f"{v} {score[v, (t, L)][0]:.2f}->{score[v, (t, L)][1]:.2f}" for v in OLD)
        print(f"{t.split('_')[-1]} {L}: {row}")
for t in TASKS:
    arms = {a: [score[f"{a}-s{s}", (t, 16384)][1] for s in (1, 2, 3)] for a in ("synthetic", "realmix", "budget")}
    gap = {a: st.mean(arms["synthetic"]) - st.mean(arms[a]) for a in ("realmix", "budget")}
    sep = min(arms["synthetic"]) > max(arms["realmix"])
    print(f"{t.split('_')[-1]} 16K at 192: " + ", ".join(f"{a} {'/'.join(f'{x:.2f}' for x in xs)} (mean {st.mean(xs):.2f}, sd {st.stdev(xs):.2f})" for a, xs in arms.items())
          + f"; synthetic - realmix {gap['realmix']:+.2f}, synthetic - budget {gap['budget']:+.2f}, complete separation {sep}")
g = st.mean(score[f"synthetic-s{s}", ("ruler_niah_multivalue", 16384)][1] for s in (1, 2, 3)) - st.mean(score[f"realmix-s{s}", ("ruler_niah_multivalue", 16384)][1] for s in (1, 2, 3))
print("outcome (multi-value 16K gap):", "cost" if g >= 0.15 else "no cost" if g <= 0.08 else "small", f"({g:+.2f})")
EOF
    echo "wrote $OUT/tables-192.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

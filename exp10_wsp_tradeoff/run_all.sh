#!/usr/bin/env bash
# Experiment 10: is the weight edit's recall damage on repeated structure separable from its thinking-loop fix?
# Variants, measures, rules and odds in RESULTS.md, pre-registered before any run. No training; exp10.sbatch runs one
# variant per job on an A40 (4 h, 32G). Cluster, from the front end, in this order:
#   smokes, a run dir of their own (-> M):
#     TAG=smoke-cm5 SCALE=1 CASES=2 LIMIT=4 PER_LEVEL=1 MATH_TOKENS=256 infra/cluster/submit.sh exp10
#     RUN_IN=$M TAG=smoke-answer SCALE=1 PHASE=answer CASES=2 LIMIT=4 PER_LEVEL=1 MATH_TOKENS=256 infra/cluster/submit.sh exp10
#   the nine variants in one run dir (-> R), each after both smokes: D=--dependency=afterok:<smoke-cm5 id>:<smoke-answer id>
#     TAG=c1                                                            infra/cluster/submit.sh exp10 $D   (the base)
#     RUN_IN=$R TAG=c0 SCALE=0.16666667 GATE=1                          infra/cluster/submit.sh exp10 $D   (c = 1 - 6 SCALE = 0)
#     RUN_IN=$R TAG=cm1 SCALE=0.33333333 GATE=1                         infra/cluster/submit.sh exp10 $D   (c = -1)
#     RUN_IN=$R TAG=cm3 SCALE=0.66666667 GATE=1                         infra/cluster/submit.sh exp10 $D   (c = -3)
#     RUN_IN=$R TAG=cm5 SCALE=1                                         infra/cluster/submit.sh exp10 $D   (published)
#     RUN_IN=$R TAG=cm5-L15 SCALE=1 PATTERN=layers.15.mlp.down_proj.weight GATE=1 infra/cluster/submit.sh exp10 $D
#     RUN_IN=$R TAG=cm5-L19 SCALE=1 PATTERN=layers.19.mlp.down_proj.weight GATE=1 infra/cluster/submit.sh exp10 $D
#     RUN_IN=$R TAG=cm5-prompt SCALE=1 PHASE=prompt                     infra/cluster/submit.sh exp10 $D
#     RUN_IN=$R TAG=cm5-answer SCALE=1 PHASE=answer                     infra/cluster/submit.sh exp10 $D
# Mac: rsync -a --exclude 'slurm-*' --exclude sweep.jsonl "aau:$R/" exp10_wsp_tradeoff/results/raw/
#      scp "aau:$R/sweep.jsonl" "aau:data/rg/ruler/ruler-16384.jsonl" exp10_wsp_tradeoff/results/cases/   (git-ignored)
#      exp10_wsp_tradeoff/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
OUT=exp10_wsp_tradeoff/results; RAW=$OUT/raw
case "${1:-report}" in
  report)
    $PY -m recall_guard.cli report --results $RAW/niah-16384-*.jsonl --out $OUT/tables-niah.md
    $PY -m recall_guard.cli report --results $RAW/sweep-*.jsonl --out $OUT/tables-sweep.md
    $PY exp10_wsp_tradeoff/summary.py > $OUT/summary.md  # every number and every pre-registered reading
    shasum -a 256 $OUT/cases/*.jsonl 2>/dev/null || echo "no case files in $OUT/cases: item counts skipped"
    echo "wrote $OUT/tables-niah.md, tables-sweep.md and summary.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

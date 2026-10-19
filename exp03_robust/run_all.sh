#!/usr/bin/env bash
# Experiment 3: robustness of exp01/exp02 (docs/robustness.md on branch paper, items 1, 2, 5, 6, 7).
# Cluster:
#   STAGE=base MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust            -> RUN
#   RUN_IN=$RUN STAGE=base MODEL=Qwen/Qwen2.5-1.5B RG_ENV=modern infra/cluster/submit.sh robust
#   for s in 1 2 3; do RUN_IN=$RUN STAGE=repair TRAIN_SEED=$s MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust --time=08:00:00; done
#   for s in 1 2;   do RUN_IN=$RUN STAGE=repair TRAIN_SEED=$s MODEL=Qwen/Qwen2.5-1.5B RG_ENV=modern infra/cluster/submit.sh robust --time=08:00:00; done
# Mac:
#   rsync -a --exclude 'adapter-*' --exclude 'slurm-*' "aau:$RUN/" exp03_robust/results/raw/ && exp03_robust/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
case "${1:-report}" in
  report)
    # the two 50-case suites alone (n = 100 per cell, the paper's numbers); the 25-case held-out and multi-hop files go to their own table
    .venv/bin/python -m recall_guard.cli report --results exp03_robust/results/raw/suite-s*-*.jsonl --out exp03_robust/results/tables-suites.md
    .venv/bin/python -m recall_guard.cli report --results exp03_robust/results/raw/heldout-*.jsonl exp03_robust/results/raw/multihop25-*.jsonl --out exp03_robust/results/tables-extra.md
    .venv/bin/python -m recall_guard.cli report --results exp03_robust/results/raw/ruler-*.jsonl --out exp03_robust/results/tables-ruler.md
    echo "wrote exp03_robust/results/tables-suites.md, tables-extra.md and tables-ruler.md"
    for f in exp03_robust/results/raw/bench-*.json exp03_robust/results/raw/bpb-*.json; do [ -f "$f" ] && python3 -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"; done ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

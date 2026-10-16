#!/usr/bin/env bash
# Experiment 2: can LoRA on synthetic many-key documents repair a hybrid's long-context recall?
# Cluster (shared run dir; "base" jobs give the before numbers, "repair" jobs train and give the after numbers):
#   MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet STAGE=base infra/cluster/submit.sh exp02      -> prints RUN
#   RUN_IN=$RUN STAGE=repair MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet    infra/cluster/submit.sh exp02
#   RUN_IN=$RUN STAGE=base   MODEL=Qwen/Qwen2.5-1.5B      RG_ENV=modern infra/cluster/submit.sh exp02
#   RUN_IN=$RUN STAGE=repair MODEL=Qwen/Qwen2.5-1.5B      RG_ENV=modern infra/cluster/submit.sh exp02
# Mac:
#   rsync -a 'aau:$RUN/*.jsonl' 'aau:$RUN/*.json' exp02_repair/results/raw/ && exp02_repair/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
case "${1:-report}" in
  report)
    .venv/bin/python -m recall_guard.cli report \
      --results exp01_step1/results/raw/jet-ai_Jet-Nemotron-2B.jsonl exp01_step1/results/raw/Qwen_Qwen2.5-1.5B.jsonl \
                exp02_repair/results/raw/repaired-*.jsonl exp02_repair/results/raw/heldout-*.jsonl \
      --out exp02_repair/results/tables.md
    echo "wrote exp02_repair/results/tables.md"; cat exp02_repair/results/raw/bench-*.json ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

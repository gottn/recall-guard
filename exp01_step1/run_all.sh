#!/usr/bin/env bash
# Experiment 1: do the stressors separate hybrid from full attention where the needle test does not?
# Cluster (one job per model, same run directory so all share one suite):
#   RUN=~/runs/rg/step1/<ts>-<sha>                      (first submit creates it; reuse with RUN_IN)
#   MODEL=Qwen/Qwen3.5-4B      ENV=modern infra/cluster/submit.sh step1
#   RUN_IN=$RUN MODEL=Qwen/Qwen3-4B          ENV=modern infra/cluster/submit.sh step1
#   RUN_IN=$RUN MODEL=jet-ai/Jet-Nemotron-2B ENV=jet    infra/cluster/submit.sh step1
#   RUN_IN=$RUN MODEL=Qwen/Qwen2.5-1.5B      ENV=modern infra/cluster/submit.sh step1
# Mac (pull results, build the tables):
#   rsync -a aau:$RUN/*.jsonl exp01_step1/results/raw/ && exp01_step1/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
case "${1:-report}" in
  report)
    .venv/bin/python -m recall_guard.cli report --results exp01_step1/results/raw/*.jsonl \
      --pair Qwen/Qwen3.5-4B=Qwen/Qwen3-4B --pair jet-ai/Jet-Nemotron-2B=Qwen/Qwen2.5-1.5B \
      --out exp01_step1/results/tables.md
    echo "wrote exp01_step1/results/tables.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

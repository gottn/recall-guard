#!/usr/bin/env bash
# Experiment 4: recall on real documents. RULER qa_1 (SQuAD, one gold paragraph) and qa_2 (HotpotQA, two gold paragraphs)
# over real Wikipedia text at 4K/16K/32K, n = 100 per cell; predictions in RESULTS.md, data recipe in RULER-PROVENANCE.md.
# Mac, once: generate the cases (RULER-PROVENANCE.md), then rsync -a <qa dir>/ aau:~/data/rg/ruler-qa/
# Cluster, one job per model or adapter (E3 = the exp03 run dir holding the adapters):
#   E3=$HOME/runs/rg/robust/20261016-171229-9f67d4b
#   MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs                                                   -> RUN
#   RUN_IN=$RUN MODEL=Qwen/Qwen2.5-1.5B RG_ENV=modern infra/cluster/submit.sh realdocs
#   RUN_IN=$RUN ADAPTER=$E3/adapter-jet-ai_Jet-Nemotron-2B-seed1 MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs
#   RUN_IN=$RUN ADAPTER=$E3/adapter-Qwen_Qwen2.5-1.5B-seed1 MODEL=Qwen/Qwen2.5-1.5B RG_ENV=modern infra/cluster/submit.sh realdocs
#   RUN_IN=$RUN MODEL=meta-llama/Llama-3.1-8B-Instruct RG_ENV=modern infra/cluster/submit.sh realdocs
#   RUN_IN=$RUN MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh realdocs
#   RUN_IN=$RUN ADAPTER=$E3/adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh realdocs
#   RUN_IN=$RUN ADAPTER=$E3/adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh realdocs
# Mac: rsync -a --exclude 'slurm-*' "aau:$RUN/" exp04_realdocs/results/raw/ && exp04_realdocs/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
RAW=exp04_realdocs/results/raw
PY=.venv/bin/python
JET=jet-ai_Jet-Nemotron-2B; QWEN=Qwen_Qwen2.5-1.5B; MIL=JunxiongWang_Llama3.1-Mamba2-8B-dpo; LLAMA=meta-llama_Llama-3.1-8B-Instruct
case "${1:-report}" in
  report)
    $PY -m recall_guard.cli report --results $RAW/ruler-*.jsonl --out exp04_realdocs/results/tables.md
    # the gates, each over all lengths: source -> hybrid is the deficit, base -> repaired must not lose a cell
    : > exp04_realdocs/results/gates.md
    for pair in "base-$QWEN base-$JET" "base-$JET repair-seed1-$JET" "base-$QWEN repair-seed1-$QWEN" \
                "base-$LLAMA base-$MIL" "base-$MIL repair-seed1-gentle-$MIL" "base-$MIL repair-seed1-qk-$MIL"; do
      set -- $pair
      ls $RAW/ruler-*-"$1".jsonl $RAW/ruler-*-"$2".jsonl >/dev/null 2>&1 || continue
      { echo "### $1 -> $2"; $PY -m recall_guard.cli check --baseline $RAW/ruler-*-"$1".jsonl --candidate $RAW/ruler-*-"$2".jsonl || true; echo; } >> exp04_realdocs/results/gates.md
    done
    echo "wrote exp04_realdocs/results/tables.md and gates.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

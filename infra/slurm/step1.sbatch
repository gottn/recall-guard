#!/usr/bin/env bash
# Experiment 1: one model, the full suite (5 tasks x 6 lengths x 25 cases), one A100.
# Submit only via infra/cluster/submit.sh:   MODEL=Qwen/Qwen3.5-4B RG_ENV=modern infra/cluster/submit.sh step1
# The suite is regenerated deterministically from (commit, seed, Qwen2.5 tokenizer) so every model sees the same prompts.
#SBATCH --partition=aicentre-a100
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=06:00:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
: "${MODEL:?set MODEL=<hf id>}"
TRC=""; case "$MODEL" in jet-ai/*) TRC="--trust-remote-code";; esac
SLUG="$(echo "$MODEL" | tr / _)"
echo "commit $RG_SHA on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, model=$MODEL, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  source infra/cluster/env.sh
  [ -f $RG_OUT/suite.jsonl ] || \$PY -m recall_guard.cli generate --out $RG_OUT/suite.jsonl --seed 0 --cases 25
  \$PY -m recall_guard.cli run --suite $RG_OUT/suite.jsonl --model $MODEL $TRC --out $RG_OUT/$SLUG.jsonl $JOB_ARGS
  \$PY -m recall_guard.cli report --results $RG_OUT/$SLUG.jsonl --out $RG_OUT/$SLUG.md
"
echo "step1 done: $MODEL"

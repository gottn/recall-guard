#!/usr/bin/env bash
# Experiment 2: recall repair. One model per job, one A100.
#   STAGE=base   : held-out suite + ARC/HellaSwag on the base model (the "before" numbers)
#   STAGE=repair : LoRA train on synthetic many-key docs, then step1 suite + held-out suite + bench with the adapter
# Submit only via infra/cluster/submit.sh, e.g.
#   RUN_IN=$RUN STAGE=base   MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet    infra/cluster/submit.sh exp02
#   RUN_IN=$RUN STAGE=repair MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet    infra/cluster/submit.sh exp02
# SUITE defaults to the step1 suite so "after" numbers are comparable to exp01.
#SBATCH --partition=aicentre-a100
#SBATCH --qos=unprivileged
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=05:00:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1 HF_DATASETS_OFFLINE=0
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
: "${MODEL:?set MODEL=<hf id>}"; STAGE="${STAGE:-base}"
SUITE="${SUITE:-$HOME/runs/rg/step1/20261016-121320-8beb29d/suite.jsonl}"
TRC=""; case "$MODEL" in jet-ai/*) TRC="--trust-remote-code";; esac
SLUG="$(echo "$MODEL" | tr / _)"
echo "commit $RG_SHA on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, model=$MODEL, stage=$STAGE, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  source infra/cluster/env.sh
  [ -f $RG_OUT/heldout.jsonl ] || \$PY -m recall_guard.cli generate --out $RG_OUT/heldout.jsonl --seed 1 --cases 25 --tasks heldout_many
  if [ $STAGE = base ]; then
    \$PY -m recall_guard.cli run --suite $RG_OUT/heldout.jsonl --model $MODEL $TRC --out $RG_OUT/heldout-$SLUG.jsonl
    \$PY -m recall_guard.cli bench --model $MODEL $TRC --n 500 --out $RG_OUT/bench-$SLUG.json
  else
    A=$RG_OUT/adapter-$SLUG
    [ -f \$A/adapter_config.json ] || \$PY -m recall_guard.cli train --model $MODEL $TRC --out \$A $JOB_ARGS
    \$PY -m recall_guard.cli run --suite $SUITE --model $MODEL $TRC --adapter \$A --out $RG_OUT/repaired-$SLUG.jsonl
    \$PY -m recall_guard.cli run --suite $RG_OUT/heldout.jsonl --model $MODEL $TRC --adapter \$A --out $RG_OUT/heldout-repaired-$SLUG.jsonl
    \$PY -m recall_guard.cli bench --model $MODEL $TRC --adapter \$A --n 500 --out $RG_OUT/bench-repaired-$SLUG.json
  fi
"
echo "exp02 $STAGE done: $MODEL"

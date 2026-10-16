#!/usr/bin/env bash
# exp02 smoke: proves LoRA training runs on the model (module names, memory at 16K, tok/s) in 3 optimizer steps,
# then 2 completions with the adapter and a 20-item bench. Submit via submit.sh:  MODEL=... RG_ENV=... infra/cluster/submit.sh exp02_smoke
#SBATCH --partition=aicentre-a100
#SBATCH --qos=unprivileged
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=00:40:00
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
  \$PY -m recall_guard.cli train --model $MODEL $TRC --out $RG_OUT/adapter-$SLUG --n-docs 12 --lengths 16384 --grad-accum 4 --max-steps 3
  \$PY -m recall_guard.cli generate --out $RG_OUT/mini.jsonl --cases 1 --lengths 4096 --tasks needle heldout_many
  \$PY -m recall_guard.cli run --suite $RG_OUT/mini.jsonl --model $MODEL $TRC --adapter $RG_OUT/adapter-$SLUG --out $RG_OUT/mini-$SLUG.jsonl
  \$PY -m recall_guard.cli bench --model $MODEL $TRC --adapter $RG_OUT/adapter-$SLUG --n 20 --out $RG_OUT/bench-mini-$SLUG.json
"
echo "exp02 smoke done: $MODEL"

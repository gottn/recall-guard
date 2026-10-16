#!/usr/bin/env bash
# Smoke for a converted 8B hybrid loaded through backends/loaders.py: builds the env, a 2-case suite at 4K (needle +
# held-out parcels), one run, the report. Submit via submit.sh (defaults: MODEL=Mamba-in-the-Llama 8B, RG_ENV=mil):
#   RG_ENV=mil infra/cluster/submit.sh mil_smoke          MODEL=hazyresearch/lolcats-llama-3.1-8b-ft-lora RG_ENV=mil ...
#SBATCH --partition=aicentre-a100
#SBATCH --qos=unprivileged
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=01:00:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1 RG_ENV=mil
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
MODEL="${MODEL:-JunxiongWang/Llama3.1-Mamba2-8B-dpo}"
SLUG="$(echo "$MODEL" | tr / _)"
echo "commit $RG_SHA (checkout now $(git -C "$RG_ROOT" rev-parse --short HEAD)) on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, model=$MODEL, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  T0=\$SECONDS
  source infra/cluster/env.sh
  \$PY -c 'import sys, triton, einops; print(\"triton\", triton.__version__, \"python\", sys.version.split()[0])'
  echo \"env ready in \$((SECONDS - T0))s\"
  \$PY -m recall_guard.cli generate --out $RG_OUT/mini.jsonl --cases 1 --lengths 4096 --tasks needle heldout_many
  \$PY -m recall_guard.cli run --suite $RG_OUT/mini.jsonl --model $MODEL --out $RG_OUT/mini-$SLUG.jsonl
  cat $RG_OUT/mini-$SLUG.jsonl
  \$PY -m recall_guard.cli report --results $RG_OUT/mini-$SLUG.jsonl
  echo \"wall \$((SECONDS - T0))s\"
"
echo "mil smoke done: $MODEL"

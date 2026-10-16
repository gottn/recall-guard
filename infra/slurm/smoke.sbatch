#!/usr/bin/env bash
# Smoke test: one GPU, 30 minutes. Proves container + venv + cached model + the generate/run/report pipeline.
# Submit only via infra/cluster/submit.sh smoke   (RG_ENV=jet MODEL=jet-ai/Jet-Nemotron-2B to prove the jet env).
#SBATCH --partition=prioritized
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=00:30:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
MODEL="${MODEL:-Qwen/Qwen2.5-1.5B}"
TRC=""; case "$MODEL" in jet-ai/*) TRC="--trust-remote-code";; esac
echo "commit $RG_SHA on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, model=$MODEL, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  source infra/cluster/env.sh
  \$PY -m recall_guard.cli generate --out $RG_OUT/suite-smoke.jsonl --cases 2 --lengths 1024 4096
  \$PY -m recall_guard.cli run --suite $RG_OUT/suite-smoke.jsonl --model $MODEL $TRC --out $RG_OUT/smoke-\$(echo $MODEL | tr / _).jsonl
  \$PY -m recall_guard.cli report --results $RG_OUT/smoke-*.jsonl
"
echo "smoke done"

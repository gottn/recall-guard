#!/usr/bin/env bash
# Experiment 4 (real documents): RULER QA over real Wikipedia paragraphs, qa_1 (SQuAD, one gold document) and qa_2
# (HotpotQA, two gold documents) at 4K/16K/32K, n = 100 per cell. One model per job, no training: adapters come from
# the exp03 run dir. Submit only via infra/cluster/submit.sh:
#   MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs                                  -> RUN (base)
#   RUN_IN=$RUN ADAPTER=$HOME/runs/rg/robust/<run>/adapter-jet-ai_Jet-Nemotron-2B-seed1 MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs
# QA cases come from ~/data/rg/ruler-qa (generated on the Mac with NVIDIA's qa.py, converted by recall_guard.cli import-ruler;
# exp04_realdocs/RULER-PROVENANCE.md). Default partition: A40 (Mamba-in-the-Llama peaks at 21 GiB at 32K).
#SBATCH --partition=prioritized
#SBATCH --qos=normal
#SBATCH --gres=gpu:a40:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=08:00:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
: "${MODEL:?set MODEL=<hf id>}"
QA_DIR="${QA_DIR:-$HOME/data/rg/ruler-qa}"
ADAPTER="${ADAPTER:-}"
TRC=""; case "$MODEL" in jet-ai/*) TRC="--trust-remote-code";; esac
SLUG="$(echo "$MODEL" | tr / _)"
if [ -n "$ADAPTER" ]; then
  [ -f "$ADAPTER/adapter_config.json" ] || { echo "no adapter at $ADAPTER"; exit 1; }
  B="$(basename "$ADAPTER")"; TAG="repair-${B#adapter-$SLUG-}"; ADP="--adapter $ADAPTER"   # adapter-<slug>-seed1-gentle -> repair-seed1-gentle
else
  TAG=base; ADP=""
fi
ls "$QA_DIR"/*.jsonl >/dev/null
echo "commit $RG_SHA on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, model=$MODEL, tag=$TAG, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  source infra/cluster/env.sh
  for R in $QA_DIR/*.jsonl; do \$PY -m recall_guard.cli run --suite \$R --model $MODEL $TRC $ADP --max-new-tokens 32 --out $RG_OUT/\$(basename \$R .jsonl)-$TAG-$SLUG.jsonl; done
"
echo "realdocs done: $MODEL $TAG"

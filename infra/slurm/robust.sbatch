#!/usr/bin/env bash
# Experiment 3 (robustness): one model per job, one A100.
#   STAGE=base   : our suites (seed 1, seed 2; n=50 at 16K/32K) + RULER suites + held-out + bench + long-text bpb, no adapter
#   STAGE=repair : train v2 mix (random/similar/updated/multihop) with TRAIN_SEED, then the same evaluations with the adapter,
#                  plus the alternative-explanation checks on suite seed 1 at 32K (unmerged adapter; chat template)
# Submit only via infra/cluster/submit.sh:
#   STAGE=base   MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust              -> RUN
#   RUN_IN=$RUN STAGE=repair TRAIN_SEED=1 MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust --time=08:00:00
#   TRAIN_LENGTHS="8192 16384" TRAIN_TAG=-le16k ... trains below 32K to test length generalisation (item 3)
# RULER suites come from ~/data/rg/ruler (generated on the Mac with NVIDIA's generator, converted by recall_guard.ruler).
#SBATCH --partition=aicentre-a100
#SBATCH --qos=unprivileged
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=05:00:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
: "${MODEL:?set MODEL=<hf id>}"; STAGE="${STAGE:-base}"; TRAIN_SEED="${TRAIN_SEED:-1}"; TRAIN_LENGTHS="${TRAIN_LENGTHS:-8192 16384 32768}"
RULER_DIR="${RULER_DIR:-$HOME/data/rg/ruler}"
TEXT="${TEXT:-$HOME/data/rg/mobydick.txt}"
TRC=""; case "$MODEL" in jet-ai/*) TRC="--trust-remote-code";; esac
SLUG="$(echo "$MODEL" | tr / _)"
[ -f "$TEXT" ] || curl -sL -o "$TEXT" https://www.gutenberg.org/cache/epub/2701/pg2701.txt
echo "commit $RG_SHA on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, model=$MODEL, stage=$STAGE, seed=$TRAIN_SEED, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  source infra/cluster/env.sh
  for s in 1 2; do [ -f $RG_OUT/suite-s\$s.jsonl ] || \$PY -m recall_guard.cli generate --out $RG_OUT/suite-s\$s.jsonl --seed \$s --cases 50 --lengths 16384 32768; done
  [ -f $RG_OUT/heldout.jsonl ] || \$PY -m recall_guard.cli generate --out $RG_OUT/heldout.jsonl --seed 1 --cases 25 --tasks heldout_many
  [ -f $RG_OUT/multihop25.jsonl ] || \$PY -m recall_guard.cli generate --out $RG_OUT/multihop25.jsonl --seed 0 --cases 25 --tasks multihop
  if [ $STAGE = base ]; then TAG=base; ADP=''; else
    A=$RG_OUT/adapter-$SLUG-seed$TRAIN_SEED${TRAIN_TAG:-}; TAG=repair-seed$TRAIN_SEED${TRAIN_TAG:-}; ADP=\"--adapter \$A\"
    [ -f \$A/adapter_config.json ] || \$PY -m recall_guard.cli train --model $MODEL $TRC --out \$A --seed $TRAIN_SEED --n-docs 600 --lengths $TRAIN_LENGTHS
  fi
  for S in suite-s1 suite-s2 heldout multihop25; do \$PY -m recall_guard.cli run --suite $RG_OUT/\$S.jsonl --model $MODEL $TRC \$ADP --out $RG_OUT/\$S-\$TAG-$SLUG.jsonl; done
  for R in $RULER_DIR/*.jsonl; do \$PY -m recall_guard.cli run --suite \$R --model $MODEL $TRC \$ADP --max-new-tokens 64 --out $RG_OUT/\$(basename \$R .jsonl)-\$TAG-$SLUG.jsonl; done
  \$PY -m recall_guard.cli bench --model $MODEL $TRC \$ADP --n 500 --out $RG_OUT/bench-\$TAG-$SLUG.json
  \$PY -m recall_guard.cli ppl --model $MODEL $TRC \$ADP --text $TEXT --window-tokens 16384 --windows 8 --out $RG_OUT/bpb-\$TAG-$SLUG.json
  if [ $STAGE = repair ]; then
    \$PY -m recall_guard.cli run --suite $RG_OUT/suite-s1.jsonl --lengths 32768 --model $MODEL $TRC \$ADP --adapter-mode attach --out $RG_OUT/suite-s1-\$TAG-unmerged-$SLUG.jsonl
    \$PY -m recall_guard.cli run --suite $RG_OUT/suite-s1.jsonl --lengths 32768 --model $MODEL $TRC \$ADP --chat --out $RG_OUT/suite-s1-\$TAG-chat-$SLUG.jsonl
  fi
"
echo "robust $STAGE done: $MODEL seed=$TRAIN_SEED"

#!/usr/bin/env bash
# Experiment 10 (exp10_wsp_tradeoff/RESULTS.md): is the weight edit's recall damage on repeated structure separable
# from its thinking-loop fix? One variant of Qwen/Qwen3.5-0.8B per job, no training. A variant moves the tensors that
# match PATTERN (down_proj of layers 15 and 19) to W + SCALE * (W_edit - W): in place, or only while reading the prompt,
# or only while generating (PHASE=prompt / answer). Without SCALE the job runs the unedited base. Every job runs RULER's
# single needle and multi-value at 16K with 192 new tokens, the haystack sweep (generated into the run dir) and MATH-500
# loops; GATE=1 adds exp08's six gate sets (suites from exp08's run dir, the exp01 suite, real QA).
# Submit only via infra/cluster/submit.sh (all nine variants and the smoke: exp10_wsp_tradeoff/run_all.sh):
#   TAG=c0 SCALE=0.16666667 GATE=1 infra/cluster/submit.sh exp10                      -> RUN
#   RUN_IN=$RUN TAG=cm5-answer SCALE=1 PHASE=answer infra/cluster/submit.sh exp10
# Smoke: CASES=2 LIMIT=4 PER_LEVEL=1 MATH_TOKENS=256, in a run dir of its own.
#SBATCH --partition=prioritized
#SBATCH --qos=normal
#SBATCH --gres=gpu:a40:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00
set -euo pipefail
export HF_HOME="$HOME/hf_cache" PYTHONUNBUFFERED=1
CONTAINER="${CONTAINER:-/home/container/pytorch/pytorch_25.09.sif}"
: "${TAG:?set TAG=<variant name>}"
MODEL="${MODEL:-Qwen/Qwen3.5-0.8B}"; EDIT="${EDIT:-RikiyaT/Qwen3.5-0.8B-weight-space-programming}"
PATTERN="${PATTERN:-layers.1[59].mlp.down_proj.weight}"; PHASE="${PHASE:-all}"; GATE="${GATE:-0}"
X8="${X8:-$HOME/runs/rg/robust/20261106-105622-26d25e8}"  # exp08's run dir: suite-s1, suite-s2, heldout, multihop25
STEP1="${STEP1:-$HOME/runs/rg/step1/20261016-121320-8beb29d/suite.jsonl}"
RULER="${RULER:-$HOME/data/rg/ruler/ruler-16384.jsonl}"; QA_DIR="${QA_DIR:-$HOME/data/rg/ruler-qa}"
CASES="${CASES:-50}"; LIMIT="${LIMIT:-0}"; PER_LEVEL="${PER_LEVEL:-20}"; MATH_TOKENS="${MATH_TOKENS:-16384}"
EDIT_ARGS=""  # the pattern is quoted for the inner shell, which would otherwise glob its brackets
[ -n "${SCALE:-}" ] && EDIT_ARGS="--restore-from $EDIT --restore-pattern '$PATTERN' --restore-scale $SCALE --restore-phase $PHASE"
RUN="\$PY -m recall_guard.cli run --model $MODEL $EDIT_ARGS --limit $LIMIT"
echo "commit $RG_SHA on $(hostname), gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader | head -1), env=$RG_ENV, tag=$TAG, edit=${EDIT_ARGS:-none}, gate=$GATE, out=$RG_OUT"
srun singularity exec --nv "$CONTAINER" bash -c "
  set -euo pipefail
  cd $RG_ROOT
  source infra/cluster/env.sh
  [ -f $RG_OUT/sweep.jsonl ] || \$PY -m recall_guard.cli generate --out $RG_OUT/sweep.jsonl --seed 10 --cases $CASES --lengths 16384 --cells p1:1 p5:1 p50:1 r50:1 filler:1 filler:2 filler:4 filler:8
  $RUN --suite $RULER --tasks ruler_niah_single_1 ruler_niah_multivalue --max-new-tokens 192 --out $RG_OUT/niah-16384-$TAG.jsonl
  $RUN --suite $RG_OUT/sweep.jsonl --max-new-tokens 192 --out $RG_OUT/sweep-$TAG.jsonl
  \$PY -m recall_guard.cli loops --model $MODEL $EDIT_ARGS --per-level $PER_LEVEL --max-new-tokens $MATH_TOKENS --out $RG_OUT/loops-$TAG.jsonl
  if [ $GATE = 1 ]; then
    for S in suite-s1 suite-s2 heldout multihop25; do $RUN --suite $X8/\$S.jsonl --out $RG_OUT/\$S-$TAG.jsonl; done
    $RUN --suite $STEP1 --out $RG_OUT/step1-$TAG.jsonl
    for Q in $QA_DIR/*.jsonl; do $RUN --suite \$Q --out $RG_OUT/qa-\$(basename \$Q .jsonl)-$TAG.jsonl; done
  fi
"
echo "exp10 done: $TAG"

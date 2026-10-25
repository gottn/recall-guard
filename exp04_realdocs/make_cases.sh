#!/usr/bin/env bash
# Generate the exp04 cases with NVIDIA's RULER QA generator and import them as Cases. Run on the Mac:
#   exp04_realdocs/make_cases.sh <RULER clone> <out dir>        e.g. make_cases.sh /tmp/RULER ~/data/rg/ruler-qa
# Needs <clone>/scripts/data/synthetic/json/{squad,hotpotqa}.json (their download_qa_dataset.sh) and the repo .venv
# (transformers for the Qwen2.5-1.5B tokenizer). Sizes every prompt so that prompt + 32 new tokens fit the length.
set -euo pipefail
RULER="${1:?RULER clone}"; OUT="${2:?out dir}"
cd "$(dirname "$0")/.."
PY="$(pwd)/.venv/bin/python"
TEMPLATE='Answer the question based on the given documents. Only give me the answer and do not output any other words.\n\nThe following are given documents.\n\n{context}\n\nAnswer the question based on the given documents. Only give me the answer and do not output any other words.\n\nQuestion: {query} Answer:'
GEN="$OUT/generated"
for L in 4096 16384 32768; do
  for T in qa_1:squad qa_2:hotpotqa; do
    [ -f "$GEN/$L/${T%%:*}/validation.jsonl" ] && continue
    (cd "$RULER/scripts/data/synthetic" && "$PY" qa.py --save_dir "$GEN/$L" --save_name "${T%%:*}" --dataset "${T##*:}" \
       --tokenizer_path Qwen/Qwen2.5-1.5B --tokenizer_type hf --max_seq_length "$L" --tokens_to_generate 32 \
       --num_samples 100 --random_seed 42 --template "$TEMPLATE")
  done
done
"$PY" -m recall_guard.cli import-ruler --dir "$GEN" --out-dir "$OUT"

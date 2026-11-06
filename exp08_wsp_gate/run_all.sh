#!/usr/bin/env bash
# Experiment 8: does the training-free weight edit of "Sparks of Weight-Space Programming" change long-context recall?
# Gate rule and prediction in RESULTS.md. No training: both checkpoints run as base models (STAGE=base, no adapter).
# Cluster (A40="--partition=prioritized --qos=normal --gres=gpu:a40:1"; W=RikiyaT/Qwen3.5-0.8B-weight-space-programming):
#   STAGE=base MODEL=Qwen/Qwen3.5-0.8B RG_ENV=modern infra/cluster/submit.sh robust $A40 --mem=32G --time=04:00:00   -> R
#   RUN_IN=$R STAGE=base MODEL=$W RG_ENV=modern infra/cluster/submit.sh robust $A40 --mem=32G --time=04:00:00
#   MODEL=Qwen/Qwen3.5-0.8B RG_ENV=modern infra/cluster/submit.sh realdocs $A40 --mem=32G --time=02:00:00   -> Q
#   RUN_IN=$Q MODEL=$W RG_ENV=modern infra/cluster/submit.sh realdocs $A40 --mem=32G --time=02:00:00
#   S=$HOME/runs/rg/step1/20261016-121320-8beb29d (the exp01 suite); for M in Qwen/Qwen3.5-0.8B $W:
#     RUN_IN=$S MODEL=$M RG_ENV=modern infra/cluster/submit.sh step1 $A40 --mem=32G --time=02:00:00
# Mac: rsync -a --exclude 'slurm-*' --exclude 'suite-s?.jsonl' --exclude heldout.jsonl --exclude multihop25.jsonl "aau:$R/" exp08_wsp_gate/results/raw/robust/
#      rsync -a --exclude 'slurm-*' "aau:$Q/" exp08_wsp_gate/results/raw/qa/
#      rsync -a "aau:$S/Qwen_Qwen3.5-0.8B.jsonl" "aau:$S/RikiyaT_Qwen3.5-0.8B-weight-space-programming.jsonl" exp08_wsp_gate/results/raw/step1/
#      exp08_wsp_gate/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
OUT=exp08_wsp_gate/results; RB=$OUT/raw/robust; QA=$OUT/raw/qa; S1=$OUT/raw/step1
BASE=Qwen_Qwen3.5-0.8B; EDIT=RikiyaT_Qwen3.5-0.8B-weight-space-programming
gate() {  # gate <heading> <baseline files...> -- <candidate files...>: one check, appended to gates.md, never fatal
  local title="$1"; shift; local base=() cand=()
  while [ "$1" != "--" ]; do base+=("$1"); shift; done; shift; cand=("$@")
  ls "${base[@]}" "${cand[@]}" >/dev/null 2>&1 || { echo "skip $title (missing files)"; return; }
  { echo "### $title"; $PY -m recall_guard.cli check --baseline "${base[@]}" --candidate "${cand[@]}" || true; echo; } >> $OUT/gates.md
}
case "${1:-report}" in
  report)
    # one table per suite family: step1, the s1/s2 suites and multihop25 share task names at 16K/32K and would pool
    $PY -m recall_guard.cli report --results $RB/suite-s*-base-*.jsonl $RB/heldout-base-*.jsonl --out $OUT/tables-suites.md
    $PY -m recall_guard.cli report --results $RB/multihop25-base-*.jsonl --out $OUT/tables-multihop25.md
    $PY -m recall_guard.cli report --results $RB/ruler-*-base-*.jsonl --out $OUT/tables-ruler.md
    $PY -m recall_guard.cli report --results $QA/ruler-*-base-*.jsonl --out $OUT/tables-qa.md
    $PY -m recall_guard.cli report --results $S1/*.jsonl --out $OUT/tables-step1.md
    : > $OUT/gates.md
    for F in suite-s1 suite-s2 heldout multihop25; do  # one gate per file: s1/s2 reuse case ids, heldout/multihop25 share their 16K/32K ids with the suites
      gate "$F: base -> edited" $RB/$F-base-$BASE.jsonl -- $RB/$F-base-$EDIT.jsonl
    done
    gate "step1: base -> edited" $S1/$BASE.jsonl -- $S1/$EDIT.jsonl
    gate "real QA: base -> edited" $QA/ruler-*-base-$BASE.jsonl -- $QA/ruler-*-base-$EDIT.jsonl
    for F in suite-s1 suite-s2 heldout multihop25; do
      gate "$F: edited -> base, FAIL cells are edited gains" $RB/$F-base-$EDIT.jsonl -- $RB/$F-base-$BASE.jsonl
    done
    gate "step1: edited -> base, FAIL cells are edited gains" $S1/$EDIT.jsonl -- $S1/$BASE.jsonl
    gate "real QA: edited -> base, FAIL cells are edited gains" $QA/ruler-*-base-$EDIT.jsonl -- $QA/ruler-*-base-$BASE.jsonl
    # no RULER gate: the generator repeats 10 (16K) and 4 (32K) case ids per file and check refuses them; read tables-ruler.md
    $PY - $RB/*-base-$BASE.jsonl $QA/*-base-$BASE.jsonl $S1/$BASE.jsonl <<'EOF'
import json, sys  # validity: the edit must reach the forward pass, so some completions must differ from the base's
from collections import Counter  # (case id, output) multisets: RULER files repeat case ids
same = total = 0
for f in sys.argv[1:]:
    b, e = (Counter((r["case_id"], r["output"]) for r in map(json.loads, open(p)))
            for p in (f, f.replace("Qwen_Qwen3.5-0.8B", "RikiyaT_Qwen3.5-0.8B-weight-space-programming")))
    same += sum((b & e).values())
    total += sum(b.values())
print(f"identical completions, base vs edited: {same} of {total}")
EOF
    for f in $RB/bench-base-{$BASE,$EDIT}.json $RB/bpb-base-{$BASE,$EDIT}.json; do
      [ -f "$f" ] && $PY -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"
    done
    echo "wrote $OUT/tables-suites.md, tables-multihop25.md, tables-ruler.md, tables-qa.md, tables-step1.md and gates.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

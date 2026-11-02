#!/usr/bin/env bash
# Experiment 6: the full synthetic dose plus the real half. Outcomes in RESULTS.md; exp05_realmix/run_all.sh with both halves doubled.
# Cluster, training + the exp03 damage checks (robust.sbatch STAGE=repair; the adapter lands in the run dir R):
#   D="--real-dir $HOME/data/rg/realqa --exclude-dir $HOME/data/rg/ruler-qa"; A40="--partition=prioritized --qos=normal --gres=gpu:a40:1"
#   STAGE=repair TRAIN_SEED=1 TRAIN_TAG=-budget TRAIN_DOCS=1200 TRAIN_EXTRA="$D" MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust $A40 --mem=32G --time=12:00:00   -> R
#   RUN_IN=$R STAGE=repair TRAIN_SEED=1 TRAIN_TAG=-budget TRAIN_DOCS=600 TRAIN_LENGTHS="8192 16384" TRAIN_EXTRA="--lr 5e-5 $D" \
#     MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh robust $A40 --mem=56G --time=12:00:00
# Cluster, the exp04 real-QA cases with the new adapters (after the training jobs: --dependency=afterany:<job id>):
#   ADAPTER=$R/adapter-jet-ai_Jet-Nemotron-2B-seed1-budget MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs --mem=32G --time=04:00:00   -> Q
#   RUN_IN=$Q ADAPTER=$R/adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh realdocs --mem=48G --time=06:00:00
# Mac: rsync -a --exclude 'adapter-*' --exclude 'slurm-*' "aau:$R/" exp06_budget/results/raw/damage/
#      rsync -a --exclude 'slurm-*' "aau:$Q/" exp06_budget/results/raw/qa/ && exp06_budget/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
OUT=exp06_budget/results; QA=$OUT/raw/qa; DMG=$OUT/raw/damage
E5Q=exp05_realmix/results/raw/qa; E5D=exp05_realmix/results/raw/damage; E4=exp04_realdocs/results/raw; E3=exp03_robust/results/raw
JET=jet-ai_Jet-Nemotron-2B; MIL=JunxiongWang_Llama3.1-Mamba2-8B-dpo
B=repair-seed1-budget; R=repair-seed1-realmix
gate() {  # gate <heading> <baseline files...> -- <candidate files...>: one check, appended to gates.md, never fatal
  local title="$1"; shift; local base=() cand=()
  while [ "$1" != "--" ]; do base+=("$1"); shift; done; shift; cand=("$@")
  ls "${base[@]}" "${cand[@]}" >/dev/null 2>&1 || { echo "skip $title (missing files)"; return; }
  { echo "### $title"; $PY -m recall_guard.cli check --baseline "${base[@]}" --candidate "${cand[@]}" || true; echo; } >> $OUT/gates.md
}
case "${1:-report}" in
  report)
    $PY -m recall_guard.cli report --results $E4/ruler-*-base-*.jsonl $E4/ruler-*-repair-seed1-$JET.jsonl $E4/ruler-*-repair-seed1-gentle-$MIL.jsonl \
      $E5Q/ruler-*-$R-*.jsonl $QA/ruler-*.jsonl --out $OUT/tables-qa.md
    ls $DMG/suite-s*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/suite-s*-base-{$JET,$MIL}.jsonl $E3/suite-s*-repair-seed[123]-$JET.jsonl $E3/suite-s*-repair-seed1-gentle-$MIL.jsonl \
        $E5D/suite-s*-$R-{$JET,$MIL}.jsonl $DMG/suite-s*-$B-*.jsonl --out $OUT/tables-damage.md
    ls $DMG/multihop25-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/multihop25-base-{$JET,$MIL}.jsonl $E3/multihop25-repair-seed[123]-$JET.jsonl $E3/multihop25-repair-seed1-gentle-$MIL.jsonl \
        $E5D/multihop25-$R-*.jsonl $DMG/multihop25-$B-*.jsonl --out $OUT/tables-multihop25.md
    ls $DMG/ruler-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/ruler-*-base-{$JET,$MIL}.jsonl $E3/ruler-*-repair-seed1-$JET.jsonl $E3/ruler-*-repair-seed1-gentle-$MIL.jsonl \
        $E5D/ruler-*-$R-*.jsonl $DMG/ruler-*-$B-*.jsonl --out $OUT/tables-ruler.md
    : > $OUT/gates.md
    for m in "$JET repair-seed1" "$MIL repair-seed1-gentle"; do
      set -- $m; H=$1; SYN=$2
      gate "real QA: base -> budget ($H)"       $E4/ruler-*-base-$H.jsonl -- $QA/ruler-*-$B-$H.jsonl
      gate "real QA: synthetic -> budget ($H)"  $E4/ruler-*-$SYN-$H.jsonl -- $QA/ruler-*-$B-$H.jsonl
      gate "real QA: realmix -> budget ($H)"    $E5Q/ruler-*-$R-$H.jsonl  -- $QA/ruler-*-$B-$H.jsonl
      gate "real QA: budget -> realmix ($H), FAIL cells are budget gains"  $QA/ruler-*-$B-$H.jsonl -- $E5Q/ruler-*-$R-$H.jsonl
      for S in suite-s1 suite-s2 heldout multihop25; do  # one gate per file: s1/s2 reuse case ids, heldout/multihop25 share their 16K/32K ids with the suites
        gate "$S: base -> budget ($H)"       $E3/$S-base-$H.jsonl -- $DMG/$S-$B-$H.jsonl
        gate "$S: synthetic -> budget ($H)"  $E3/$S-$SYN-$H.jsonl -- $DMG/$S-$B-$H.jsonl
        gate "$S: realmix -> budget ($H)"    $E5D/$S-$R-$H.jsonl  -- $DMG/$S-$B-$H.jsonl
        gate "$S: budget -> realmix ($H), FAIL cells are budget gains"  $DMG/$S-$B-$H.jsonl -- $E5D/$S-$R-$H.jsonl
      done
      # no RULER gate: the generator repeats 10 (16K) and 4 (32K) case ids per file and check refuses them; outcome B reads tables-ruler.md
    done
    ls $DMG/ruler-*.jsonl >/dev/null 2>&1 && $PY - $E3/ruler-*-repair-seed1-$JET.jsonl $E3/ruler-*-repair-seed1-gentle-$MIL.jsonl $E5D/ruler-*-$R-*.jsonl $DMG/ruler-*-$B-*.jsonl <<'EOF'
import json, re, sys  # outcome B readout: a single-span answer to a multi-value / multi-query needle lists at most one 7-digit number
for f in sys.argv[1:]:
    rows = [json.loads(line) for line in open(f)]
    for t in ("ruler_niah_multivalue", "ruler_niah_multiquery"):
        bad = [r for r in rows if r["task"] == t and not r["contains"]]
        print(f"{f.rsplit('/', 1)[-1]} {t}: {len(bad)} failures, {sum(len(set(re.findall('[0-9]{7}', r['output']))) <= 1 for r in bad)} list <= 1 number")
EOF
    for f in $E3/bench-base-{$JET,$MIL}.json $E3/bench-repair-seed1-$JET.json $E3/bench-repair-seed1-gentle-$MIL.json $E5D/bench-*.json $DMG/bench-*.json \
             $E3/bpb-base-{$JET,$MIL}.json $E3/bpb-repair-seed1-$JET.json $E3/bpb-repair-seed1-gentle-$MIL.json $E5D/bpb-*.json $DMG/bpb-*.json; do
      [ -f "$f" ] && $PY -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"
    done
    echo "wrote $OUT/tables-qa.md, tables-damage.md, tables-multihop25.md, tables-ruler.md and gates.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

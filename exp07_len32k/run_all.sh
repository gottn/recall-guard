#!/usr/bin/env bash
# Experiment 7: 32K documents at 8B (arm 1) and the 2B synthetic-only control (arm 2). Outcomes in RESULTS.md.
# Cluster, training + the exp03 damage checks (robust.sbatch STAGE=repair; the adapters land in the run dir R):
#   D="--real-dir $HOME/data/rg/realqa --exclude-dir $HOME/data/rg/ruler-qa"; A40="--partition=prioritized --qos=normal --gres=gpu:a40:1"
#   STAGE=repair TRAIN_SEED=1 TRAIN_TAG=-budget32k TRAIN_DOCS=600 TRAIN_LENGTHS="8192 16384 32768" TRAIN_EXTRA="--lr 5e-5 $D" \
#     MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh robust $A40 --mem=56G --time=12:00:00   -> R
#   RUN_IN=$R STAGE=repair TRAIN_SEED=1 TRAIN_TAG=-syn1200 TRAIN_DOCS=1200 MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust $A40 --mem=32G --time=12:00:00
# Cluster, the exp04 real-QA cases with the new adapters (after the training jobs: --dependency=afterany:<job id>):
#   ADAPTER=$R/adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh realdocs --mem=48G --time=06:00:00   -> Q
#   RUN_IN=$Q ADAPTER=$R/adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs --mem=32G --time=04:00:00
# Mac: rsync -a --exclude 'adapter-*' --exclude 'slurm-*' --exclude 'suite-s?.jsonl' --exclude heldout.jsonl --exclude multihop25.jsonl "aau:$R/" exp07_len32k/results/raw/damage/
#      rsync -a --exclude 'slurm-*' "aau:$Q/" exp07_len32k/results/raw/qa/ && exp07_len32k/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
OUT=exp07_len32k/results; QA=$OUT/raw/qa; DMG=$OUT/raw/damage
E6Q=exp06_budget/results/raw/qa; E6D=exp06_budget/results/raw/damage; E5Q=exp05_realmix/results/raw/qa; E5D=exp05_realmix/results/raw/damage
E4=exp04_realdocs/results/raw; E3=exp03_robust/results/raw
JET=jet-ai_Jet-Nemotron-2B; MIL=JunxiongWang_Llama3.1-Mamba2-8B-dpo
B=repair-seed1-budget; L=repair-seed1-budget32k; S=repair-seed1-syn1200
gate() {  # gate <heading> <baseline files...> -- <candidate files...>: one check, appended to gates.md, never fatal
  local title="$1"; shift; local base=() cand=()
  while [ "$1" != "--" ]; do base+=("$1"); shift; done; shift; cand=("$@")
  ls "${base[@]}" "${cand[@]}" >/dev/null 2>&1 || { echo "skip $title (missing files)"; return; }
  { echo "### $title"; $PY -m recall_guard.cli check --baseline "${base[@]}" --candidate "${cand[@]}" || true; echo; } >> $OUT/gates.md
}
case "${1:-report}" in
  report)
    $PY -m recall_guard.cli report --results $E4/ruler-*-base-*.jsonl $E4/ruler-*-repair-seed1-$JET.jsonl $E4/ruler-*-repair-seed1-gentle-$MIL.jsonl \
      $E5Q/ruler-*-repair-seed1-realmix-$MIL.jsonl $E6Q/ruler-*.jsonl $QA/ruler-*.jsonl --out $OUT/tables-qa.md
    ls $DMG/suite-s*-repair-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/suite-s*-base-{$JET,$MIL}.jsonl $E3/suite-s*-repair-seed1-$JET.jsonl $E3/suite-s*-repair-seed1-gentle-$MIL.jsonl \
        $E5D/suite-s*-repair-seed1-realmix-$MIL.jsonl $E6D/suite-s*-$B-{$JET,$MIL}.jsonl $DMG/suite-s*-repair-*.jsonl --out $OUT/tables-damage.md
    ls $DMG/multihop25-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/multihop25-base-{$JET,$MIL}.jsonl $E3/multihop25-repair-seed1-$JET.jsonl $E3/multihop25-repair-seed1-gentle-$MIL.jsonl \
        $E5D/multihop25-repair-seed1-realmix-$MIL.jsonl $E6D/multihop25-$B-{$JET,$MIL}.jsonl $DMG/multihop25-repair-*.jsonl --out $OUT/tables-multihop25.md
    ls $DMG/ruler-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/ruler-*-base-{$JET,$MIL}.jsonl $E3/ruler-*-repair-seed1-$JET.jsonl $E3/ruler-*-repair-seed1-gentle-$MIL.jsonl \
        $E5D/ruler-*-repair-seed1-realmix-$MIL.jsonl $E6D/ruler-*-$B-{$JET,$MIL}.jsonl $DMG/ruler-*-repair-*.jsonl --out $OUT/tables-ruler.md
    : > $OUT/gates.md
    gate "real QA: base -> budget32k ($MIL)"    $E4/ruler-*-base-$MIL.jsonl -- $QA/ruler-*-$L-$MIL.jsonl
    gate "real QA: budget -> budget32k ($MIL)"  $E6Q/ruler-*-$B-$MIL.jsonl  -- $QA/ruler-*-$L-$MIL.jsonl
    gate "real QA: budget32k -> budget ($MIL), FAIL cells are budget32k gains"  $QA/ruler-*-$L-$MIL.jsonl -- $E6Q/ruler-*-$B-$MIL.jsonl
    gate "real QA: base -> syn1200 ($JET)"       $E4/ruler-*-base-$JET.jsonl -- $QA/ruler-*-$S-$JET.jsonl
    gate "real QA: synthetic -> syn1200 ($JET)"  $E4/ruler-*-repair-seed1-$JET.jsonl -- $QA/ruler-*-$S-$JET.jsonl
    for F in suite-s1 suite-s2 heldout multihop25; do  # one gate per file: s1/s2 reuse case ids, heldout/multihop25 share their 16K/32K ids with the suites
      gate "$F: base -> budget32k ($MIL)"    $E3/$F-base-$MIL.jsonl -- $DMG/$F-$L-$MIL.jsonl
      gate "$F: gentle -> budget32k ($MIL)"  $E3/$F-repair-seed1-gentle-$MIL.jsonl -- $DMG/$F-$L-$MIL.jsonl
      gate "$F: budget -> budget32k ($MIL)"  $E6D/$F-$B-$MIL.jsonl -- $DMG/$F-$L-$MIL.jsonl
      gate "$F: budget32k -> budget ($MIL), FAIL cells are budget32k gains"  $DMG/$F-$L-$MIL.jsonl -- $E6D/$F-$B-$MIL.jsonl
      gate "$F: base -> syn1200 ($JET)"       $E3/$F-base-$JET.jsonl -- $DMG/$F-$S-$JET.jsonl
      gate "$F: synthetic -> syn1200 ($JET)"  $E3/$F-repair-seed1-$JET.jsonl -- $DMG/$F-$S-$JET.jsonl
      gate "$F: budget -> syn1200 ($JET)"     $E6D/$F-$B-$JET.jsonl -- $DMG/$F-$S-$JET.jsonl
    done
    # no RULER gate: the generator repeats 10 (16K) and 4 (32K) case ids per file and check refuses them; arm 2 reads tables-ruler.md
    ls $DMG/ruler-*.jsonl >/dev/null 2>&1 && $PY - $E3/ruler-*-repair-seed1-$JET.jsonl $E6D/ruler-*-$B-$JET.jsonl $DMG/ruler-*-$S-$JET.jsonl <<'EOF'
import json, re, sys  # arm 2 readout: a single-span answer to a multi-value / multi-query needle lists at most one 7-digit number
for f in sys.argv[1:]:
    rows = [json.loads(line) for line in open(f)]
    for t in ("ruler_niah_multivalue", "ruler_niah_multiquery"):
        bad = [r for r in rows if r["task"] == t and not r["contains"]]
        print(f"{f.rsplit('/', 1)[-1]} {t}: {len(bad)} failures, {sum(len(set(re.findall('[0-9]{7}', r['output']))) <= 1 for r in bad)} list <= 1 number")
EOF
    for f in $E3/bench-base-{$JET,$MIL}.json $E3/bench-repair-seed1-$JET.json $E3/bench-repair-seed1-gentle-$MIL.json $E6D/bench-*.json $DMG/bench-*.json \
             $E3/bpb-base-{$JET,$MIL}.json $E3/bpb-repair-seed1-$JET.json $E3/bpb-repair-seed1-gentle-$MIL.json $E6D/bpb-*.json $DMG/bpb-*.json; do
      [ -f "$f" ] && $PY -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"
    done
    echo "wrote $OUT/tables-qa.md, tables-damage.md, tables-multihop25.md, tables-ruler.md and gates.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

#!/usr/bin/env bash
# Experiment 5: real-document QA in the repair mix. Predictions in RESULTS.md; generator recall_guard/real_data.py.
# Cluster, once: ssh aau 'bash -s' < exp05_realmix/fetch_data.sh      (SQuAD v2 train + HotpotQA train -> ~/data/rg/realqa)
# Cluster, training + the exp03 damage checks (robust.sbatch STAGE=repair; the adapter lands in the run dir R):
#   D="--real-dir $HOME/data/rg/realqa --exclude-dir $HOME/data/rg/ruler-qa"; A40="--partition=prioritized --qos=normal --gres=gpu:a40:1"
#   STAGE=repair TRAIN_SEED=1 TRAIN_TAG=-realmix TRAIN_EXTRA="$D" MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust $A40 --mem=32G --time=08:00:00   -> R
#   RUN_IN=$R STAGE=repair TRAIN_SEED=1 TRAIN_TAG=-realmix TRAIN_DOCS=300 TRAIN_LENGTHS="8192 16384" TRAIN_EXTRA="--lr 5e-5 $D" \
#     MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh robust $A40 --mem=48G --time=12:00:00
# Cluster, the exp04 real-QA cases with the new adapters (after the training jobs: --dependency=afterany:<job id>):
#   ADAPTER=$R/adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh realdocs --mem=32G --time=04:00:00   -> Q
#   RUN_IN=$Q ADAPTER=$R/adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil infra/cluster/submit.sh realdocs --mem=48G --time=06:00:00
# Mac: rsync -a --exclude 'adapter-*' --exclude 'slurm-*' "aau:$R/" exp05_realmix/results/raw/damage/
#      rsync -a --exclude 'slurm-*' "aau:$Q/" exp05_realmix/results/raw/qa/ && exp05_realmix/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
QA=exp05_realmix/results/raw/qa; DMG=exp05_realmix/results/raw/damage
E4=exp04_realdocs/results/raw; E3=exp03_robust/results/raw
JET=jet-ai_Jet-Nemotron-2B; QWEN=Qwen_Qwen2.5-1.5B; MIL=JunxiongWang_Llama3.1-Mamba2-8B-dpo; LLAMA=meta-llama_Llama-3.1-8B-Instruct
gate() {  # gate <heading> <baseline files...> -- <candidate files...>: one check, appended to gates.md, never fatal
  local title="$1"; shift; local base=() cand=()
  while [ "$1" != "--" ]; do base+=("$1"); shift; done; shift; cand=("$@")
  ls "${base[@]}" "${cand[@]}" >/dev/null 2>&1 || { echo "skip $title (missing files)"; return; }
  { echo "### $title"; $PY -m recall_guard.cli check --baseline "${base[@]}" --candidate "${cand[@]}" || true; echo; } >> exp05_realmix/results/gates.md
}
case "${1:-report}" in
  report)
    $PY -m recall_guard.cli report --results $E4/ruler-*.jsonl $QA/ruler-*.jsonl --out exp05_realmix/results/tables-qa.md
    ls $DMG/suite-s*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/suite-s*-base-{$JET,$MIL}.jsonl $E3/suite-s*-repair-seed1-$JET.jsonl $E3/suite-s*-repair-seed1-gentle-$MIL.jsonl $DMG/suite-s*-repair-seed[123]-realmix-*.jsonl \
      --out exp05_realmix/results/tables-damage.md
    ls $DMG/ruler-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/ruler-*-base-{$JET,$MIL}.jsonl $E3/ruler-*-repair-seed1-$JET.jsonl $E3/ruler-*-repair-seed1-gentle-$MIL.jsonl $DMG/ruler-*-repair-seed[123]-realmix-*.jsonl \
      --out exp05_realmix/results/tables-ruler.md
    : > exp05_realmix/results/gates.md
    for m in "$JET repair-seed1 $QWEN" "$MIL repair-seed1-gentle $LLAMA"; do
      set -- $m; H=$1; SYN=$2; SRC=$3
      gate "real QA: base -> realmix ($H)"       $E4/ruler-*-base-$H.jsonl  -- $QA/ruler-*-repair-seed1-realmix-$H.jsonl
      gate "real QA: synthetic -> realmix ($H)"  $E4/ruler-*-$SYN-$H.jsonl  -- $QA/ruler-*-repair-seed1-realmix-$H.jsonl
      gate "real QA: realmix -> synthetic ($H), FAIL cells are realmix gains"  $QA/ruler-*-repair-seed1-realmix-$H.jsonl -- $E4/ruler-*-$SYN-$H.jsonl
      gate "real QA: source -> realmix ($H), the remaining deficit"  $E4/ruler-*-base-$SRC.jsonl -- $QA/ruler-*-repair-seed1-realmix-$H.jsonl
      for S in suite-s1 suite-s2 heldout multihop25; do  # one gate per file: s1/s2 reuse case ids, heldout/multihop25 share their 16K/32K ids with the suites
        gate "$S: base -> realmix ($H)"       $E3/$S-base-$H.jsonl -- $DMG/$S-repair-seed1-realmix-$H.jsonl
        gate "$S: synthetic -> realmix ($H)"  $E3/$S-$SYN-$H.jsonl -- $DMG/$S-repair-seed1-realmix-$H.jsonl
      done
      # no RULER gate: the generator repeats 10 (16K) and 4 (32K) case ids per file, exp03 too, and check refuses them; P4(b) reads tables-ruler.md
    done
    for H in $JET $MIL; do for s in 2 3; do  # seeds 2-3: the README damage check (base -> adapter); seed spread reads the tables
      gate "real QA: base -> realmix seed $s ($H)"  $E4/ruler-*-base-$H.jsonl -- $QA/ruler-*-repair-seed$s-realmix-$H.jsonl
      for S in suite-s1 suite-s2 heldout multihop25; do gate "$S: base -> realmix seed $s ($H)"  $E3/$S-base-$H.jsonl -- $DMG/$S-repair-seed$s-realmix-$H.jsonl; done
    done; done
    for f in $E3/bench-base-{$JET,$MIL}.json $E3/bench-repair-seed1-$JET.json $E3/bench-repair-seed1-gentle-$MIL.json $DMG/bench-*.json \
             $E3/bpb-base-{$JET,$MIL}.json $E3/bpb-repair-seed1-$JET.json $E3/bpb-repair-seed1-gentle-$MIL.json $DMG/bpb-*.json; do
      [ -f "$f" ] && $PY -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"
    done
    echo "wrote exp05_realmix/results/tables-qa.md, tables-damage.md, tables-ruler.md and gates.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

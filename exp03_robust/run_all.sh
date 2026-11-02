#!/usr/bin/env bash
# Experiment 3: robustness of exp01/exp02 (docs/robustness.md, items 1, 2, 5, 6, 7).
# Cluster:
#   STAGE=base MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust            -> RUN
#   RUN_IN=$RUN STAGE=base MODEL=Qwen/Qwen2.5-1.5B RG_ENV=modern infra/cluster/submit.sh robust
#   for s in 1 2 3; do RUN_IN=$RUN STAGE=repair TRAIN_SEED=$s MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet infra/cluster/submit.sh robust --time=08:00:00; done
#   for s in 1 2;   do RUN_IN=$RUN STAGE=repair TRAIN_SEED=$s MODEL=Qwen/Qwen2.5-1.5B RG_ENV=modern infra/cluster/submit.sh robust --time=08:00:00; done
# Mac:
#   rsync -a --exclude 'adapter-*' --exclude 'slurm-*' "aau:$RUN/" exp03_robust/results/raw/ && exp03_robust/run_all.sh report
# Real-document QA for the gates: realdocs.sbatch with ADAPTER=$RUN/adapter-<slug>-seed<s>; commands and pull in exp04_realdocs/run_all.sh.
set -euo pipefail
cd "$(dirname "$0")/.."
E3=exp03_robust/results/raw; E4=exp04_realdocs/results/raw
JET=jet-ai_Jet-Nemotron-2B; MIL=JunxiongWang_Llama3.1-Mamba2-8B-dpo
gate() {  # gate <heading> <baseline files...> -- <candidate files...>: one check, appended to gates.md, never fatal
  local title="$1"; shift; local base=() cand=()
  while [ "$1" != "--" ]; do base+=("$1"); shift; done; shift; cand=("$@")
  ls "${base[@]}" "${cand[@]}" >/dev/null 2>&1 || { echo "skip $title (missing files)"; return; }
  { echo "### $title"; .venv/bin/python -m recall_guard.cli check --baseline "${base[@]}" --candidate "${cand[@]}" || true; echo; } >> exp03_robust/results/gates.md
}
case "${1:-report}" in
  report)
    # the two 50-case suites alone (n = 100 per cell, the headline numbers); the 25-case held-out and multi-hop files go to their own table
    .venv/bin/python -m recall_guard.cli report --results exp03_robust/results/raw/suite-s*-*.jsonl --out exp03_robust/results/tables-suites.md
    .venv/bin/python -m recall_guard.cli report --results exp03_robust/results/raw/heldout-*.jsonl exp03_robust/results/raw/multihop25-*.jsonl --out exp03_robust/results/tables-extra.md
    .venv/bin/python -m recall_guard.cli report --results exp03_robust/results/raw/ruler-*.jsonl --out exp03_robust/results/tables-ruler.md
    # the damage gates, base -> adapter: one per synthetic file (s1 / s2 reuse case ids), then real-document QA on the exp04
    # cases, which every synthetic gate misses for seed 2; no RULER gate (the generator repeats case ids, check refuses them)
    : > exp03_robust/results/gates.md
    for m in "$JET repair-seed1" "$JET repair-seed2" "$JET repair-seed3" "$MIL repair-seed1-gentle" "$MIL repair-seed2-gentle" "$MIL repair-seed3-gentle"; do
      set -- $m; H=$1; A=$2
      for S in suite-s1 suite-s2 heldout multihop25; do gate "$S: base -> $A ($H)" $E3/$S-base-$H.jsonl -- $E3/$S-$A-$H.jsonl; done
      gate "real QA: base -> $A ($H)" $E4/ruler-*-base-$H.jsonl -- $E4/ruler-*-$A-$H.jsonl
    done
    echo "wrote exp03_robust/results/tables-suites.md, tables-extra.md, tables-ruler.md and gates.md"
    for f in exp03_robust/results/raw/bench-*.json exp03_robust/results/raw/bpb-*.json; do [ -f "$f" ] && python3 -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"; done ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

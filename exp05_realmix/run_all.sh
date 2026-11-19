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
      --results $E3/suite-s*-base-{$JET,$MIL,$QWEN,$LLAMA}.jsonl $E3/suite-s*-repair-seed1-{$JET,$QWEN}.jsonl $E3/suite-s*-repair-seed1-gentle-$MIL.jsonl $DMG/suite-s*-repair-seed[123]-realmix-*.jsonl \
      --out exp05_realmix/results/tables-damage.md
    ls $DMG/ruler-*.jsonl >/dev/null 2>&1 && $PY -m recall_guard.cli report \
      --results $E3/ruler-*-base-{$JET,$MIL,$QWEN,$LLAMA}.jsonl $E3/ruler-*-repair-seed1-{$JET,$QWEN}.jsonl $E3/ruler-*-repair-seed1-gentle-$MIL.jsonl $DMG/ruler-*-repair-seed[123]-realmix-*.jsonl \
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
    # control (2026-11-18): the 2B recipe on the source. FAIL cells of the reverse gate are the control's gains.
    CTL="$QA/ruler-*-repair-seed1-realmix-$QWEN.jsonl"
    gate "real QA: source -> source + realmix (control)"  $E4/ruler-*-base-$QWEN.jsonl -- $CTL
    gate "real QA: source + realmix -> source, FAIL cells are the control's gains"  $CTL -- $E4/ruler-*-base-$QWEN.jsonl
    for s in 1 2 3; do
      gate "real QA: source + realmix -> Jet + realmix seed $s, the deficit after equal training"  $CTL -- $QA/ruler-*-repair-seed$s-realmix-$JET.jsonl
    done
    # control at 8B (pre-registered 2026-11-18): the gentle recipe on the source. The rule reads the qa_1 cells of the last gate.
    CTL8="$QA/ruler-*-repair-seed1-realmix-$LLAMA.jsonl"
    gate "real QA: source -> source + realmix (8B control)"  $E4/ruler-*-base-$LLAMA.jsonl -- $CTL8
    gate "real QA: source + realmix -> source (8B), FAIL cells are the control's gains"  $CTL8 -- $E4/ruler-*-base-$LLAMA.jsonl
    for s in 2 3; do gate "real QA: source -> realmix seed $s ($MIL), the remaining deficit"  $E4/ruler-*-base-$LLAMA.jsonl -- $QA/ruler-*-repair-seed$s-realmix-$MIL.jsonl; done
    for s in 1 2 3; do
      gate "real QA: source + realmix -> Mamba-in-the-Llama + realmix seed $s, the deficit after equal training"  $CTL8 -- $QA/ruler-*-repair-seed$s-realmix-$MIL.jsonl
    done
    for S in suite-s1 suite-s2 heldout multihop25; do  # the controls' damage checks: reported, not criteria
      gate "$S: source -> source + realmix (control)"     $E3/$S-base-$QWEN.jsonl  -- $DMG/$S-repair-seed1-realmix-$QWEN.jsonl
      gate "$S: source -> source + realmix (8B control)"  $E3/$S-base-$LLAMA.jsonl -- $DMG/$S-repair-seed1-realmix-$LLAMA.jsonl
    done
    $PY - <<'EOF'  # the controls' gains on qa_1 in cases of 100, and the pre-registered labels (RESULTS.md, Control and Control at 8B)
import json, os
from recall_guard.aggregate import binomial_tail_half
from recall_guard.score import first_line, strip_think
E4, QA, Q ="exp04_realdocs/results/raw", "exp05_realmix/results/raw/qa", "Qwen_Qwen2.5-1.5B"
LENGTHS = (4096, 16384, 32768)
hits = lambda p: sum(r["contains"] for r in map(json.loads, open(p)) if r["task"] == "ruler_qa_1")
# RULER's rule reads the whole output and every model runs on after its answer, so also count the first line only
gold = {c["id"]: c["answer"].lower().split("|") for L in LENGTHS for c in map(json.loads, open(f"exp04_realdocs/results/cases/ruler-{L}.jsonl"))}
hit1 = lambda r: any(a in first_line(strip_think(r["output"])).lower() for a in gold[r["case_id"]])
first = lambda p: sum(hit1(r) for r in map(json.loads, open(p)) if r["task"] == "ruler_qa_1")
ctl = f"{QA}/ruler-{{L}}-repair-seed1-realmix-{Q}.jsonl"
if os.path.exists(ctl.format(L=16384)):
    G = {L: hits(ctl.format(L=L)) - hits(f"{E4}/ruler-{L}-base-{Q}.jsonl") for L in (16384, 32768)}
    print("control gain on qa_1, cases of 100:", G, "->", "repair" if max(G.values()) <= 10 else "training" if max(G.values()) >= 20 else "mixed")
    print("first line only, qa_1 hits of 100 at 16K and 32K: source", [first(f"{E4}/ruler-{L}-base-{Q}.jsonl") for L in (16384, 32768)],
          "control", [first(ctl.format(L=L)) for L in (16384, 32768)],
          "| Jet + realmix seeds 1-3 at 32K", [first(f"{QA}/ruler-32768-repair-seed{s}-realmix-jet-ai_Jet-Nemotron-2B.jsonl") for s in (1, 2, 3)])
L8, M8 = "meta-llama_Llama-3.1-8B-Instruct", "JunxiongWang_Llama3.1-Mamba2-8B-dpo"
ctl8 = f"{QA}/ruler-{{L}}-repair-seed1-realmix-{L8}.jsonl"
if os.path.exists(ctl8.format(L=16384)):  # the label reads 16K, where the hybrid's gain fits in the source's room
    for name, n in (("whole output", hits), ("first line only", first)):
        src, c8 = ([n(p.format(L=L)) for L in LENGTHS] for p in (f"{E4}/ruler-{{L}}-base-{L8}.jsonl", ctl8))
        print(f"8B control, qa_1 hits of 100 at 4K/16K/32K, {name}: source", src, "control", c8, "gain", [b - a for a, b in zip(src, c8)],
              "| hybrid + realmix seeds 1-3", [[n(f"{QA}/ruler-{L}-repair-seed{s}-realmix-{M8}.jsonl") for s in (1, 2, 3)] for L in LENGTHS])
    G16 = hits(ctl8.format(L=16384)) - hits(f"{E4}/ruler-16384-base-{L8}.jsonl")
    print("8B control label at 16K:", "repair" if G16 <= 5 else "training" if G16 >= 10 else "mixed")
    # post hoc (2026-11-19): the deficit gate on the first line, where the control's later "Answer:" lines cannot score
    q1 = lambda p: {r["case_id"]: hit1(r) for r in map(json.loads, open(p)) if r["task"] == "ruler_qa_1"}
    for L in LENGTHS:
        c = q1(ctl8.format(L=L))
        for s in (1, 2, 3):
            h = q1(f"{QA}/ruler-{L}-repair-seed{s}-realmix-{M8}.jsonl")
            lost, gained = sum(c[k] and not h[k] for k in c), sum(h[k] and not c[k] for k in c)
            assert lost - gained == sum(c.values()) - sum(h.values())
            print(f"8B deficit after equal training, first line only, qa_1@{L} seed {s}: {lost} lost / {gained} gained, p {binomial_tail_half(lost, lost + gained):.3g}")
        for r in map(json.loads, open(ctl8.format(L=L))):
            if r["task"] == "ruler_qa_1" and r["contains"] and not hit1(r):
                print(f"8B control scores after its first line only, {r['case_id']}: gold {gold[r['case_id']][0]!r}, output {r['output'][:70]!r}")
EOF
    for f in $E3/bench-base-{$JET,$MIL,$QWEN,$LLAMA}.json $E3/bench-repair-seed1-{$JET,$QWEN}.json $E3/bench-repair-seed1-gentle-$MIL.json $DMG/bench-*.json \
             $E3/bpb-base-{$JET,$MIL,$QWEN,$LLAMA}.json $E3/bpb-repair-seed1-{$JET,$QWEN}.json $E3/bpb-repair-seed1-gentle-$MIL.json $DMG/bpb-*.json; do
      [ -f "$f" ] && $PY -c "import json,sys; d=json.load(open(sys.argv[1])); d.pop('bpb_values',None); print(json.dumps(d))" "$f"
    done
    echo "wrote exp05_realmix/results/tables-qa.md, tables-damage.md, tables-ruler.md and gates.md" ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

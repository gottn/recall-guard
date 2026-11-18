#!/usr/bin/env bash
# Experiment 14: does pinning the kernel configurations make the two layouts agree? Two decodes of realmix seed 2 at 64
# tokens with hf.pin_autotune active. Outcomes in RESULTS.md. step1.sbatch runs `cli run` with JOB_ARGS on a linked suite.
# Cluster, from ~/projects/recall-guard, one run dir per arm (V / extra arguments X): pin32 / --lengths 32768;  pinmix / -
#   A=~/runs/rg/robust/20261101-183230-8b5abb6/adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix
#   D=~/runs/rg/rescore/20261118-pin/$V; mkdir -p $D && ln -sf ~/data/rg/ruler-mvmq/ruler-mvmq.jsonl $D/suite.jsonl
#   TRITON_PRINT_AUTOTUNING=1 RUN_IN=$D MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet JOB_ARGS="--max-new-tokens 64 --adapter $A $X" \
#     infra/cluster/submit.sh step1 --partition=prioritized --qos=normal --gres=gpu:a40:1 --mem=32G --time=01:00:00 --nodelist=a256-a40-04
#   after the jobs, per arm: grep -h -A3 'Triton autotuning for function' $D/slurm-*.out > $D/autotune.txt
# Mac: rsync -a --exclude suite.jsonl --exclude 'slurm-*' --exclude '*.md' aau:runs/rg/rescore/20261118-pin/ exp14_pin/results/raw/ && exp14_pin/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
case "${1:-report}" in
  report)
    RAW="${RAW:-exp14_pin/results/raw}" $PY - <<'EOF'
import json, os, statistics as st
# pin32 against the 32K half of pinmix, exact; then where the pinned answers sit against the stored run (S) and cap64 (C).
J, RAW = "jet-ai_Jet-Nemotron-2B", os.environ["RAW"]
TASKS = ("ruler_niah_multivalue", "ruler_niah_multiquery")
load = lambda p: [json.loads(l) for l in open(p)]
key = lambda r: (r["case_id"], r["task"], r["length_bucket"])
half = lambda rows, L: [r for r in rows if r["task"] in TASKS and r["length_bucket"] == L]
S = {L: half(load(f"exp05_realmix/results/raw/damage/ruler-{L}-repair-seed2-realmix-{J}.jsonl"), L) for L in (16384, 32768)}
C = load(f"exp12_rerun_noise/results/raw/cap64/{J}.jsonl")
pin32, pinmix = (load(f"{RAW}/{v}/{J}.jsonl") for v in ("pin32", "pinmix"))

def diff(name, a, b):
    assert [key(r) for r in a] == [key(r) for r in b], f"{name}: case order differs"
    d = sum(x["output"] != y["output"] for x, y in zip(a, b))
    moved = sum(x["contains"] != y["contains"] for x, y in zip(a, b))
    print(f"{name}: {len(a) - d} of {len(a)} identical, {moved} verdicts differ")
    return d

d = diff("pin32 vs pinmix 32K half", pin32, half(pinmix, 32768))
diff("pin32 vs S", pin32, S[32768])
diff("pin32 vs C", pin32, half(C, 32768))
diff("pinmix 16K half vs S", half(pinmix, 16384), S[16384])
diff("pinmix vs C, all 200", pinmix, C)
print("outcome:", "pinned" if d == 0 else "not pinned")
for v in ("pin32", "pinmix"):
    p = f"{RAW}/{v}/autotune.txt"
    print(f"{v}: {open(p).read().count('Triton autotuning for function') if os.path.exists(p) else 'no'} autotuning lines in the log")
wall = lambda rows, L: st.median(r["wall_s"] for r in rows if r["length_bucket"] == L)
print("median seconds per case, pinned / unpinned (cap64):",
      {L: (round(wall(pinmix, L), 2), round(wall(C, L), 2)) for L in (16384, 32768)}, "| pin32:", round(wall(pin32, 32768), 2))
EOF
    ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

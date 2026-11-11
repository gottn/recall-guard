#!/usr/bin/env bash
# Experiment 13: does what a process decodes first set the path of its 32K answers? Four decodes of realmix seed 2 at 64
# tokens. Outcomes in RESULTS.md. No training and no code change: step1.sbatch runs `cli run` with JOB_ARGS on a linked suite.
# Cluster, once (the 32K half first; lines kept byte for byte):
#   cd ~/data/rg/ruler-mvmq && { tail -n 100 ruler-mvmq.jsonl; head -n 100 ruler-mvmq.jsonl; } > ruler-mvmq-rev.jsonl
# Cluster, from ~/projects/recall-guard, one run dir per arm (V / suite file F / extra arguments X):
#   full16 / ~/data/rg/ruler/ruler-16384.jsonl / -;  full32 / ~/data/rg/ruler/ruler-32768.jsonl / -;
#   only32 / ~/data/rg/ruler-mvmq/ruler-mvmq.jsonl / --lengths 32768;  rev / ~/data/rg/ruler-mvmq/ruler-mvmq-rev.jsonl / -
#   A=~/runs/rg/robust/20261101-183230-8b5abb6/adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix
#   D=~/runs/rg/rescore/20261111-layout/$V; mkdir -p $D && ln -sf $F $D/suite.jsonl
#   TRITON_PRINT_AUTOTUNING=1 RUN_IN=$D MODEL=jet-ai/Jet-Nemotron-2B RG_ENV=jet JOB_ARGS="--max-new-tokens 64 --adapter $A $X" \
#     infra/cluster/submit.sh step1 --partition=prioritized --qos=normal --gres=gpu:a40:1 --mem=32G --time=01:00:00 --nodelist=a256-a40-04
#   after the jobs, per arm: grep -h -A3 'Triton autotuning' $D/slurm-*.out > $D/autotune.txt
# Mac: rsync -a --exclude suite.jsonl --exclude 'slurm-*' --exclude '*.md' aau:runs/rg/rescore/20261111-layout/ exp13_decode_layout/results/raw/ && exp13_decode_layout/run_all.sh report
set -euo pipefail
cd "$(dirname "$0")/.."
PY=.venv/bin/python
case "${1:-report}" in
  report)
    RAW="${RAW:-exp13_decode_layout/results/raw}" $PY - <<'EOF'
import json, os, re
# Exact comparisons against the stored exp05 run (S) and exp12's cap64 (C); outcome by the rules in RESULTS.md.
J, RAW = "jet-ai_Jet-Nemotron-2B", os.environ["RAW"]
TASKS = ("ruler_niah_multivalue", "ruler_niah_multiquery")
load = lambda p: [json.loads(l) for l in open(p)]
key = lambda r: (r["case_id"], r["task"], r["length_bucket"])
S = {L: load(f"exp05_realmix/results/raw/damage/ruler-{L}-repair-seed2-realmix-{J}.jsonl") for L in (16384, 32768)}
C = load(f"exp12_rerun_noise/results/raw/cap64/{J}.jsonl")
arm = {v: load(f"{RAW}/{v}/{J}.jsonl") for v in ("full16", "full32", "only32", "rev")}
mv = lambda rows, L: [r for r in rows if r["task"] in TASKS and r["length_bucket"] == L]  # the multi-answer cases of one length

def diff(name, a, b):
    assert [key(r) for r in a] == [key(r) for r in b], f"{name}: case order differs"
    d = sum(x["output"] != y["output"] for x, y in zip(a, b))
    moved = sum(x["contains"] != y["contains"] for x, y in zip(a, b))
    print(f"{name}: {len(a) - d} of {len(a)} identical, {moved} verdicts differ")
    return d

diff("full16 vs S, all variants", arm["full16"], S[16384])
diff("full32 vs S, all variants", arm["full32"], S[32768])
layout = diff("full32 vs S, multi-answer", mv(arm["full32"], 32768), mv(S[32768], 32768)) == 0
diff("full32 vs C, multi-answer", mv(arm["full32"], 32768), mv(C, 32768))
o_s = diff("only32 vs S", arm["only32"], mv(S[32768], 32768))
o_c = diff("only32 vs C", arm["only32"], mv(C, 32768))
r32 = diff("rev 32K half vs S", mv(arm["rev"], 32768), mv(S[32768], 32768))
diff("rev 32K half vs C", mv(arm["rev"], 32768), mv(C, 32768))
r16 = diff("rev 16K half vs S", mv(arm["rev"], 16384), mv(S[16384], 16384))
print("outcome:", "not layout" if not layout else "first prompt" if o_s == 0 else "composition" if o_c == 0 else "mixed")
print("rev:", "one state per process" if r32 == 0 and r16 >= 10 else "one state per length" if r32 == 0 and r16 == 0 else "other")

# Mechanism readout, not a criterion: the configuration each autotuned kernel keeps, per arm, and the ones that differ.
pat = re.compile(r"function (\S+?),?\s+with key as (.*?),\s+finished.*?best config selected: (.*?);", re.S)
kept = {}
for v in arm:
    p = f"{RAW}/{v}/autotune.txt"
    kept[v] = {(f, k): c for f, k, c in pat.findall(open(p).read())} if os.path.exists(p) else {}
    print(f"{v}: {len(kept[v])} autotuned kernel keys in the log")
for fk in sorted(set().union(*kept.values())):
    cs = {v: kept[v].get(fk) for v in arm}
    if len(set(cs.values())) > 1:
        print("differs:", fk[0], fk[1][:80], cs)
EOF
    ;;
  *) echo "usage: run_all.sh report"; exit 1 ;;
esac

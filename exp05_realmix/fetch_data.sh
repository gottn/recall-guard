#!/usr/bin/env bash
# Experiment 5 training sources, fetched ONCE on the cluster front end into ~/data/rg/realqa (never into the repo):
#   ssh aau 'bash -s' < exp05_realmix/fetch_data.sh
# SQuAD v2 train and HotpotQA train: the splits disjoint from exp04's evaluation (SQuAD v2 dev, HotpotQA dev-distractor).
# RULER's HotpotQA host (curtis.ml.cmu.edu) did not answer on 2026-10-26; the fallback is the HuggingFace parquet mirror
# (hotpotqa/hotpot_qa, distractor/train-*.parquet) converted on the Mac by hotpot_from_parquet.py and copied up:
#   rsync -a hotpot_train_v1.1.json aau:data/rg/realqa/
set -euo pipefail
D="${1:-$HOME/data/rg/realqa}"; mkdir -p "$D"
[ -s "$D/train-v2.0.json" ] || curl -sSL -o "$D/train-v2.0.json" https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
[ -s "$D/hotpot_train_v1.1.json" ] || curl -sSL --connect-timeout 30 -o "$D/hotpot_train_v1.1.json" http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_train_v1.1.json \
  || { rm -f "$D/hotpot_train_v1.1.json"; echo "HotpotQA host unreachable: convert the parquet mirror on the Mac and rsync it to $D (see the header)"; }
ls -l "$D"; sha256sum "$D"/*.json

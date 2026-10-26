#!/usr/bin/env bash
# Experiment 5 training sources, fetched ONCE on the cluster front end into ~/data/rg/realqa (never into the repo):
#   ssh aau 'bash -s' < exp05_realmix/fetch_data.sh
# SQuAD v2 train and HotpotQA train: the splits disjoint from exp04's evaluation (SQuAD v2 dev, HotpotQA dev-distractor).
set -euo pipefail
D="${1:-$HOME/data/rg/realqa}"; mkdir -p "$D"
[ -s "$D/train-v2.0.json" ] || curl -sSL -o "$D/train-v2.0.json" https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v2.0.json
[ -s "$D/hotpot_train_v1.1.json" ] || curl -sSL -o "$D/hotpot_train_v1.1.json" http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_train_v1.1.json
ls -l "$D"; sha256sum "$D"/*.json

#!/usr/bin/env bash
# Sourced INSIDE the container by every job: builds (once) and selects the venv for $ENV (modern|jet).
# Venvs live in ~/pydeps so they survive across runs; torch is inherited from the container.
set -euo pipefail
ENV="${ENV:-modern}"
VENV="$HOME/pydeps/rg-$ENV"
REQ="$RG_ROOT/infra/cluster/requirements-$ENV.txt"
[ -x "$VENV/bin/python" ] || python -m venv --system-site-packages "$VENV"
STAMP="$VENV/.req-$(md5sum "$REQ" | cut -c1-8)"
[ -f "$STAMP" ] || { "$VENV/bin/pip" install -q -r "$REQ" && touch "$STAMP"; }
PY="$VENV/bin/python"
$PY -c 'import torch, transformers; print("torch", torch.__version__, "cuda", torch.cuda.is_available(), torch.cuda.get_device_name(0)); print("transformers", transformers.__version__)'

#!/usr/bin/env bash
# Sourced INSIDE the container by every job: builds (once) and selects the venv for $ENV (modern|jet) via RG_ENV; "ENV" itself is reserved by the container shell.
# Venvs live in ~/pydeps so they survive across runs; torch is inherited from the container.
set -euo pipefail
# Triton (used by flash-linear-attention) looks for libcuda.so via ldconfig, which the image lacks; --nv mounts it here.
export TRITON_LIBCUDA_PATH=/.singularity.d/libs
RG_ENV="${RG_ENV:-modern}"
VENV="$HOME/pydeps/rg-$RG_ENV"
REQ="$RG_ROOT/infra/cluster/requirements-$RG_ENV.txt"
[ -x "$VENV/bin/python" ] || python -m venv --system-site-packages "$VENV"
STAMP="$VENV/.req-$(md5sum "$REQ" | cut -c1-8)"
[ -f "$STAMP" ] || { "$VENV/bin/pip" install -q -r "$REQ" && "$VENV/bin/pip" uninstall -y -q peft torchao 2>/dev/null; touch "$STAMP"; }
PY="$VENV/bin/python"
$PY -c 'import torch, transformers; print("torch", torch.__version__, "cuda", torch.cuda.is_available(), torch.cuda.get_device_name(0)); print("transformers", transformers.__version__)'

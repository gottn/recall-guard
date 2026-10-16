#!/usr/bin/env bash
# Sourced INSIDE the container by every job: builds (once) and selects the venv for $ENV (modern|jet|mil) via RG_ENV; "ENV" itself is reserved by the container shell.
# Venvs live in ~/pydeps so they survive across runs; torch is inherited from the container.
set -euo pipefail
# Triton (used by flash-linear-attention) looks for libcuda.so via ldconfig, which the image lacks; --nv mounts it here.
export TRITON_LIBCUDA_PATH=/.singularity.d/libs
RG_ENV="${RG_ENV:-modern}"
VENV="$HOME/pydeps/rg-$RG_ENV"
REQ="$RG_ROOT/infra/cluster/requirements-$RG_ENV.txt"
[ -x "$VENV/bin/python" ] || python -m venv --system-site-packages "$VENV"
STAMP="$VENV/.req-$(md5sum "$REQ" | cut -c1-8)"
# "#src <git-url> <rev>" lines in the requirements file: unpackaged research code, fetched at a pinned rev onto sys.path.
src_on_path() {
  local site d _ url rev
  site="$("$VENV/bin/python" -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
  : > "$site/rg-src.pth"
  while read -r _ url rev; do
    d="$VENV/src/$(basename "$url")"
    rm -rf "$d"; git init -q "$d"; git -C "$d" fetch -q --depth 1 "$url" "$rev"; git -C "$d" checkout -q FETCH_HEAD
    echo "$d" >> "$site/rg-src.pth"
  done < <(grep '^#src ' "$REQ" || true)
}
exec 9>"$VENV.lock"; flock 9  # one builder at a time: parallel jobs raced on the same venv (exit 128)
if [ ! -f "$STAMP" ]; then  # a failed install exits here instead of stamping a broken venv
  "$VENV/bin/pip" install -q -r "$REQ"
  "$VENV/bin/pip" uninstall -y -q peft torchao 2>/dev/null || true
  src_on_path
  touch "$STAMP"
fi
flock -u 9
PY="$VENV/bin/python"
$PY -c 'import torch, transformers; print("torch", torch.__version__, "cuda", torch.cuda.is_available(), torch.cuda.get_device_name(0)); print("transformers", transformers.__version__)'

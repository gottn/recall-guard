#!/usr/bin/env bash
# Gate: lint, purity grep, tests, hook installed. Run before every commit.
set -euo pipefail
cd "$(dirname "$0")"
PY=.venv/bin/python
[ -x "$PY" ] || { echo "no .venv; run: uv venv --python 3.12 .venv && VIRTUAL_ENV=.venv uv pip install -e '.[dev]'"; exit 1; }
$PY -m ruff check .
# Purity gate: the core (everything but backends/ and cli.py) must not import I/O, torch or randomness-with-global-state.
if grep -nE '^(import|from) (torch|transformers|os|sys|pathlib|json|io|subprocess)\b' recall_guard/*.py | grep -v '^recall_guard/cli.py'; then
  echo "check.sh: effectful import in core module (allowed only in recall_guard/backends/ and recall_guard/cli.py)"; exit 1
fi
if grep -nE 'random\.(seed|random|randint|choice|shuffle)\(' recall_guard/*.py; then
  echo "check.sh: module-level random.* call in core; use an explicit random.Random(seed) instance"; exit 1
fi
$PY -m pytest
[ "$(git config core.hooksPath)" = ".githooks" ] || { echo "run: git config core.hooksPath .githooks"; exit 1; }
echo "check.sh: ok"

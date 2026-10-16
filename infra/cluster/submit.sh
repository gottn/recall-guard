#!/usr/bin/env bash
# The only way jobs start on the cluster. Run ON the front end, from the repo checkout:
#   infra/cluster/submit.sh <job> [extra sbatch args]            e.g. infra/cluster/submit.sh smoke
#   MODEL=Qwen/Qwen3.5-4B RG_ENV=modern infra/cluster/submit.sh step1
#   RUN_IN=~/runs/rg/step1/<run> MODEL=... infra/cluster/submit.sh step1   add a model to an existing run
# Pulls fast-forward only, refuses a dirty checkout, records the commit, writes outputs OUTSIDE the repo.
# Whole script is one function so bash parses it fully BEFORE the pull can rewrite this file underneath it.
set -euo pipefail
main() {
JOB="${1:?usage: submit.sh <job> [sbatch args]}"; shift || true
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
SCRIPT="infra/slurm/$JOB.sbatch"
git pull --ff-only --quiet
[ -f "$SCRIPT" ] || { echo "no such job: $SCRIPT"; ls infra/slurm; exit 1; }
if [ -n "$(git status --porcelain --untracked-files=no)" ]; then
  echo "refusing to submit: cluster checkout has local modifications (develop on the Mac, pull here)"; git status --short; exit 1
fi
SHA="$(git rev-parse --short HEAD)"
if [ -n "${RUN_IN:-}" ]; then
  OUT="$(cd "$RUN_IN" && pwd)"
  case "$OUT" in "$HOME/runs/rg/"*) ;; *) echo "RUN_IN must be an existing run under ~/runs/rg: $OUT"; exit 1 ;; esac
else
  OUT="$HOME/runs/rg/$JOB/$(date +%Y%m%d-%H%M%S)-$SHA"
  mkdir -p "$OUT"
fi
git log -1 --format='%H%n%s' > "$OUT/commit-$(date +%Y%m%d-%H%M%S).txt"
export RG_OUT="$OUT" RG_SHA="$SHA" RG_ROOT="$ROOT" MODEL="${MODEL:-}" RG_ENV="${RG_ENV:-modern}" JOB_ARGS="${JOB_ARGS:-}"
NAME="rg-$JOB${MODEL:+-${MODEL##*/}}"
JOBID=$(sbatch --parsable --job-name="$NAME" --output="$OUT/slurm-%j.out" "$@" "$SCRIPT")
echo "submitted $JOB as job $JOBID @ $SHA"
echo "output:  $OUT"
echo "watch:   squeue -j $JOBID ; tail -f $OUT/slurm-$JOBID.out"
}
main "$@"

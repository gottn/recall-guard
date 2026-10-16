# recall-guard

A recall-regression harness for long-context language models. It generates stress tests that
target the way fixed-size memories fail (near-duplicate keys, facts that change, multi-hop
chains), runs them against any model, and reports a recall curve by context length.

Needle-in-a-haystack tests sit in the easy corner of this problem: one random key, one static
fact. Hybrid models (3 of 4 layers linear attention) pass them and still break on real
documents. This harness is built to catch that class of failure before customers do.

## Layout

- `recall_guard/` — the package. Everything outside `backends/` and `cli.py` is pure.
  - `types.py` frozen records (Case, Result)
  - `filler.py` deterministic filler text
  - `tasks.py` case generators, one per stressor
  - `suite.py` builds a suite (tasks × lengths × seeds) sized with a reference tokenizer
  - `score.py` scoring; `aggregate.py` results → table rows
  - `backends/hf.py` HuggingFace completion backend (the only GPU code)
  - `cli.py` `generate | run | report`
- `exp01_step1/` — Experiment 1: do the stressors separate hybrid from full attention where the needle test does not?
- `infra/` — cluster setup, Slurm jobs. Jobs start only via `infra/cluster/submit.sh`.

## Develop

```
uv venv --python 3.12 .venv && VIRTUAL_ENV=.venv uv pip install -e '.[dev]'
./check.sh
```

Read `STATE.md` first. Style and commit rules are in `STYLE.md`.

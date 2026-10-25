# recall-guard

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](pyproject.toml)

A recall-regression harness for long-context language models, and a post-hoc repair for converted hybrids.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/img/explainer-dark.png">
  <img src="docs/img/explainer-light.png" alt="Three documents: one fact hidden, found 100% of the time; sixteen facts hidden, one asked for, found 25% of the time against 99% for the source transformer; the same model after 45 minutes of training on under 1% of its weights, found 100% of the time">
</picture>

A converted hybrid is a pretrained transformer whose attention layers were mostly replaced by linear-attention or
state-space layers. Such models pass the single-needle test and still fail to recall one of sixteen planted facts at
32K tokens. A LoRA adapter on under 1% of the weights, trained for 45 minutes on synthetic many-fact documents, brings
recall back to the source model's level.

## Install

```
uv venv --python 3.12 .venv && VIRTUAL_ENV=.venv uv pip install -e '.[dev]'
git config core.hooksPath .githooks && ./check.sh
```

Running models needs `uv pip install -e '.[run]'`; the converted hybrids need the environments pinned in
`infra/cluster/requirements-*.txt`.

## Run

```
python -m recall_guard.cli generate --out suite.jsonl --tokenizer Qwen/Qwen2.5-1.5B --cases 25
python -m recall_guard.cli run --suite suite.jsonl --model Qwen/Qwen2.5-1.5B --out qwen.jsonl
python -m recall_guard.cli run --suite suite.jsonl --model jet-ai/Jet-Nemotron-2B --trust-remote-code --out jet.jsonl
python -m recall_guard.cli report --results qwen.jsonl jet.jsonl --pair jet-ai/Jet-Nemotron-2B=Qwen/Qwen2.5-1.5B
python -m recall_guard.cli check --baseline qwen.jsonl --candidate jet.jsonl
```

Tasks: `needle`, `many_random`, `many_similar`, `updated`, `multihop`, `heldout_many`, at 1K to 32K tokens, sized
under one reference tokenizer so every model sees byte-identical prompts. A case is recalled when the planted six-digit
code appears on the first line of the completion.

`check` is the CI gate: it pairs the two runs on case id, applies the exact one-sided McNemar test to every
(task, length) cell and to all cases pooled, and exits 1 when the candidate recalls less (alpha 0.05, split over the
cells). On the runs above it fails `many_random` and `many_similar` at 32K and leaves `needle` alone. A cell trips
once about ten cases are lost and none gained, so use `--cases 50` or more to catch a 0.2 drop in a single cell; the
pooled row catches smaller drops spread across the suite.

Repair:

```
python -m recall_guard.cli train --model jet-ai/Jet-Nemotron-2B --trust-remote-code --out adapter/ --n-docs 300 --lr 5e-5
python -m recall_guard.cli run   --suite suite.jsonl --model jet-ai/Jet-Nemotron-2B --trust-remote-code --adapter adapter/ --out jet-repaired.jsonl
```

`bench` (ARC-Easy, HellaSwag), `ppl` (bits per byte on long text) and `import-ruler` (RULER cases) are documented in
`python -m recall_guard.cli -h`.

## Results

`exp01_step1/`, `exp02_repair/`, `exp03_robust/` and `exp04_realdocs/` each hold a `RESULTS.md` and every raw completion
under `results/raw/`; `STATE.md` is the lab notebook. `exp*/run_all.sh report` regenerates the tables from them.
`exp04_realdocs/` repeats the test on real Wikipedia QA (RULER qa_1 and qa_2, 100 questions per cell): the hybrids match
their sources at 4K and lose 0.24 (2B) and 0.64 (8B) of single-document recall at 32K; the adapter recovers 58% of that gap
at both scales with no cell regressing.

## License

MIT. Model outputs in `results/raw` were produced with Qwen2.5, Jet-Nemotron, Llama 3.1 and Mamba-in-the-Llama
checkpoints under their own licenses.

# STATE

Updated: 2026-10-16

## Goal
Build a recall-regression tool production teams would run in CI, and prove it catches long-context
recall failures in hybrid (linear-attention) models that needle tests miss.

## Step 1 (exp01) — the premise test
Compare hybrid vs full-attention pairs on five tasks × six context lengths:
`needle` (control), `many_random` (16 unrelated keys), `many_similar` (16 near-duplicate keys),
`updated` (facts overwritten mid-document), `multihop` (2-hop chains).
Pairs: Qwen3.5-4B (hybrid) vs Qwen3-4B; Jet-Nemotron-2B (hybrid, Qwen2.5 MLPs) vs Qwen2.5-1.5B.
Verdict rule: the tool earns its existence if a stressor separates the pairs at a length where `needle` does not.

## Status (2026-10-16)
- Harness complete and gated (13 tests, purity grep): generate / run / report. Local CPU smoke on Qwen2.5-0.5B passed.
- Cluster: repo cloned to ~/projects/recall-guard via deploy key; jobs submit only through infra/cluster/submit.sh.
- Modern smoke passed on an A10 (torch 2.9 nv25.09, transformers 5.20); jet venv builds in ~25 min, cached in ~/pydeps/rg-jet.
- step1 run dir: ~/runs/rg/step1/20261016-121320-8beb29d (suite.jsonl, 750 cases, generated at 8beb29d). Jobs: Qwen2.5-1.5B 1085911, Qwen3.5-4B 1086038, Qwen3-4B 1086039. Jet-Nemotron-2B awaits its smoke (1086025).
- Mac: `.venv` has CPU torch; `exp01_step1/run_all.sh report` builds the tables from pulled JSONL.

## Decisions
- Completion-style prompts, no chat template, greedy decoding, 16 new tokens, for every model.
- Suite is generated once with the Qwen2.5 tokenizer as reference and shared by all models.
- Two cluster envs: `modern` (transformers main, Qwen3/3.5) and `jet` (transformers 4.53 + jet-ai fla fork).

## Traps
- `ENV` is overwritten by the container shell (/etc/shinit_v2): the env selector is `RG_ENV`.
- Triton inside singularity needs `TRITON_LIBCUDA_PATH=/.singularity.d/libs` (env.sh sets it) or fla kernels die with 'libcuda.so cannot found'.
- A100 partition needs `--qos=unprivileged`; the account default QOS `normal` is refused.
- Qwen3.5 opens every raw completion with `<think>`; the backend prefills the empty block when the tokenizer has the token, and the scorer strips think blocks. Stored outputs are raw, so re-scoring is free.
- submit.sh pulls inside itself; its body is one function so bash parses it before the pull rewrites it.
- Parallel jobs in one run dir: the suite is written to a per-pid temp file then renamed.
- Jet-Nemotron pins transformers<=4.53 and its own flash-linear-attention fork; never share its venv.
- Qwen3.5/Qwen3 default to thinking mode under the chat template; completion prompts avoid it.

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

## Status
- Repo scaffolded. Nothing measured yet.

## Decisions
- Completion-style prompts, no chat template, greedy decoding, 16 new tokens, for every model.
- Suite is generated once with the Qwen2.5 tokenizer as reference and shared by all models.
- Two cluster envs: `modern` (transformers main, Qwen3/3.5) and `jet` (transformers 4.53 + jet-ai fla fork).

## Traps
- Jet-Nemotron pins transformers<=4.53 and its own flash-linear-attention fork; never share its venv.
- Qwen3.5/Qwen3 default to thinking mode under the chat template; completion prompts avoid it.

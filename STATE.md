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
Verdict rule: the tool earns its existence if a stressor separates the pairs at a length where `needle` does not. **Met** (2026-10-16): see exp01_step1/RESULTS.md.

## Status (2026-10-16, evening)
- **Step 1 done, verdict yes for the matched pair**: Jet-Nemotron-2B keeps needle=1.00 to 32K but drops to 0.16–0.20 on 16 keys at 32K vs 0.68–0.72 for its Qwen2.5-1.5B base; gap opens at 16K. Qwen3.5-4B shows no key deficit, a 0.24–0.28 multi-hop deficit at 8–16K. Hybrids win on overwritten facts. See exp01_step1/RESULTS.md.
- Earlier today:
- Harness complete and gated (13 tests, purity grep): generate / run / report. Local CPU smoke on Qwen2.5-0.5B passed.
- Cluster: repo cloned to ~/projects/recall-guard via deploy key; jobs submit only through infra/cluster/submit.sh.
- Modern smoke passed on an A10 (torch 2.9 nv25.09, transformers 5.20); jet venv builds in ~25 min, cached in ~/pydeps/rg-jet.
- step1 run dir: ~/runs/rg/step1/20261016-121320-8beb29d (suite.jsonl, 750 cases, generated at 8beb29d). Jobs: Qwen2.5-1.5B 1085911, Qwen3.5-4B 1086038, Qwen3-4B 1086039. Jet-Nemotron-2B awaits its smoke (1086025).
- Mac: `.venv` has CPU torch; `exp01_step1/run_all.sh report` builds the tables from pulled JSONL.

## Experiment 2 (exp02_repair) — can training repair a hybrid's long-context recall?
LoRA (own implementation, recall_guard/backends/lora.py) on every linear projection outside the MLPs, loss only on
answer tokens, synthetic documents of 16-48 keys (random / near-duplicate / overwritten) at 8K-16K, 8 questions each.
Evaluate after: step1 suite (same file), `heldout_many` (parcel template, never trained on), ARC-Easy + HellaSwag (500 each).
Control: identical recipe on Qwen2.5-1.5B. Gain in both = format familiarity; gain only in the hybrid = repair.
Smokes passed (Jet: 9.4 GB peak, 1344 tok/s at 16K; control 8422 tok/s). Full runs submitted 2026-10-16 13:26 into
`~/runs/rg/exp02/20261016-132629-5c3e622`: Jet base 1087235, Jet repair 1087236, Qwen2.5 base 1087237, Qwen2.5 repair 1087238
(600 docs at 8K/16K/32K, seed 0). Pull with `rsync -a 'aau:<run>/*.jsonl' 'aau:<run>/*.json' exp02_repair/results/raw/` then `exp02_repair/run_all.sh report`.

## Next
1. n=100 at 16K/32K, three seeds, Jet pair (confirms the 16K gap).
2. Key count 16→64 and 64K for Jet (capacity curve).
3. Second matched pair (LoLCATs or Mamba-in-the-Llama vs Llama-3-8B).
4. Step 2: fine-tune a hybrid, measure before/after with this suite.

## Decisions
- Completion-style prompts, no chat template, greedy decoding, 16 new tokens, for every model.
- Suite is generated once with the Qwen2.5 tokenizer as reference and shared by all models.
- Two cluster envs: `modern` (transformers main, Qwen3/3.5) and `jet` (transformers 4.53 + jet-ai fla fork).

## Traps
- PEFT >= 0.21 refuses the image's torchao 0.13; torchao >= 0.16 needs torch 2.10 (image has 2.9). Use the own LoRA; never add peft/torchao.
- Full-vocabulary logits at 16K are 9.3 GiB in float32: apply lm_head only at answer positions (train.answer_loss).
- Commit subjects are measured in bytes by the hook: the em dash costs 3, so keep subjects under ~95 characters.
- `ENV` is overwritten by the container shell (/etc/shinit_v2): the env selector is `RG_ENV`.
- Triton inside singularity needs `TRITON_LIBCUDA_PATH=/.singularity.d/libs` (env.sh sets it) or fla kernels die with 'libcuda.so cannot found'.
- A100 partition needs `--qos=unprivileged`; the account default QOS `normal` is refused.
- Qwen3.5 opens every raw completion with `<think>`; the backend prefills the empty block when the tokenizer has the token, and the scorer strips think blocks. Stored outputs are raw, so re-scoring is free.
- submit.sh pulls inside itself; its body is one function so bash parses it before the pull rewrites it.
- Parallel jobs in one run dir: the suite is written to a per-pid temp file then renamed.
- Jet-Nemotron pins transformers<=4.53 and its own flash-linear-attention fork; never share its venv.
- Qwen3.5/Qwen3 default to thinking mode under the chat template; completion prompts avoid it.

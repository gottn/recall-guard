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

## Status (2026-10-16, night)
- **Exp02 done, verdict yes**: 42 min of LoRA on one A100 lifts Jet-Nemotron-2B from 0.16 to 0.92 on 16 keys at 32K (control 0.91), transfers to the unseen parcel template (0.24 to 0.84), ARC/HellaSwag unchanged. Regression: multi-hop (untrained) collapses to ~0.03 via a one-hop shortcut. The exp01 overwrite advantage is downgraded (prompt-following). See exp02_repair/RESULTS.md.
- **Step 1 done, verdict yes for the matched pair**: Jet-Nemotron-2B keeps needle=1.00 to 32K but drops to 0.16–0.20 on 16 keys at 32K vs 0.68–0.72 for the Qwen2.5-1.5B it was converted from; gap opens at 16K. Qwen3.5-4B shows no key deficit, a 0.24–0.28 multi-hop deficit at 8–16K. Hybrids win on overwritten facts. See exp01_step1/RESULTS.md.
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

## Experiment 3 (exp03_robust) — robustness items 1, 2, 5, 6, 7
Run dir `~/runs/rg/robust/20261016-171229-9f67d4b`, submitted 2026-10-16 17:12. Jobs: Jet base 1089542, Qwen2.5 base 1089543,
Jet repair seeds 1-3 = 1089544-46, Qwen2.5 repair seeds 1-2 = 1089547-48. Each evaluates: our suites seed 1 and 2 (n=50 at
16K/32K), held-out parcels, 25 multi-hop cases, six RULER needle variants at 16K/32K (NVIDIA generator, ~/data/rg/ruler),
ARC/HellaSwag, bits per byte on Moby Dick at 16K; repair jobs train the v2 mix (with multi-hop) and add the unmerged-adapter
and chat-template checks at 32K. Collect: `rsync -a --exclude 'adapter-*' --exclude 'slurm-*' aau:<run>/ exp03_robust/results/raw/`
then `exp03_robust/run_all.sh report`.
Item 9 unblocked 2026-10-16 evening: Llama 3.1 licence accepted (user musab96) and a fine-grained token stored at ~/hf_cache/token on aau (HF_TOKEN also in ~/.bashrc); a real gated download returns 200. A background agent is integrating the Mamba-in-the-Llama and LoLCATs loaders (recall_guard/backends/loaders.py, env `mil`, infra/slurm/mil_smoke.sbatch).
Candidate 8B checkpoints: JunxiongWang/Llama3.1-Mamba2-8B-dpo (Mamba-in-the-Llama), hazyresearch/lolcats-llama-3.1-8b-ft-lora.
8B loaders (in progress 2026-10-16 17:50): `recall_guard/backends/loaders.py` routes ids to `backends/mil.py` (Mamba-in-the-Llama:
HF Llama skeleton from the repo config + MambaInLlama Mamba-2 layers, Triton only, no CUDA builds); env `mil`
(requirements-mil.txt, `#src` lines fetched by env.sh). Smoke submitted at 86512f5: L4 debug 1089694 (prioritized), A100 1089695,
logs under `~/runs/rg/mil_smoke/`. Next: read the logs, fix, resubmit (`RG_ENV=mil infra/cluster/submit.sh mil_smoke`) until the
4K needle has contains=True; then write `backends/lolcats.py` (base meta-llama/Llama-3.1-8B + distill + ft-lora, own LoRA merge, no peft).

## Next
1. Length generalisation of the repair: train at <=16K, test at 32K/64K.
2. Repair data with multi-hop included; confirm the multi-hop regression disappears.
3. Capacity frontier after repair: 32/64/128 keys at 32K.
4. Scale to a matched 8B pair (LoLCATs or Mamba-in-the-Llama vs Llama-3-8B).
5. Step 2: does an ordinary instruction fine-tune undo the repair or break an unrepaired hybrid?
6. Still owed from exp01: n=100 with seeds at 16K (the 16K gap was template-dependent: parcels held 0.96).

## Decisions
- Completion-style prompts, no chat template, greedy decoding, 16 new tokens, for every model.
- Suite is generated once with the Qwen2.5 tokenizer as reference and shared by all models.
- Two cluster envs: `modern` (transformers main, Qwen3/3.5) and `jet` (transformers 4.53 + jet-ai fla fork).

## Prior art
Read docs/prior-art.md before writing anything public. Key points: Qwen2.5-1.5B is Jet's initialisation checkpoint, not a weight-identical base (stage 2 trained the MLPs for 350B tokens); Jet-Long already shows an unpaired RULER drop at 32K (46.59); Lizard (50% softmax) reports parity to 32K, so the deficit depends on how few attention layers survive; no published post-hoc repair with transfer and no-damage numbers.

## Traps
- PEFT >= 0.21 refuses the image's torchao 0.13; torchao >= 0.16 needs torch 2.10 (image has 2.9). Use the own LoRA; never add peft/torchao.
- Full-vocabulary logits at 16K are 9.3 GiB in float32: apply lm_head only at answer positions (train.answer_loss).
- Commit subjects are measured in bytes by the hook: the em dash costs 3, so keep subjects under ~95 characters.
- After a hook rejection the index stays staged: run `git reset` before re-adding, or the next commit sweeps everything
  (commits 19aa2a0 and 9f67d4b are complete but mislabeled for this reason).
- `ENV` is overwritten by the container shell (/etc/shinit_v2): the env selector is `RG_ENV`.
- Triton inside singularity needs `TRITON_LIBCUDA_PATH=/.singularity.d/libs` (env.sh sets it) or fla kernels die with 'libcuda.so cannot found'.
- A100 partition needs `--qos=unprivileged`; the account default QOS `normal` is refused.
- Qwen3.5 opens every raw completion with `<think>`; the backend prefills the empty block when the tokenizer has the token, and the scorer strips think blocks. Stored outputs are raw, so re-scoring is free.
- submit.sh pulls inside itself; its body is one function so bash parses it before the pull rewrites it.
- Parallel jobs in one run dir: the suite is written to a per-pid temp file then renamed.
- Jet-Nemotron pins transformers<=4.53 and its own flash-linear-attention fork; never share its venv.
- Qwen3.5/Qwen3 default to thinking mode under the chat template; completion prompts avoid it.

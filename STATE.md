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
**8B stage complete (2026-10-17 early):** repair trained at <=16K lifts the 8B hybrid to 0.98/0.91 on keys at 32K (Llama 0.99/1.00), RULER MK1/MK2 to 1.00/0.96; but damage is real at 8B: bpb +15%, HellaSwag -3 to -5 points. Four 8B anti-forgetting runs are queued in the exp03 run dir (all seed 1, trained at <=16K, evaluated to 32K with RULER, bench, bpb):
Moved to A40 GPUs (prioritized partition, qos normal) because one user held all A100s: 1091565 `-gentle` (300 docs, lr 5e-5); 1091581 `-replay` (600 docs, every other example a War-and-Peace window with full LM loss; first attempt 1091566 OOMed on full-sequence logits, fixed by chunked loss in 5c7fb47);
1091609 `-qk` (600 docs, LoRA on q_proj/k_proj only; first attempt 1091567 trained q_proj only because the `|` in TRAIN_EXTRA became a shell pipe, its adapter is kept as `-qonly`, unevaluated); 1091582 `-gentle-replay` (300 docs, lr 5e-5, replay, weight decay 0.01).
Results so far (32K, n=100; bpb at 16K): heavy keys 0.98/0.91, multi-hop 0.85, bpb 1.156 (+15%); gentle keys 1.00/0.99, multi-hop 0.99,
RULER MK1 0.96, bpb 1.065 (+5.7%), HS within noise; gentle+replay bpb 0.978 but multi-hop 0.30; full replay bpb 0.992 but multi-hop 0.36 and
RULER multi-value 0.00. Dose keeps recall, replay removes damage; they oppose. Next recipe queued: 1092559 `-gentle2-replay25` (800 examples,
lr 5e-5, one in four natural). qk (1091609) RULER/damage pending. Base: bpb 1.008, HS 0.600/0.778, keys 0.25.
Commit 56e52c0 is labelled ci but also carries the train.py/cli.py replay+targets+weight-decay code (hook rejection swept the index). See exp03_robust/RESULTS.md items 20-23.
**2B stage complete (night of 2026-10-16):** three hybrid seeds and two control seeds; the hybrid reaches the control's post-training level on our suites (1.00); on RULER the control was already at ceiling so the hybrid's gains are repair; single-answer training hurts multi-answer RULER tasks in both models (coverage rule, third instance); bpb +0.4-0.6% in both. See exp03_robust/RESULTS.md items 10-13.
**Base stage (earlier):** RULER multi-key sees the Jet failure (MK1 0.56 vs 0.94 at 32K; MV 0.02 vs 0.46), so the
harness has no detection advantage over RULER; the 16K random-key gap is confirmed at n=100 (0.57 vs 0.90); Jet's needle at 32K is
0.86 at n=100 (not 1.00); generation is deterministic (150/150 identical completions across runs). See exp03_robust/RESULTS.md.
Item 9 unblocked 2026-10-16 evening: Llama 3.1 licence accepted (user musab96) and a fine-grained token stored at ~/hf_cache/token on aau (HF_TOKEN also in ~/.bashrc); a real gated download returns 200. A background agent is integrating the Mamba-in-the-Llama and LoLCATs loaders (recall_guard/backends/loaders.py, env `mil`, infra/slurm/mil_smoke.sbatch).
Candidate 8B checkpoints: JunxiongWang/Llama3.1-Mamba2-8B-dpo (Mamba-in-the-Llama), hazyresearch/lolcats-llama-3.1-8b-ft-lora.
8B loaders (2026-10-16 18:15): `recall_guard/backends/loaders.py` routes ids to `backends/mil.py` (Mamba-in-the-Llama) and
`backends/lolcats.py` (LoLCATs); env `mil` (requirements-mil.txt; `#src` lines fetched by env.sh; builds in ~15 min, cached
in ~/pydeps/rg-mil). MIL smoke PASSED on an L4 (job 1089694, 86512f5): 4K needle contains=True exact=True, heldout_many
contains=True, load 237 s (33 GB fp32 .bin, ~4 min download), peak 16.2 GiB, first case 120 s (Triton JIT), second 1.5 s.
A100 proof run 1089695 still queued (behind the exp03 jobs). Logs under `~/runs/rg/mil_smoke/`.
LoLCATs (base Llama-3.1-8B + distill + ft LoRA merged) loads in 30-70 s, peak 18.0 GiB at 4K, fluent output, but FIDELITY
UNVERIFIED: needle right at 128 and 512 tokens, wrong at 1K/4K; heldout_many wrong from 512 up; Moby Dick bits/byte 0.955
at 1K and 1.055 at 2K vs 0.315/0.301 for Llama-3.1-8B (jobs 1089746-50). Suspect: their demo config loads
meta-llama/Meta-Llama-3-8B (403 for us, licence not accepted) while the repo names say 3.1. Test once access exists:
`MODEL=hazyresearch/lolcats-llama-3.1-8b-ft-lora:meta-llama/Meta-Llama-3-8B LENGTHS="512 4096" PPL_WINDOW=1024 RG_ENV=mil
infra/cluster/submit.sh mil_smoke --partition=prioritized --qos=normal --gres=gpu:l4:1`. Diagnostics 1089772-74: at 128
tokens (inside the softmax window) LoLCATs 0.875 vs Llama 0.792 bits/byte, so the window + LoRA path is sane; LoLCATs gets
WORSE with more context (0.875 -> 0.955 -> 1.055 at 128/1K/2K) while Llama improves (0.79 -> 0.32): the linear branch
hurts. Distill-only (no LoRA) 1.40 at 1K. Do not run the full suite on LoLCATs before the base question is settled.
Full suite: `MODEL=JunxiongWang/Llama3.1-Mamba2-8B-dpo RG_ENV=mil RUN_IN=<step1 run> infra/cluster/submit.sh step1`.

## 8B pair (item 9), submitted night of 2026-10-16
Mamba-in-the-Llama 8B (JunxiongWang/Llama3.1-Mamba2-8B-dpo, env `mil`, 50% Mamba-2 layers, from Llama-3.1-8B-Instruct) done on the
step1 suite (job 1091249, peak 21.3 GiB): needle 1.00 everywhere, many_random 0.52 / 0.48 / 0.12 at 8K / 16K / 32K, many_similar 0.08
from 8K. Comparator meta-llama/Llama-3.1-8B-Instruct (job 1091250) done: 0.96-1.00 on 16 keys at 32K, needle 1.00; the 8B gap opens at 4K (+0.24) and reaches 0.84-0.92 at 32K. See exp01_step1/RESULTS.md addendum. Robust jobs in the exp03 run dir: 1091447 (MIL base), 1091448
(Llama-Instruct base), 1091449 (MIL repair seed 1, TRAIN_LENGTHS="8192 16384", tag -le16k: trains below 32K, so its 32K numbers
are the length-generalisation test, item 3). LoLCATs loader is suspect (probably expects Meta-Llama-3-8B; licence not accepted).

## Next
1. Length generalisation of the repair: train at <=16K, test at 32K/64K.
2. Repair data with multi-hop included; confirm the multi-hop regression disappears.
3. Capacity frontier after repair: 32/64/128 keys at 32K.
4. Scale to a matched 8B pair (LoLCATs or Mamba-in-the-Llama vs Llama-3-8B).
5. Step 2, reshaped by Attention Amnesia (arXiv 2606.11052, which already shows CoT SFT breaks hybrid recall and fixes it by restoring W_Q/W_K): test ordinary (non-CoT) SFT, whether our repair survives it, and whether QK-Restore and the adapter compose.
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
- TRAIN_EXTRA / JOB_ARGS are interpolated unquoted into the job's `bash -c`: never put `|`, `;` or quotes in them (use `[qk]_proj`, not `q_proj|k_proj`).
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

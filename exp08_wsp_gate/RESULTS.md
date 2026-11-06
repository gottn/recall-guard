# Experiment 8: does a training-free weight edit change long-context recall?

**Verdict: pending.** The gate rule and the prediction below were written on 2026-11-06 before any full run; the
Results section is filled in only from `results/raw` by `run_all.sh report`.

## Question
"Sparks of Weight-Space Programming" (Takehi, Teoh, Zhang, Khattab, MIT CSAIL blog, 2026-11-02,
https://rikiyat.github.io/blog/weight-space-programming/, Experiment 8) has an LLM edit Qwen3.5-0.8B's weights directly,
with no training. The LLM traced the model's thinking loops to one direction written by the MLPs of layers 15 and 19, and
subtracted that direction from 64 output columns of `down_proj` in each layer (131,072 weights, 0.016%). The post
reports MATH-500 7.9% -> 48.1%, GSM8K 13.8% -> 67.1% and IFEval 21.0% -> 62.3% with thinking on, and no recall check.
Qwen3.5 is the model class this repo studies: 18 linear-attention layers and 6 full-attention layers (3, 7, 11, 15, 19,
23). The two edited MLPs sit in full-attention blocks. Would `recall-guard check` pass this edit before release?

## Method
- **Checkpoints**: base `Qwen/Qwen3.5-0.8B` @ 2fc0636, edited `RikiyaT/Qwen3.5-0.8B-weight-space-programming` @
  d1671a1 (the model card's rebuild of the post's edit, the full multimodal release). Both have the same config, are
  stored in bfloat16, and load text-only through `AutoModelForCausalLM` in bfloat16 (env `modern`, transformers 5.20).
- **Premise check** (`edit_check.py`, range requests only): both files hold 488 tensors with the same names, dtypes and
  shapes. The two edited tensors match the card's sha256, and each differs from the base in exactly 64 columns of
  `down_proj` (1,024 rows; 1,023 in layer 19). That is 130,188 changed weights out of the 131,072 the edit touches; bf16
  rounding leaves the other 884 unchanged. The other 486 tensors are not byte-compared: the card says they are identical,
  and checking that means downloading both 1.75 GB files.
- **Smoke** (jobs 1152408-09, a T4, the 24-case smoke suite at 1K / 4K): both load with no missing or unexpected weights
  in 18-49 s, at 1.4 GiB. Both get the empty think block, and their 24 completions are identical.
- **Protocol**: the repo's, unchanged: completion prompts, the empty think block prefilled, greedy decoding, 32 new
  tokens (64 for RULER needles). The post measures the edit with thinking on; a retrieval gate answers without it, so
  this tests what the edit does outside the regime it was made for.
- **Runs**: both models get the same jobs, on A40s, at 26d25e8 (the cluster's `origin/main`; no code change since 50ade98).
  - `robust.sbatch STAGE=base`: suites seeds 1 and 2 (the five step1 tasks plus held-out parcels at 16K / 32K, n = 50
    per cell per file), held-out parcels and 25-case multi-hop (n = 25 at each of 1K-32K), six RULER needle variants
    (n = 50 at 16K / 32K), ARC-Easy and HellaSwag (500 each), bits per byte on Moby Dick (8 windows of 16K).
  - `realdocs.sbatch`: exp04 real-document QA, qa_1 and qa_2 at 4K / 16K / 32K, n = 100.
  - `step1.sbatch`: the exp01 suite (five tasks at 1K-32K, n = 25, generated at 8beb29d), the only 1K-8K coverage of
    needle, many_random, many_similar and updated.
  - Commands are in `run_all.sh`.

## Gate rule, pre-registered
- **Primary**: `recall-guard check --baseline <base file> --candidate <edited file>` on six result sets: suite-s1,
  suite-s2, heldout, multihop25, step1, and real QA (the three qa length files as one set). That is one check per file,
  because s1, s2 and step1 reuse case ids and heldout / multihop25 share their 16K / 32K ids with the suites. Alpha is
  0.05 per check: pooled at 0.05, each cell at 0.05 / cells. **The edit loses recall if any primary check fails, in any
  cell or pooled.** Every length is covered by a check. The 4K cells are reported explicitly: heldout_many, multihop
  (25-case file), qa_1, qa_2, and the five step1 tasks.
- **Power**: with no gains, a cell fails at >= 8 lost cases in the suite files (12 cells, n = 50), >= 7 in heldout,
  multihop25 and real QA (6 cells), and >= 10 in step1 (30 cells, n = 25). A cell where the base recalls fewer cases than
  that cannot fail, and is reported as untestable rather than passed.
- **No RULER gate**: the generator repeats case ids within a file, and `check` refuses duplicates. RULER needles are
  read from `tables-ruler.md`, descriptively.
- **Secondary**, not part of the verdict: the reverse check (edited -> base) per file. Its FAIL cells are edited gains.
- **Validity**: the comparison is void if the edit does not reach the forward pass, that is, if bits per byte are
  identical and every completion matches the base's (`run_all.sh` counts identical completions).
- **Cost**: the edit is free on these measures if ARC-Easy and HellaSwag accuracy stay within 0.02 of the base and bits
  per byte within 0.005.

## Prediction, pre-registered
- **P1: every primary check passes.** The edit removes one direction from 128 of the model's 86,016 MLP neurons (64 of
  3,584 in 2 of 24 layers). Our protocol answers in at most 64 tokens with the think block closed, so the loop the edit
  targets never starts. We expect a few discordant pairs per cell, split between losses and gains.
- **P2: cost-free.** Bench within 0.02 and bits per byte within 0.005 of the base.
- **What would refute it**: the post describes the removed direction as the cause of loops, in which the model repeats
  its own earlier text. Recall also works by copying earlier text verbatim. If that direction is part of the copy path,
  losses would appear where copying is hardest: the 16-key cells and multi-hop at 16K / 32K, and RULER multi-value.
  The gate would flag them; MATH-500 and IFEval cannot see them.

## Results
(Filled in from `results/raw` by `run_all.sh report` after the runs.)

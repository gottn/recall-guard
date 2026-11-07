# Experiment 8: does a training-free weight edit change long-context recall?

**Verdict (2026-11-07): the edit loses recall, so the gate blocks it.** Two of the six primary checks fail on the pooled
row: the exp01 suite drops 0.80 -> 0.77 (32 lost / 10 gained, p 0.0005) and suite seed 1 drops 0.75 -> 0.73 (23 / 12,
p 0.045). No single cell fails, and P1 is refuted. RULER, read descriptively outside the gate, shows a larger failure. On
the single needle in a haystack of one repeated passage, the edited model repeats the haystack in 100 of 100 cases ("The
grass is green. The sky is blue. ..."), where the base answers all 100. Multi-value falls 0.40 -> 0.18 at 16K and 0.36 ->
0.16 at 32K. P2 holds (ARC-Easy -0.004, HellaSwag +0.014, bits per byte +0.002). The comparison is valid: 725 of 3,450
completions differ. The gate rule and the prediction below were written on 2026-11-06 before any full run; the Results
section is filled in only from `results/raw` by `run_all.sh report`.

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
Run dirs `~/runs/rg/robust/20261106-105622-26d25e8`, `~/runs/rg/realdocs/20261106-105625-26d25e8` and the exp01 suite's
`~/runs/rg/step1/20261016-121320-8beb29d`, at 26d25e8 on A40s, all COMPLETED: robust 1152442 base / 1152443 edited (1 h 07 min
/ 1 h 01 min), real QA 1152444 / 1152445 (13 min each), step1 1152446 / 1152447 (9 min each). Every number: `run_all.sh
report` (results/tables-*.md, gates.md, and the printed identical-completion count, bench and bits per byte); "a / b" is
cases lost / gained by the edited model in `check`.

### Primary checks (base -> edited)

| check | cases | base | edited | lost / gained | p, pooled | verdict |
|---|---:|---:|---:|---:|---:|---|
| suite-s1 | 600 | 0.75 | 0.73 | 23 / 12 | 0.045 | **FAIL**, pooled |
| suite-s2 | 600 | 0.73 | 0.71 | 21 / 12 | 0.081 | pass |
| heldout | 150 | 0.97 | 0.93 | 6 / 1 | 0.063 | pass |
| multihop25 | 150 | 0.45 | 0.41 | 10 / 4 | 0.090 | pass |
| step1 (exp01 suite) | 750 | 0.80 | 0.77 | 32 / 10 | 0.0005 | **FAIL**, pooled |
| real QA | 600 | 0.56 | 0.55 | 30 / 20 | 0.10 | pass |

- **Losses outnumber gains in all six checks** (122 / 59 in total), but no cell clears its corrected threshold. The largest
  cells: many_similar at 16K (s1 4 / 2, s2 5 / 0) and 32K (s1 5 / 3), held-out at 16K (3 / 0, 3 / 1), multi-hop at 32K
  (s1 3 / 0) and 8K (step1 4 / 1), and updated at 2K and 4K (step1 3 / 0 each). Every lost suite or step1 case still
  answers with a number, a wrong code, so the loss is retrieval, not format. The 4K cells all pass: held-out 1 / 0,
  multihop25 3 / 0, qa_1 3 / 3, qa_2 6 / 1, and in step1 many_random 1 / 0, many_similar 0 / 1, multi-hop 1 / 2, needle
  0 / 0, updated 3 / 0. Four of 72 cells could not fail, because the base recalls fewer cases than a failing cell needs: multi-hop at 8K
  in multihop25 (6 / 25), and at 4K, 8K and 32K in step1 (7-9 / 25).
- **The reverse checks find no gain** in any file (edited -> base passes six of six).

### RULER needles (n = 50 per cell, descriptive: no gate, because the files repeat case ids)

| variant, 16K / 32K | base | edited |
|---|---|---|
| single needle, noise haystack | 1.00 / 1.00 | **0.00 / 0.00** |
| multi-value | 0.40 / 0.36 | **0.18 / 0.16** |
| multikey_1 / multikey_2 | 1.00 / 1.00, 1.00 / 0.94 | 0.98 / 1.00, 0.96 / 0.94 |
| multikey_3 (UUIDs) | 0.20 / 0.36 | 0.28 / 0.40 |
| multi-query | 0.00 / 0.00 | 0.00 / 0.00 |

- All 100 edited answers on the single needle open with the haystack's first sentence. The haystack repeats one
  five-sentence passage, and the edited model continues it instead of answering. Multi-value loses 11 and 10 cases and
  gains none. The exp01 suite's needle, whose filler is varied sentences, stays at 1.00 at every length for both models.

### Cost and validity
- ARC-Easy 0.654 -> 0.650, HellaSwag 0.398 -> 0.412, bits per byte 1.2760 -> 1.2783: P2 holds.
- 2,725 of 3,450 completions are identical (79%); the edit reaches the forward pass.

### Reading
- The refutation reading named RULER multi-value and the hardest copy cells. Multi-value halves, and the pooled losses
  lean to many_similar and multi-hop. The clearest damage lies where the gate's own suites cannot look. In a haystack made
  of one repeated passage, the edit meant to stop thinking loops produces a copy loop, with thinking off.
- `check` blocks the edit on two pooled rows. The strongest evidence, 100 lost and 0 gained on the single needle, sits in
  the RULER files, which `check` refuses.

## Failures and limits
- One greedy run per model; n = 25-100 per cell. The suite-s1 failure is marginal (p 0.045), and s2 passes (p 0.081).
- RULER reads are descriptive: 50 rows per cell, with some case ids repeated within a file.
- The protocol closes the think block, so this does not test the edit in the regime it was made for.
- Only the two edited tensors were byte-compared (Method).

## Next
1. Make RULER gateable: make repeated case ids unique at import (`import-ruler`), so that `check` covers the needle
   variants. It would have flagged the single needle here.

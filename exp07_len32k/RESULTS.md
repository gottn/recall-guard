# Experiment 7: 32K documents at 8B, and the 2B synthetic-only control

**Verdict: pending.** Outcomes below were written on 2026-11-06 before any model ran; the Results section is filled in
only from `results/raw` by `run_all.sh report`.

## Question
Exp06 doubled both halves of the realmix recipe and left two open questions. At 8B every loss sits at 32K, the one length
the gentle recipe never trains on: many_similar 0.97 -> 0.85, multi-hop 0.97 -> 0.89, the 25-case multi-hop file 1.00 ->
0.80, RULER multi-value 0.60 -> 0.56, while real QA gained. At 2B RULER's multi-value and multi-query needles stay 0.20
below the synthetic adapter at 16K, and exp06 cannot tell whether the real half causes this or just twice the
single-answer training. Arm 1 adds 32K documents to the 8B budget recipe; arm 2 trains the 2B on 1,200 synthetic documents
alone, at exp06's step count.

## Method
Exp06's trainer, evaluation and recipes, two changes, one per arm (commands in `run_all.sh`):
- **Arm 1, 8B `-budget32k`**: Mamba-in-the-Llama, 600 documents (300 synthetic + 300 real) at 8K / 16K / 32K instead of
  8K / 16K, lr 5e-5, the exp06 budget recipe otherwise. The length cycle changes which document gets which length, so the
  stream is new (not a continuation of exp06). About 11M tokens; no 8B run has trained at 32K before (peak 24.3 GB at
  16K), so an A40 out-of-memory failure moves the job to an A100.
- **Arm 2, 2B `-syn1200`**: Jet-Nemotron-2B, 1,200 synthetic documents, no real half, lr 2e-4, 8K / 16K / 32K. The stream is
  the exp03 seed-1 stream continued: its first 600 documents are exp03's in the same order, and it has exp06's 300 steps.
  Against exp06 budget (600 synthetic + 600 real, 300 steps) only the real half differs.
- **Code**: the cluster pulls `origin/main` (50ade98), which includes d6523cd, so arm 1's real pool has the 55 SQuAD
  paragraphs (0.3%) that exp05 and exp06 lacked.
- **Evaluation**: unchanged (`robust.sbatch` damage checks, `realdocs.sbatch` real QA). **Comparators**: exp03 base, seed-1
  synthetic and gentle adapters; exp05 realmix; exp06 budget. **Gates**: `check` per file and per real-QA set; no RULER
  gate (repeated case ids), so arm 2 reads `tables-ruler.md`.

## Outcomes, pre-registered
**Arm 1 (8B): does 32K training remove exp06's 32K losses?** Exp03 gentle at 32K: many_similar 0.99, multi-hop 0.99,
held-out 1.00, the 25-case file 1.00, RULER multi-value 0.80. Exp06 budget: 0.85, 0.89, 0.96, 0.80, 0.56.
- **length**: suite many_similar, multi-hop and held-out at 32K >= 0.95; the 25-case file at 32K >= 0.92; RULER
  multi-value at 32K >= 0.74 (gentle less 0.06); and gentle -> budget32k flags no 32K cell.
- **not length**: suite many_similar and multi-hop at 32K both still <= 0.90.
- **mixed**: anything else.
- **C, real QA holds against exp06**: qa_1 at 32K >= 0.75 (0.79 less one SE); budget -> budget32k loses no real-QA cell;
  base -> budget32k loses no 4K cell.
- **D, cost**: ARC-Easy and HellaSwag accuracy within 0.02 of exp06 budget (0.832 / 0.570); bits per byte at most 0.005
  above it (<= 1.058). The bound is no longer exp06's strict "not above": the three exp03 gentle seeds span 1.063-1.083,
  so 0.005 is a quarter of the seed spread.
- Recommendation rule: the budget32k recipe replaces realmix at 8B if the outcome is **length** and C and D hold.

**Arm 2 (2B): the real half or more training?** RULER at 16K (n = 50): exp03 synthetic multi-value 0.68, multi-query
0.62; exp06 budget 0.48 / 0.42.
- **real half**: multi-value and multi-query at 16K both >= 0.62 / 0.56 (exp03 less 0.06). The same 300 steps without
  real documents keep them, so the real half caused exp06's loss.
- **training**: both <= 0.58 / 0.52 (exp03 less 0.10). Single-answer training itself erodes multi-answer recall with
  steps, whatever the data.
- **mixed**: anything else.
- Reported, not criteria: multi-hop against exp03's three-seed floor (suite 0.94 / 0.81 at 16K / 32K), real QA against the
  exp03 synthetic adapter (qa_1 at 32K 0.26), bits per byte against exp03 seed 1 (1.0862), and the failure-shape readout.

Expectation, not a criterion: **length** for arm 1, because every exp06 8B loss sits at the untrained length; qa_2 at 32K
should also rise (exp05: two-hop moved only inside the training lengths). None for arm 2.

## Results
Pending: run dirs, job ids and tables once the jobs finish (`run_all.sh report`).

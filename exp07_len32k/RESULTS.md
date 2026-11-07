# Experiment 7: 32K documents at 8B, and the 2B synthetic-only control

**Verdict (2026-11-07, one seed per arm): mixed in both arms, and neither change can be told apart from seed noise.**
Arm 1 (8B, 32K documents): at 32K many_similar 0.98, held-out 0.99 and the 25-case file 0.96 clear the "length" bars, while
multi-hop 0.94 (bar 0.95) and RULER multi-value 0.64 (bar 0.74) miss them. C holds (qa_1 at 32K 0.80, no real-QA cell lost).
D fails on bits per byte (1.069 against 1.058), with bench within 0.004. By the rule budget32k does not replace realmix.
Arm 2 (2B, 1,200 synthetic documents): multi-value at 16K is 0.56, on the "training" side, and multi-query 0.58, on the
"real half" side, so mixed. Reported: the same 300 steps without real documents cost real QA (qa_1 at 4K 0.70 -> 0.44, the
base -> syn1200 gate fails) and keep multi-hop (0.96 at 32K). Seeds 2 and 3 of the budget adapter (exp06, run the same
week) already reach these levels. At 8B they have many_similar 0.94 / 0.99 and multi-hop 0.94 / 0.99 at 32K. At 2B they
have multi-value 0.82 / 0.70 and multi-query 0.56 / 0.60 at 16K. Both arms were measured against budget seed 1, and most of
its losses belonged to that seed. Outcomes below were written on 2026-11-06 before any model ran; the Results section is
filled in only from `results/raw` by `run_all.sh report`.

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
Run dirs `~/runs/rg/robust/20261106-103327-50ade98` (training and damage checks) and `~/runs/rg/realdocs/20261106-103336-50ade98`
(real QA), at 50ade98 on A40s, all COMPLETED: 1152402 Mamba-in-the-Llama (7 h 47 min; training 2 h 24 min: 600 documents, 150
steps, 11.4M tokens, 1,328 tok/s, peak 32.8 GB, so no A100 was needed; final loss 0.29), 1152404 Jet (6 h 58 min; training
3 h 53 min: 1,200 documents, 300 steps, 22.9M tokens, 1,638 tok/s, final loss 0.00), 1152405 / 1152406 real QA (48 / 30 min).
Every number: `run_all.sh report` (results/tables-qa.md, tables-damage.md, tables-multihop25.md, tables-ruler.md, gates.md,
and the printed bench, bits per byte and failure-shape lines); "a / b" is cases lost / gained by the candidate in `check`.
Budget seeds 2 and 3 come from exp06's report.

### Arm 1: 8B with 32K documents (suite n = 100 per cell from s1 + s2; the 25-case file n = 25; RULER n = 50)

| at 32K | gentle (exp03) | budget (exp06), seeds 1 / 2 / 3 | **budget32k** | "length" bar |
|---|---:|---|---:|---:|
| many_similar | 0.99 | 0.85 / 0.94 / 0.99 | **0.98** | >= 0.95 |
| multi-hop | 0.99 | 0.89 / 0.94 / 0.99 | **0.94** | >= 0.95 |
| held-out | 1.00 | 0.96 / 0.96 / 0.99 | **0.99** | >= 0.95 |
| 25-case multi-hop file | 1.00 | 0.80 / 0.92 / 1.00 | **0.96** | >= 0.92 |
| RULER multi-value | 0.80 | 0.56 / 0.66 / 0.86 | **0.64** | >= 0.74 |

- **Mixed.** Two of the five bars miss. "Not length" needed many_similar and multi-hop both at or below 0.90. Gentle ->
  budget32k flags no 32K cell but fails pooled on s1 (7 / 1, p 0.035) and s2 (11 / 2, p 0.011): budget32k sits 0.01-0.02
  below gentle across the suite. Budget32k beats budget seed 1 (budget32k -> budget flags many_similar at 32K on s1, 8 / 0),
  but every budget32k cell lies inside the budget seeds' range.
- **C holds.** qa_1 at 32K is 0.80 (bar 0.75; budget 0.79, Llama 0.83). Budget -> budget32k passes every real-QA cell.
  Base -> budget32k passes, with qa_1 at 4K 0.86 -> 0.92 (2 / 8) and qa_2 at 4K 0.51 -> 0.61 (6 / 16). The expected qa_2
  rise at 32K is 0.47 -> 0.53, inside the budget seeds' 0.47-0.53.
- **D fails.** ARC-Easy 0.834 and HellaSwag 0.566 sit within 0.004 of budget (0.832 / 0.570). Bits per byte are 1.0687
  against the 1.058 bound, inside the budget seeds' 1.043-1.081.

### Arm 2: 2B on 1,200 synthetic documents (RULER n = 50; suite and real QA n = 100)

| cell | synthetic, 600 documents (exp03 seed 1) | budget (exp06), seeds 1 / 2 / 3 | **syn1200** |
|---|---:|---|---:|
| RULER multi-value 16K (real half >= 0.62, training <= 0.58) | 0.68 | 0.48 / 0.82 / 0.70 | **0.56** |
| RULER multi-query 16K (real half >= 0.56, training <= 0.52) | 0.62 | 0.42 / 0.56 / 0.60 | **0.58** |
| multi-hop suite 16K / 32K | 0.97 / 0.89 | 0.84 / 0.87, 0.62 / 0.49, 0.68 / 0.61 | **1.00 / 0.96** |
| qa_1 4K / 16K / 32K | 0.67 / 0.42 / 0.26 | 0.82 / 0.72 / 0.45 (seed 1) | **0.44 / 0.27 / 0.12** |
| bits per byte | 1.0862 | 1.0901 / 1.0921 / 1.0888 | **1.0873** |

- **Mixed.** Multi-value lands on the training side and multi-query on the real-half side. None of the failures at 16K
  lists at most one number (0 of 22, 0 of 21; budget seed 1 1 of 26, 3 of 29). The synthetic seeds span 0.48-0.70 and
  0.36-0.62 in these cells, and the budget seeds 0.48-0.82 and 0.42-0.60. A one-seed control cannot separate the readings.
- **Real QA falls with synthetic-only steps.** Base -> syn1200 fails pooled (114 / 36) and at 4K: qa_1 0.70 -> 0.44 (33 / 7,
  p 2e-5) and qa_2 0.50 -> 0.27 (26 / 3). Synthetic -> syn1200, the same stream 300 steps earlier, fails five of six cells
  (qa_1 at 32K 0.26 -> 0.12, 15 / 1). 74 of 100 qa_1 answers at 4K open with a digit, against 38 at 600 documents, 5 for
  the base and 18-20 for the budget seeds. This is exp03 seed 2's code-answer prior, growing with synthetic-only steps.
- **Multi-hop is better than any synthetic seed** (0.94-0.97 / 0.81-0.89), and the 25-case file holds 0.96 or more at every
  length. The damage gates on the synthetic files pass against base, synthetic and budget. Bench equals synthetic seed 1
  (0.776 / 0.492), and bits per byte are +0.001.

## Failures and limits
- One seed per arm. The budget seeds swing 0.1-0.3 between seeds in exactly the cells both arms were designed around. Arm
  1's document stream is new by design (the length cycle reassigns documents), so it is effectively a new seed too.
- D's 0.005 bound is smaller than the budget seeds' bits-per-byte spread (0.038).
- The expectation "length" for arm 1 missed on two bars. RULER cells hold 50 cases (1 SE 0.07), and no RULER gate exists
  (repeated case ids).

## Next
1. Compare recipes on three seeds per arm, using seed means and ranges. One-seed differences in multi-hop, RULER and the
   8B 32K cells sit inside the seed spread.
2. Three findings survive three seeds: the real-QA gain of a real half, at both scales; Jet's chained-key loss with a real
   half (five of six adapters at or below 0.61 at 32K); and the real-QA erosion from synthetic-only steps (exp03 seed 2,
   syn1200). The open question is which part of the real half costs the second hop of chained keys.

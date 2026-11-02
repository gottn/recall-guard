# Experiment 6: the full synthetic dose plus the real half

**Verdict: pending.** Outcomes A-D below were written on 2026-11-02 before any model ran; the Results section is filled in
only from `results/raw` by `run_all.sh report`.

## Question
Exp05 put real-document QA into half the repair mix at an unchanged budget. Single-document recall rose at both scales
(qa_1 at 32K 0.12 -> 0.44 at 2B, 0.19 -> 0.72 at 8B, no 4K cost), but Jet-Nemotron-2B's chained-key multi-hop suite fell
from 0.97 / 0.89 to 0.65 / 0.45 at 16K / 32K and RULER's multi-value and multi-query needles lost 0.12-0.20 in five cells
across both models. Two readings compete. **Dose**: the synthetic half got half its exp03 documents, and chained or
multi-answer retrieval needs the full count. **Prior**: SQuAD-style real QA teaches a single-span answer habit that
suppresses those tasks whatever the synthetic dose. Exp06 restores the full synthetic dose and keeps the real half: if
the losses come back, it was dose; if they stay, it was the real data.

## Method
Exp05's trainer, generator, evaluation and recipes; only the document counts double (`TRAIN_DOCS`, both halves):
Jet-Nemotron-2B 1,200 documents (600 synthetic + 600 real) at 8K / 16K / 32K, lr 2e-4; Mamba-in-the-Llama 8B the gentle
recipe with 600 documents (300 + 300) at 8K / 16K, lr 5e-5; LoRA r 16, alpha 32, grad_accum 4, `--real-dir
~/data/rg/realqa --exclude-dir ~/data/rg/ruler-qa`; tag `-budget`. Commands in `run_all.sh`.

- **Streams.** The trainer indexes both streams by j = i // 2 and seeds each document by j, so the first 600 (2B) / 300
  (8B) documents are exactly exp05's, in the same order; exp06 is exp05 continued at the same constant learning rate for
  as many steps again (2B 150 -> 300 steps, 8B 75 -> 150), on the next synthetic documents and new real ones. The
  synthetic half is exactly the exp03 seed-1 stream (600 documents at 2B, the 300 gentle ones at 8B); the real half
  extends exp05's. So "dose" here means synthetic training received, not count at a fixed number of steps.
- **Code.** Jobs run at 8b5abb6, the commit exp05 ran at (the cluster pulls `origin/main`), so the real-document
  generator is exp05's byte for byte, including the 55 SQuAD paragraphs (0.3%) that d6523cd later restored.
- **Evaluation**, unchanged: `infra/slurm/robust.sbatch` (STAGE=repair) trains, then runs the exp03 damage checks
  (suites seeds 1 and 2 at 16K / 32K, n = 100 per cell; held-out parcels; 25 multi-hop cases at each of 1K-32K; six RULER
  needle variants at 16K / 32K, n = 50; ARC-Easy and HellaSwag, 500 each; bits per byte on Moby Dick at 16K; unmerged and
  chat checks); `infra/slurm/realdocs.sbatch` runs the exp04 real-QA cases (qa_1, qa_2 at 4K / 16K / 32K, n = 100).
- **Comparators** (no new runs): exp03 seed-1 synthetic adapters (Jet seeds 1-3 for the multi-hop range), exp05 realmix
  adapters, exp04 base rows. **Gates**: `recall-guard check` per file and per real-QA set, base -> budget, synthetic ->
  budget, realmix -> budget, and budget -> realmix (its FAIL cells are budget gains); no RULER gate (the generator repeats
  case ids, `check` refuses them), so B reads `tables-ruler.md`.
- **Time.** At exp05's measured A40 rates: 2B about 23M tokens, 4.3 h of training (1,480 tok/s); 8B about 7.4M tokens,
  1.4 h (1,430 tok/s). Both jobs get 12 h (exp05's 2B job took 5 h 22 min with 2 h 09 min of training).

## Outcomes, pre-registered
**A. Jet chained-key multi-hop.** Exp03, three seeds: suite 0.94-0.97 at 16K and 0.81-0.89 at 32K, stale 0.03-0.06 and
0.11-0.19; the 25-case file >= 0.84 at every length (its floor, 32K). Exp05: 0.65 / 0.45, stale 0.35 / 0.55, the 25-case
file 0.56-0.72.
- **dose**: >= 0.84 in every multi-hop cell (suite at 16K and 32K; the 25-case file at 1K, 2K, 4K, 8K, 16K, 32K) and the
  suite stale rate back in exp03's range (<= 0.06 at 16K, <= 0.19 at 32K).
- **prior**: suite multi-hop <= 0.65 at both 16K and 32K, every failure stale.
- **mixed**: anything else, reported as the recovered share of exp05's loss per suite cell, (exp06 - exp05) / (exp03
  seed 1 - exp05).

A stale answer (a wrong chain's code) does not separate the readings: every exp03 multi-hop failure was stale too, so the
levels decide. The 8B lost nothing here in exp05 (0.99 / 0.97); its multi-hop cells are a no-loss check.

**B. RULER multi-value and multi-query**, the five cells exp05 lost by >= 0.10 against the synthetic adapter (n = 50; Jet's
32K cells sit at 0.02-0.06 for every adapter and are left out):

| model | cell | synthetic (exp03) | realmix (exp05) |
|---|---|---:|---:|
| Jet-Nemotron-2B | multiquery 16K | 0.62 | 0.48 |
| Jet-Nemotron-2B | multivalue 16K | 0.68 | 0.52 |
| Mamba-in-the-Llama | multiquery 16K | 0.94 | 0.82 |
| Mamba-in-the-Llama | multivalue 16K | 0.88 | 0.70 |
| Mamba-in-the-Llama | multivalue 32K | 0.80 | 0.60 |

- **dose**: every cell of the model within 0.06 (about 1 SE at n = 50) of the synthetic adapter, or above it.
- **prior**: every cell of the model still >= 0.10 below the synthetic adapter.
- **mixed**: anything else.

Readout, not a criterion: a single-span answer lists at most one number. In these cells 5 of exp05's 94 failures do so
(synthetic adapter 0 of 54); most list three of four values. `run_all.sh report` prints the count.

**C. Real QA holds**, both models: qa_1 at 32K >= 0.40 (2B) and >= 0.68 (8B), exp05's 0.44 / 0.72 less one SE; realmix ->
budget loses no real-QA cell; base -> budget loses no 4K cell.

**D. No added cost**: ARC-Easy and HellaSwag accuracy within 0.02 of exp05 (2B 0.780 / 0.498, 8B 0.838 / 0.582); bits per
byte on Moby Dick at 16K not above exp05's (2B 1.0861, 8B 1.0561).

Verdict rule: per model, name the A outcome (2B) and the B outcome, then whether C and D hold. A recipe is recommended only
if C and D hold. What each outcome means: **dose**, the halves do not conflict and the budget recipe (both halves at full
dose, twice the training) replaces realmix; **prior**, the real half itself suppresses chained and multi-answer retrieval and
the fix is in the real data (a HotpotQA-only half, or multi-answer real questions), not in budget; **mixed**, both act and
the next step is a synthetic-dose sweep at a fixed real half; dose with C failing means more synthetic training erodes the
real gains, so the halves compete after all. Expectation, not a criterion: dose on A, because exp03's replay runs lost
multi-hop (0.30-0.36) when natural text displaced synthetic documents; none on B.

## Results
Pending: run dirs, job ids and tables once the jobs finish (`run_all.sh report`).

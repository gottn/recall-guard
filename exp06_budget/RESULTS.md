# Experiment 6: the full synthetic dose plus the real half

**Verdict (2026-11-06, one seed per model): dose explains most of the chained-key loss, not the multi-answer loss at 2B,
and the 8B pays at 32K.** Jet-Nemotron-2B: A **mixed, mostly dose**. Multi-hop at 32K goes 0.45 -> 0.87, back inside
exp03's 0.81-0.89 (95% of exp05's loss recovered). At 16K it goes 0.65 -> 0.84 (59%, stale 0.16 against the 0.06 bar),
and the 25-case file stays below 0.84 at 2K and 32K (0.68, 0.72). B **prior**: multi-value and multi-query at 16K stay
0.20 below the synthetic adapter (0.48 / 0.42, no better than exp05) with twice the synthetic training. C holds (qa_1 at
32K 0.45; realmix -> budget loses no cell). D fails narrowly: bits per byte 1.0901 against exp05's 1.0861, bench within
0.01. Mamba-in-the-Llama 8B: B **mixed**, dose inside the training lengths: both 16K cells return to the synthetic
adapter (multi-query 0.94, multi-value 0.86), while multi-value at 32K falls further (0.56). C holds and gains: qa_1 at 32K
0.72 -> 0.79 (Llama 0.83), qa_2 at 4K 0.54 -> 0.64 (Llama 0.67). D holds (bits per byte 1.053 < 1.056). But the 8B's no-loss
check fails at 32K, beyond its 8K-16K training lengths: many_similar 0.97 -> 0.85, multi-hop 0.97 -> 0.89 (synthetic ->
budget flags many_similar@32K, 8 / 0). By the pre-registered rule no recipe is recommended at either scale: D fails at 2B,
and at 8B C and D hold but the 32K damage gate fails. Outcomes A-D below were written on 2026-11-02 before any model ran;
the Results section is filled in only from `results/raw` by `run_all.sh report`.

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
Run dirs `~/runs/rg/robust/20261102-145806-8b5abb6` (training and damage checks) and `~/runs/rg/realdocs/20261102-145814-8b5abb6`
(real QA), at 8b5abb6 on A40s, all COMPLETED: 1138457 Jet (8 h 55 min; training 4 h 02 min: 1,200 documents, 300 steps, 23.0M
tokens, 1,581 tok/s, final loss 0.22), 1138458 Mamba-in-the-Llama (6 h 58 min; training 1 h 24 min: 600 documents, 150 steps,
7.4M tokens, 1,460 tok/s, final loss 0.26), 1138459 / 1138460 real QA (47 / 48 min). Step-1 losses equal exp05's (0.613, 1.591),
as the shared streams predict. The generated case files are byte-identical to exp05's (cmp on the cluster) and were not pulled.
Every number: `run_all.sh report` (results/tables-qa.md, tables-damage.md, tables-multihop25.md, tables-ruler.md, gates.md, and
the printed bench, bits per byte and failure-shape lines); "a / b" is cases lost / gained by the candidate in `check`.

### A. Jet chained-key multi-hop (suite n = 100 per cell from s1 + s2; the 25-case file n = 25 per length)

| adapter | suite 16K | suite 32K | stale 16K / 32K | 1K | 2K | 4K | 8K | 16K | 32K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| exp03 synthetic, seed 1 | 0.97 | 0.89 | 0.03 / 0.11 | 1.00 | 0.96 | 0.96 | 0.92 | 1.00 | 0.84 |
| exp03 seeds 1-3 | 0.94-0.97 | 0.81-0.89 | 0.03-0.06 / 0.11-0.19 | 1.00 | 0.96 | 0.96-1.00 | 0.88-0.92 | 1.00 | 0.84-0.92 |
| exp05 realmix | 0.65 | 0.45 | 0.35 / 0.55 | 0.68 | 0.56 | 0.72 | 0.60 | 0.64 | 0.72 |
| **exp06 budget** | **0.84** | **0.87** | **0.16 / 0.13** | **1.00** | **0.68** | **0.96** | **0.84** | **0.88** | **0.72** |

- **Mixed.** Dose needed >= 0.84 in all eight cells and stale <= 0.06 / 0.19. It holds on the 32K suite cell (0.87, stale
  0.13) and on 16K recall (0.84, exactly at the bar), and misses on 16K stale (0.16) and on the 25-case file at 2K (0.68) and
  32K (0.72). Prior needed <= 0.65 at both suite lengths. Recovered share of exp05's loss: 59% at 16K, 95% at 32K, 67% on the
  25-case file pooled (0.65 -> 0.85; exp03 0.95).
- The gains over exp05 pass the gate: budget -> realmix flags multi-hop at 16K and 32K on s1 (13 / 1, 24 / 1), at 32K on s2
  (20 / 1) and the 25-case file pooled (36 / 7, p 4e-6). Against the synthetic adapter a gap remains: synthetic -> budget
  fails pooled on s1 (13 / 5, p 0.048; multi-hop at 16K 7 / 0) and on the 25-case file (18 / 3, p 7e-4; 2K 8 / 1); s2 and
  held-out pass. Every suite failure is stale, as in exp03 and exp05. The other synthetic tasks stay >= 0.99.

### B. RULER multi-value and multi-query (n = 50 per cell)

| model | cell | synthetic (exp03) | realmix (exp05) | budget (exp06) | outcome |
|---|---|---:|---:|---:|---|
| Jet-Nemotron-2B | multiquery 16K | 0.62 | 0.48 | **0.42** | -0.20, prior |
| Jet-Nemotron-2B | multivalue 16K | 0.68 | 0.52 | **0.48** | -0.20, prior |
| Mamba-in-the-Llama | multiquery 16K | 0.94 | 0.82 | **0.94** | 0.00, dose |
| Mamba-in-the-Llama | multivalue 16K | 0.88 | 0.70 | **0.86** | -0.02, dose |
| Mamba-in-the-Llama | multivalue 32K | 0.80 | 0.60 | **0.56** | -0.24, prior |

- Jet: **prior**, both cells as far below the synthetic adapter as before. 8B: **mixed**, the two 16K cells back, the 32K
  cell below exp05. Readout: 7 of the 87 budget failures in these cells list at most one number (exp05 5 of 94, synthetic
  0 of 54). The failures are lists missing one of the four values, not single-span answers.
- Other variants: Jet multikey_1 0.86 / 0.72 at 16K / 32K (synthetic 0.92 / 0.84, realmix 0.76 / 0.76), UUID multikey_3
  0.78 / 0.22 (0.58 / 0.18, 0.88 / 0.30). 8B multikey_1 0.92 / 0.92 (1.00 / 0.96), multi-query at 32K 0.74 (0.76, 0.84).
  The single needle is 1.00 everywhere.

### C. Real QA (exp04 cases, n = 100 per cell)

| task | model | 4K | 16K | 32K |
|---|---|---:|---:|---:|
| qa_1 | Jet-Nemotron-2B / + realmix / **+ budget** | 0.70 / 0.79 / **0.82** | 0.39 / 0.75 / **0.72** | 0.12 / 0.44 / **0.45** |
| qa_2 | Jet-Nemotron-2B / + realmix / **+ budget** | 0.50 / 0.54 / **0.51** | 0.28 / 0.46 / **0.44** | 0.27 / 0.36 / **0.43** |
| qa_1 | Mamba-in-the-Llama / + realmix / **+ budget** | 0.86 / 0.91 / **0.92** | 0.65 / 0.80 / **0.81** | 0.19 / 0.72 / **0.79** |
| qa_2 | Mamba-in-the-Llama / + realmix / **+ budget** | 0.51 / 0.54 / **0.64** | 0.34 / 0.47 / **0.49** | 0.35 / 0.40 / **0.47** |
| qa_1 / qa_2 | Llama-3.1-8B-Instruct (source) | 0.92 / 0.67 | 0.82 / 0.64 | 0.83 / 0.57 |

- **Holds at both scales.** qa_1 at 32K is 0.45 (bar 0.40) and 0.79 (bar 0.68). Realmix -> budget passes every cell (2B
  pooled 36 / 39, 8B 19 / 47). Base -> budget passes, with the 4K cells explicit: 2B qa_1 0.70 -> 0.82 (7 / 19) and qa_2
  0.50 -> 0.51 (12 / 13); 8B 0.86 -> 0.92 (3 / 9) and 0.51 -> 0.64 (6 / 19). Synthetic -> budget passes at both scales.
- The 8B gains from the doubled real half: budget -> realmix fails pooled (47 / 19, p 4e-4). qa_2 at 4K (13 / 3, p 0.011),
  qa_1 at 32K (9 / 2) and qa_2 at 32K (10 / 3) lead, though no single cell flags after correction. Two-hop at 4K now sits
  0.03 below Llama.

### D. Cost (ARC-Easy and HellaSwag acc, n = 500, SE 0.022; bits per byte on Moby Dick at 16K)

| model | base | synthetic (exp03) | realmix (exp05) | budget (exp06) |
|---|---|---|---|---|
| Jet-Nemotron-2B | 0.764 / 0.508 / 1.0821 | 0.776 / 0.492 / 1.0862 | 0.780 / 0.498 / 1.0861 | **0.774 / 0.490 / 1.0901** |
| Mamba-in-the-Llama | 0.848 / 0.600 / 1.0079 | 0.842 / 0.586 / 1.0651 | 0.838 / 0.582 / 1.0561 | **0.832 / 0.570 / 1.0530** |

- 2B: bench within 0.01 of exp05, but bits per byte rise 0.004 above exp05 (+0.7% over base against +0.4%), so **D fails**.
  8B: bench within 0.012 and bits per byte below exp05, so **D holds** (acc_norm 0.786 / 0.726 against realmix's 0.780 / 0.736).

### 8B synthetic recall at 32K (the no-loss check; suite n = 100 per cell)

| suite task, 16K / 32K | gentle (exp03) | realmix (exp05) | budget (exp06) |
|---|---:|---:|---:|
| many_random | 1.00 / 1.00 | 0.99 / 1.00 | 0.97 / 0.97 |
| many_similar | 1.00 / 0.99 | 0.96 / 0.97 | 0.97 / **0.85** |
| multihop (25-case file at 32K) | 1.00 / 0.99 (1.00) | 0.99 / 0.97 (1.00) | 0.95 / **0.89** (**0.80**) |
| heldout_many | 0.99 / 1.00 | 0.99 / 0.98 | 1.00 / 0.96 |

- **Fails at 32K.** Synthetic -> budget fails s1 (pooled 23 / 1, p 1.5e-6; many_similar@32K 1.00 -> 0.84, 8 / 0, flagged),
  s2 (23 / 2) and the 25-case file (7 / 0, five of them at 32K). Realmix -> budget fails the same three files pooled. Needle and
  updated stay >= 0.98 and every 16K cell >= 0.95. The gentle recipe trains at 8K and 16K only. Twice the steps there cost
  synthetic recall at 32K, while real QA at 32K improves.
- Variants (n = 50 at 32K): 8B unmerged 0.84-1.00, chat template 0.82-1.00. Jet unmerged 0.84-1.00, and Jet chat 0.00
  everywhere, as for every Jet adapter.

### Reading
- **The chained-key loss was mostly dose.** Twice the synthetic training brings 32K multi-hop back into exp03's seed range
  while the real half doubles too. A prior learned from that half would have held it near 0.45. The 16K and 2K cells lag
  (0.84, 0.68), so dose is not the whole story.
- **The multi-answer loss at 2B is not dose.** Both 16K cells stay 0.20 below the synthetic adapter after twice the
  synthetic training. The failures are lists one value short, not single answers, so "prior" here means the loss rides on
  the real half or on total single-answer training, not a single-span habit. This design doubles both, so it cannot tell
  them apart.
- **At 8B the 16K multi-answer cells came back** (dose). Everything that got worse sits at 32K, outside the training
  lengths: more steps at 8K-16K trade synthetic 32K recall for real-QA gains.

## Failures and limits
- Expectation "dose on A" held at 32K and missed at 16K and on the 25-case file at 2K and 32K. The 8B no-loss check, not an
  outcome, failed at 32K.
- One seed per model. n = 100 per real-QA and suite cell, 25 per length on the multi-hop file, 50 per RULER cell (1 SE
  0.06-0.07).
- Budget doubles both halves and the step count at a constant learning rate. "Dose" therefore means synthetic training
  received, and B at 2B cannot separate the real half from more single-answer training.
- RULER files repeat case ids, so there is no RULER gate; B reads 50-row table means. The 2B bench is a single run (two runs
  of the exp05 adapter differed by up to 0.006).
- exp05's 8 h limit would have killed the Jet job (8 h 55 min): runs with 1,200 documents need the 12 h limit.

## Next
1. 32K documents in the 8B recipe (8K / 16K / 32K at budget counts): every 8B loss here sits at 32K, outside the training
   lengths.
2. Separate the real half from total training on 2B multi-answer RULER: 1,200 synthetic documents alone against budget.
   If that recovers multi-value / multi-query, the real data is the cause, and the next step is a multi-answer real half.
3. Seeds 2 and 3 of the budget adapter on the 16K multi-hop and RULER cells.

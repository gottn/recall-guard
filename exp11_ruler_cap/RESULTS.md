# Experiment 11: 2B RULER multi-answer recall without the 64-token cap

**Verdict (2026-11-08): the cap explains few misses, and the real half's multi-value cost at 2B is "small" (+0.13), with
the seeds overlapping.** P1 is refuted: 12 of the 142 misses whose last line was an unfinished list item become correct at
192 tokens, and only 6 of the 12 keep the stored output as their prefix. Past the values it retrieved, Jet keeps listing: it
cycles through the same values or counts down round numbers or years, so a list still running at the cap was already a
miss. V fails: 1,695 of 2,200 new outputs (77%) begin with the stored one, so by the rule the arms are compared on the new
runs only. There, synthetic minus realmix on multi-value at 16K is +0.13 (synthetic 0.72 / 0.74 / 0.56, realmix 0.52 /
0.62 / 0.48), between "no cost" (<= 0.08) and "cost" (>= 0.15), with no complete separation. exp05's "P4(b) is not
established", exp06's per-seed B outcomes and exp07's arm 2 reading stand. The expectation ("cost") was wrong. The
predictions below were written on 2026-11-07 before any run; the Results section is filled in only from `results/raw` by
`run_all.sh report`.

## Question
Every RULER needle run in this repo stops after 64 new tokens (`robust.sbatch`). A multi-value answer lists four 7-digit
values after a one-sentence preamble, and a multi-query answer lists one value for each of four keys. When the preamble is
long, the cap can cut the list off before the last value, and the case is scored as missed even though the model was
still listing values it had retrieved. In the stored outputs, a miss counts as cut off when its last line is an unfinished
list item.

On the 2B models such cut-off misses are common for the synthetic adapters and rare for the real-half ones. On the 8B
models there are none: their misses end before the cap, so a longer cap cannot change them. exp05 (P4(b)), exp06
(outcome B) and exp07 (arm 2) compared these cells across recipes, so the cap biased those comparisons against the
synthetic arm. Does the real half cost 2B multi-answer recall once the cap is lifted?

## Method
- **Cases.** The stored RULER multi-value and multi-query cases, unchanged: the exp03 suites
  `~/data/rg/ruler/ruler-{16384,32768}.jsonl`, filtered to the two tasks into `~/data/rg/ruler-mvmq/ruler-mvmq.jsonl`
  (200 lines kept byte for byte, n = 50 per cell, sha256 f0ddab0152f83713...; the command is in `run_all.sh`).
- **Models.** Jet-Nemotron-2B base and its ten stored adapters: exp03 synthetic seeds 1-3, exp05 realmix seeds 1-3,
  exp06 budget seeds 1-3, and exp07 syn1200. No new training.
- **Decoding.** `--max-new-tokens 192`; everything else as stored (greedy, completion prompt, empty think block, scoring).
- **Jobs.** `step1.sbatch` through `infra/cluster/submit.sh`, one run dir per variant whose `suite.jsonl` links to the
  filtered file, with `JOB_ARGS="--max-new-tokens 192 --adapter <dir>"`. They run on A40s at origin/main 3e4d01f; no code
  change is needed.
- **Validity.** With greedy decoding and the same prompt, the new output should begin with the stored 64-token output.
  If fewer than 90% of cases match, GPU nondeterminism between the original runs (exp03 on A100s) and these runs
  dominates. The comparison then uses only the new runs, which cover every arm, and the 64-token numbers are not compared.

## Baseline, at 64 tokens (stored outputs; score / cut-off misses, n = 50 per cell)

| variant | multi-value 16K | multi-query 16K | multi-value 32K | multi-query 32K |
|---|---|---|---|---|
| base | 0.24 / 0 | 0.08 / 0 | 0.02 / 0 | 0.00 / 0 |
| synthetic seeds 1 / 2 / 3 | 0.68 / 9, 0.70 / 15, 0.48 / 7 | 0.62 / 3, 0.50 / 9, 0.36 / 7 | 0.06 / 8, 0.08 / 11, 0.22 / 0 | 0.06 / 1, 0.02 / 2, 0.08 / 5 |
| realmix seeds 1 / 2 / 3 | 0.52 / 1, 0.62 / 4, 0.48 / 0 | 0.48 / 0, 0.40 / 6, 0.48 / 0 | 0.02 / 0, 0.10 / 2, 0.06 / 0 | 0.04 / 0, 0.06 / 0, 0.06 / 0 |
| budget seeds 1 / 2 / 3 | 0.48 / 3, 0.82 / 4, 0.70 / 0 | 0.42 / 0, 0.56 / 3, 0.60 / 1 | 0.00 / 0, 0.04 / 5, 0.08 / 0 | 0.00 / 0, 0.08 / 12, 0.08 / 0 |
| syn1200 | 0.56 / 9 | 0.58 / 11 | 0.14 / 0 | 0.16 / 4 |

At 64 tokens, the synthetic-minus-realmix gap in the seed means at 16K is 0.08 for multi-value and 0.04 for multi-query.
If every cut-off miss turned correct, the gaps would be 0.25 and 0.13.

## Predictions, pre-registered
- **V (mechanical).** At least 90% of new outputs begin with the stored output, and no case that was not cut off changes
  its verdict.
- **P1.** At least half of the cut-off misses become correct at 192 tokens: the lists were cut mid-enumeration of
  retrieved values.
- **Outcome, from the 2B multi-value gap at 16K (synthetic seed mean minus realmix seed mean, at 192 tokens):**
  - **cost**: >= 0.15;
  - **no cost**: <= 0.08 (the 64-token value);
  - **small**: anything in between.
- **Reported, not criteria:** the same gap for multi-query; budget and syn1200 against synthetic; the 32K cells; whether
  the seeds separate completely (3 above 3, the strongest result three seeds can give, rank test p = 0.05); and the seed
  spread at 192 against 64 tokens.
- **What follows.** Dated notes in exp05, exp06 and exp07 RESULTS.md point here. On "cost", exp05's "P4(b) is not
  established" and exp06's per-seed B outcomes are replaced by the 192-token numbers; on "no cost", they stand.

Expectation, not a criterion: P1 holds and the outcome is "cost" (0.15-0.25). The seeds will not separate completely:
synthetic seed 3 can reach at most 0.62, which is realmix seed 2's score already. So with three seeds the cost is an
effect size, not a seed-level test.

## Results
Jobs 1155277-1155287 ran on A40s at 3e4d01f and all COMPLETED on 2026-11-08 (started 05:50-08:34, 33 min to 1 h 07 min
each); run dirs `~/runs/rg/rescore/20261107-ruler192/<variant>`. Every number: `run_all.sh report` (results/tables-192.md
and the printed readout).

| prediction | rule | result | |
|---|---|---|---|
| V | >= 90% of new outputs begin with the stored one; no other verdict changes | 77% (1,695 / 2,200); 54 other changes | **fails** |
| P1 | >= half of the 142 cut-off misses become correct | 12 (8%), 6 on the stored path | **refuted** |
| outcome | synthetic - realmix, multi-value 16K, 192 tokens: cost >= 0.15, no cost <= 0.08 | +0.13 | **small** |

### Scores at 192 tokens (n = 50 per cell; the 64-token scores are in the baseline table)

| variant | multi-value 16K | multi-query 16K | multi-value 32K | multi-query 32K |
|---|---|---|---|---|
| base | 0.22 | 0.16 | 0.02 | 0.00 |
| synthetic seeds 1 / 2 / 3 | 0.72, 0.74, 0.56 | 0.60, 0.52, 0.50 | 0.08, 0.10, 0.22 | 0.06, 0.02, 0.12 |
| realmix seeds 1 / 2 / 3 | 0.52, 0.62, 0.48 | 0.48, 0.50, 0.50 | 0.02, 0.08, 0.02 | 0.04, 0.02, 0.06 |
| budget seeds 1 / 2 / 3 | 0.48, 0.82, 0.70 | 0.44, 0.62, 0.60 | 0.02, 0.10, 0.08 | 0.00, 0.12, 0.08 |
| syn1200 | 0.56 | 0.58 | 0.12 | 0.12 |

Seed means at 16K (sd), in three readings:

| reading | multi-value: synthetic / realmix / budget | synthetic - realmix | multi-query: synthetic / realmix / budget | synthetic - realmix |
|---|---|---:|---|---:|
| stored, 64 tokens | 0.62 (0.12) / 0.54 (0.07) / 0.67 (0.17) | +0.08 | 0.49 (0.13) / 0.45 (0.05) / 0.53 (0.09) | +0.04 |
| new runs, 192 tokens (the outcome) | 0.67 (0.10) / 0.54 (0.07) / 0.67 (0.17) | +0.13 | 0.54 (0.05) / 0.49 (0.01) / 0.55 (0.10) | +0.05 |
| stored, cap lifted on the stored path | 0.65 / 0.54 / 0.67 | +0.11 | 0.53 / 0.49 / 0.55 | +0.04 |

No reading separates the synthetic seeds from the realmix seeds. Synthetic against budget is -0.01 to +0.01 at 192 tokens.

### Where the verdicts changed
"Stored path": the new output begins with the stored one, so only the cap changed. "Diverged": the new run left the stored
greedy path, at a median of 23-63 characters into the answer, within the first value or two.

| change | multi-value | multi-query |
|---|---:|---:|
| cut-off miss -> correct, stored path | 3 | 3 |
| cut-off miss -> correct, diverged | 2 | 4 |
| other miss -> correct, stored path | 4 | 19 |
| other miss -> correct, diverged | 8 | 5 |
| correct -> miss, diverged | 8 | 10 |
| correct -> miss, stored path | 0 | 0 |

- **The cap cost 29 of 2,200 runs**, the stored-path gains: 22 multi-query, 7 multi-value. Most are multi-query answers
  that name each key before its value (`4. **Odd-criticism**: 154`, base at 16K), so the cut line holds text and the
  last-line test missed it.
- **The 142 flagged misses were mostly real**: 130 still miss at 192 tokens. Past the retrieved values the lists go on
  with the same values in a cycle (8077999, 9997381, 8526486, 9997381, ...), round numbers counting down (4000000,
  2000000, 1000000, 500000, ...) or years (2001, 2003, 1995, 1994, ...); all three from synthetic seed 1 at 16K.
- **Reruns diverge.** 505 of 2,200 outputs leave the stored path. The exp03 runs, stored from A100s, keep 123-144 of 200;
  the exp05-07 runs, stored from A40s like these, keep 164-172. Divergence moved 37 verdicts, 19 up and 18 down. `cli run`
  decodes one case at a time, so batching is not the cause; GPU nondeterminism and a compute path that depends on the
  token limit are not told apart here.
- **Seed spread** at 16K, sd at 64 / 192 tokens: multi-value synthetic 0.12 / 0.10, realmix 0.07 / 0.07, budget 0.17 /
  0.17; multi-query synthetic 0.13 / 0.05. The spread, not the cap, still decides these comparisons.
- **32K**: every variant stays at 0.00-0.22 under both caps. syn1200 is unchanged at 16K (0.56 / 0.58).

### Reading
- The cap did not hide the synthetic adapters' multi-answer recall. Lifting it moves the multi-value gap from +0.08 to
  +0.11 on the stored path and +0.13 on the new runs, short of the 0.15 that counts as a cost, and three seeds per arm
  overlap.
- P1's premise was wrong. The last-line test took a model that keeps listing after its last retrieved value for a cut
  answer. A cap shows only by re-decoding with the stored output as prefix.

## Failures and limits
- V failed, so 64 against 192 tokens is read only on the stored path, and the arms are compared on the new runs: one greedy
  run per variant.
- n = 50 per cell, three seeds per arm. A 0.13 gap with seed sd 0.07-0.10 is an effect size, not a test.
- The cause of the divergence is not identified.

## Next
1. **Rerun noise.** Decode one adapter at 64 tokens on an A40 (realmix seed 2, 200 cases, about 35 min) and compare it with
   its stored run. 200 / 200 identical means the token limit changes the compute path; fewer means reruns at 16K-32K are
   noisy by themselves. `check` compares two runs, and here 37 of 2,200 verdicts moved with no change to the model, so the
   gate needs that noise floor.
2. Decode RULER's multi-answer needles with 192 tokens in later runs. The cap costs little (29 of 2,200), but it costs it
   where answers name their keys.

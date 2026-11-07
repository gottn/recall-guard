# Experiment 11: 2B RULER multi-answer recall without the 64-token cap

**Verdict: pending.** The predictions below were written on 2026-11-07 before any run; the Results section is filled in
only from `results/raw` by `run_all.sh report`.

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
Pending: job ids, then `run_all.sh report`.

# Experiment 10: is the weight edit's recall damage separable from its loop fix?

**Verdict: pending; nothing has run.** Written on 2026-11-07 before any job. The variants, measures, rules and odds
below are fixed. The Results section is filled in only from `results/raw` by `run_all.sh report`, whose
`summary.py` applies the rules; a dry run on exp08's files as stand-ins reproduces exp08's gate (122 lost / 59 gained).

## Question
Exp08 found that the weight-space-programming edit of Qwen3.5-0.8B (`RikiyaT/Qwen3.5-0.8B-weight-space-programming`)
loses recall where the input repeats itself. On RULER's single needle in a haystack of one repeated passage, the
edited model continues the haystack in 100 of 100 cases, where the base answers all 100. In the synthetic suites, 67 of
76 lost cases answer with a real but wrong code from the document. Single-occurrence retrieval is untouched. The edit
was found and measured on MATH-500, GSM8K and IFEval with thinking on, and none of these repeats its input. Is the
damage the price of the advertised loop fix (one mechanism, a trade-off frontier)? Or does a partial edit keep the fix
without the damage (separable)? Exp08's hypothesis: the edited direction helps the model track its position within
repeated structure, and the edit trades that bookkeeping for the loop fix.

## Premise checks, before any run (`premise.py`, no GPU)
1. **The edit does not remove the direction; it reverses it five-fold.** In each layer the change touches 64 columns
   of `down_proj` and is rank one: the first singular value holds 0.999995 (layer 15) and 0.999991 (layer 19) of its
   squared norm. In every one of those columns, the component along the change's direction u becomes -5.00 times the
   base's (layer 15: -5.0073 to -4.9976; layer 19: -5.0062 to -4.9911; bfloat16 rounding). On those columns the
   edit is W - 6 u uᵀ W. The two layers' directions have cosine 0.85, and the change is 0.106 and 0.081 of each tensor's
   norm. The post says the editor subtracted the direction, and exp08 repeated that wording; the published weights write
   -5 times it instead. On the line W(a) = W_base + a (W_edit - W_base), the edited columns' component is c = 1 - 6a times
   the base's. So a = 1/6 is the removal the post describes (c = 0), a = 1/3 a reflection (c = -1), and a = 1 the
   published edit (c = -5). A grid of a = 0, 0.25, 0.5, 0.75, 1 would skip the removal and start at c = -0.5, so the
   dose axis here is c.
2. **Exp08's multi-value loss is mostly its 64-token cap.** All 21 lost multi-value cases (11 at 16K, 10 at 32K, none
   gained) list three of the four values. 19 end at the cap with the fourth cut off, and 2 (at 16K) stop after three
   values. In 19 of the 21, the edited model writes the key in bold (`**dirty-stress**`), which spends the tokens the
   fourth value needed. The base's own misses end in a cut-off number in 58 of 62. So at 64 tokens RULER's
   multi-value task mostly measures answer length. Exp10 reruns it with 192 new tokens; until then, exp08's
   multi-value drop (0.40 -> 0.18) is not a recall result.
3. **The echo is real.** All 100 edited single-needle answers open with the haystack's first sentence, and none
   contains a seven-digit number.
4. **Two traps in the loop measure** (the model's tokenizer configuration). Qwen3.5-0.8B's chat template writes an
   empty think block unless `enable_thinking` is true. The checkpoint ships no generation config, so `generate` stops
   only at `<|endoftext|>`, while a chat answer ends with `<|im_end|>`. Without both fixes, no answer would think, or
   every finished answer would count as hitting the limit. `loops` passes both.

## Design
**Variants**: nine jobs on the base `Qwen/Qwen3.5-0.8B` (`infra/slurm/exp10.sbatch`, one A40 each, no training).
The edited tensors are read from the published checkpoint.

| tag | change to `down_proj` of layers 15 and 19 | c in 15 / 19 | gate sets |
|---|---|---|---|
| c1 | none (the base) | 1 / 1 | exp08's base run |
| c0 | a = 1/6 | 0 / 0 (removal) | run here |
| cm1 | a = 1/3 | -1 / -1 (reflection) | run here |
| cm3 | a = 2/3 | -3 / -3 | run here |
| cm5 | a = 1, through the same patch | -5 / -5 (published) | exp08's edited run |
| cm5-L15 | a = 1 in layer 15 only | -5 / 1 | run here |
| cm5-L19 | a = 1 in layer 19 only | 1 / -5 | run here |
| cm5-prompt | a = 1 while reading the prompt only | -5 / -5, then 1 / 1 | not run |
| cm5-answer | a = 1 while generating only | 1 / 1, then -5 / -5 | not run |

The patch (`--restore-from`, `restore.apply`) sets W + a (W_edit - W) in float32 and rounds to bfloat16. On the real
tensors, a = 1 reproduces the published weights bit for bit, and a = 0.16666667 / 0.33333333 / 0.66666667 give c =
-0.0000 / -1.0004 / -3.0004. The phase variants keep the base weights and add a (W_edit - W) x through a forward hook.
The hook acts on calls over several positions (reading the prompt) or on calls over one position (each generated
token). The first answer token comes from the prompt's last position, so it belongs to the reading phase.

**Measures, in every variant**
- *Damage, the echo* (E): RULER's single needle in the noise haystack, from exp08's file at 16K (n = 50, 49 unique ids).
  It uses 192 new tokens and exp08's protocol otherwise: completion prompt, empty think block, greedy decoding. Echo =
  no answer, and "The grass is green." in the completion. Recall and "echo, then the answer" are reported too.
- *Item count*: RULER multi-value at 16K (n = 50) with 192 new tokens. Reported: the share with all four values, and
  the mean number of values found over the 46 unique ids.
- *Haystack sweep* (`haystack.py`, `generate --cells`; seed 10, n = 50 per cell, 16K, 192 new tokens, RULER's
  template). One needle in each of five haystacks: p1, p5 and p50 repeat 1, 5 or 50 noise sentences in a fixed order
  (p5 is RULER's haystack); r50 deals the same 50 in a fresh order every cycle (repeated, no period); filler is office
  text with no repeats. The filler haystack also holds k = 2, 4 and 8 values for one key. One-value cells share their
  needles case by case, so the haystack is the only difference between them. Echo = `stale`: the answer is missing
  and a haystack sentence is present. Case ids are unique, so `check` gates each cell.
- *Benefit, the loops* (H): MATH-500 (`HuggingFaceH4/MATH-500`), the first 20 problems of each level (100 in all), with
  thinking on. Decoding uses the post's sampling: temperature 0.6, top-p 0.95, top-k 20 and presence penalty 1.5,
  applied in vLLM's order. One sample per problem, 16,384 new tokens, batches of 50 sorted by prompt length, seed 0
  plus the batch offset. H is the share of answers that hit the limit, the post's own measure: in its MATH-500 table,
  93.0% (base) and 33.1% (edited) at 32,768 tokens with four samples. Also reported: accuracy (the last boxed answer
  after the think block, exact match after light normalisation, a lower bound) and the tokens used.
- *Gate* (G, for the five weight variants run here): `check` from exp08's base run to the variant on exp08's six
  primary sets (suite-s1, suite-s2, heldout, multihop25, step1, real QA). Protocol and rule are exp08's: any FAIL, pooled
  or in a cell, means recall is lost.

## Rules, pre-registered
- **V1, reproduction**: in at least 98 of 100 cases, the needle answers of c1 and cm5 must start with exp08's base and
  edited answers (the first 64 of 192 tokens). Otherwise the patch or the hardware departs from exp08: exp08's gate
  files then stand in for neither, and their rows are marked not comparable.
- **V2, the benefit is measurable**: H(c1) - H(cm5) >= 0.20 with paired exact McNemar p < 0.01 (n = 100). Otherwise
  the fix does not show under this protocol: separability is not answered, and the damage curves are reported alone.
- **V3, the damage is measurable**: E(cm5) - E(c1) >= 0.5 (exp08: 1.00).
- Shares for every variant v: benefit β(v) = (H(c1) - H(v)) / (H(c1) - H(cm5)); damage δ(v) = (E(v) - E(c1)) /
  (E(cm5) - E(c1)).
- **Outcome**, if V2 and V3 hold:
  - **Separable by weights**: a weight variant other than cm5 has β >= 0.75 and δ <= 0.25, and passes the gate. A
    partial edit then keeps three quarters of the fix with at most a quarter of the echo.
  - **Separable by phase only**: no weight variant does, but cm5-prompt or cm5-answer has β >= 0.75 and δ <= 0.25.
    That is not a weight edit, but it shows the two effects act in different phases.
  - **One mechanism**: every variant has δ >= β - 0.25, so no partial edit buys the fix ahead of the damage.
  - **Mixed**: none of these. Either a variant beats the frontier by more than 0.25 without reaching the corner, or it
    reaches the corner and fails the gate.
- **Locus of the echo**: reading if E(cm5-prompt) >= 0.5 and E(cm5-answer) <= 0.1, answering if the reverse,
  otherwise both or neither.
- **What the echo needs** (the sweep at cm5). First the anchor: p5 must echo in >= 0.8 of cases and the base in <=
  0.1 (RULER's file: 1.00 and 0.00); otherwise the sweep is descriptive only. Then: an exact period if p50 >= 0.5 and
  r50 <= 0.1; repetition without a period if r50 >= 0.5; a short period if p1 or p5 >= 0.5 and p50 <= 0.1. Filler is
  expected at <= 0.05.
- **List tracking**: lost if `check` c1 -> cm5 fails a filler k = 2, 4 or 8 cell (with no gains, 8 or more of 50
  lost); otherwise no deficit.
- **Truncation reading of exp08's multi-value loss**: holds if cm5's all-four rate at 192 tokens is within 0.06 (3
  cases) of c1's.

## Prediction, pre-registered
- **Odds: separable by weights 0.20, separable by phase only 0.10, one mechanism 0.35, mixed 0.20, and no answer
  (V2 or V3 fails) 0.15.**
- *For one mechanism*: the editor wrote -5 times the direction, not the removal it describes. That suggests weaker
  edits did not stop the loops, so the fix may need the same strong reversal that causes the damage. Both behaviours
  involve text that repeats: the model's own trace, and the haystack.
- *For separable*: the two layers' directions are not the same (cosine 0.85) and their columns differ, so one layer
  may carry the fix and the other the damage. The two effects also pull in opposite directions (fewer loops, more
  copying), which fits two circuits better than one.
- Locus: reading 0.45, answering 0.35, both or neither 0.20. What the echo needs: an exact period 0.35, repetition
  without a period 0.30, a short period 0.25, none of them 0.10. List tracking: no deficit 0.75. Truncation reading
  holds: 0.90.
- Exp08's bookkeeping hypothesis predicts an echo that needs a period (exact or short), a locus in reading, and a list
  deficit. An echo on r50, or a locus in answering, counts against it.

## Runs
- All jobs at one commit, on A40s through `submit.sh`, with the commands in `run_all.sh`. Two smoke jobs run first, in
  a run dir of their own and at tiny sizes: the published edit through the patch, and the generation-only hook. The
  nine variants then run in one run dir, each `--dependency=afterok` on both smokes.
- Expected time at exp08's rates (about 30 ms per generated token at batch 1, 0.75 s to read 16K tokens): needles
  10 min, sweep 30 min, loops 25 min, gate 55 min. That is about 2.2 h for a gated variant, 1.2 h otherwise, and 15
  A40-hours in all.
- Pull with the lines at the top of `run_all.sh`. The case files (the sweep, RULER's 16K file) go to the git-ignored
  `results/cases/` for the item counts; `run_all.sh report` prints their sha256.

## Limits
- One sample per problem at half the post's budget, so our hit rate at 16,384 tokens is not the post's at 32,768. The
  decision uses shares against our own base and published edit, both measured the same way.
- The recall measures use greedy decoding with the think block closed, as in exp08. The loop measure samples with
  thinking on. Each effect is measured under the protocol in which it was found.
- With n = 50 per needle cell and 100 problems, each share carries about ±0.1.
- The phase split is not a weight edit. Its hook adds the change in bfloat16 next to the base output instead of
  folding it into the weights.
- RULER's file repeats case ids, so its rows are descriptive; the sweep asks the same questions with unique ids.
- The sweep is our generator, not NVIDIA's; the p5 anchor ties it to RULER's file.

## Next
- Exp08 RESULTS.md needs a dated post-hoc note on premises 1 and 2 (the reversal, and the multi-value cap). It is
  left as written here, because it belongs to exp08.

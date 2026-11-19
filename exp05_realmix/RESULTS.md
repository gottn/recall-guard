# Experiment 5: real-document QA in the repair mix

**Verdict (2026-11-02, one seed per model): real QA in the mix closes the single-document gap at both scales and turns the
4K cost into a gain; two-hop moves at 16K but not at 32K; the price is paid by the halved synthetic dose.** P1 holds and is
larger than predicted: qa_1 at 32K goes 0.12 -> 0.44 at 2B (the synthetic adapter reached 0.26, the Qwen source sits at 0.36)
and 0.19 -> 0.72 at 8B (gentle 0.56, Llama 0.83); synthetic -> realmix passes every cell at both scales. P3 holds: no 4K cell
lost, and the gentle adapter's 0.05 cost on qa_1 at 4K becomes +0.05 (0.86 -> 0.91). P2 holds at 16K (8B qa_2 0.34 -> 0.47)
and fails at 32K (0.35 -> 0.40); two-hop at 2B moves more than predicted (+0.08 to +0.13). P4 fails in two of four parts:
Jet's chained-key multi-hop suite drops from 0.97 / 0.89 to 0.65 / 0.45 at 16K / 32K and RULER's multi-value and multi-query
needles lose 0.12-0.20 in three cells per model; the other synthetic tasks stay >= 0.96, ARC / HellaSwag and bits per byte are
unchanged (Jet 1.086 = synthetic adapter; 8B 1.056 against gentle's 1.065). Reading, as pre-registered for a P4 failure: the two
halves compete for one dose, so the next lever is budget, not a split. Predictions P1-P4 below were written on 2026-10-26 before
any model ran; the Results section is filled in only from `results/raw` by `run_all.sh report`.

**Seeds 2 and 3 (2026-11-07, after the verdict):** P1 holds at every seed (8B qa_1 at 32K 0.72 / 0.78 / 0.78 against the gentle
seeds' 0.56 / 0.64 / 0.56; 2B 0.44 / 0.47 / 0.48), and Jet's multi-hop loss replicates (0.45 / 0.49 / 0.57 at 32K against
0.81-0.89 for the synthetic seeds). P4(b)'s RULER loss does not: the realmix seeds sit inside the synthetic adapters' own seed
range. Section "Seeds 2 and 3".

**exp11 (2026-11-08):** these RULER multi-answer cells were decoded with 64 new tokens. Re-decoded at 192
(exp11_ruler_cap/RESULTS.md), the cap explains 29 of 2,200 runs, mostly multi-query, and synthetic minus realmix on
multi-value at 16K is +0.13, the pre-registered "small", with the seeds overlapping. P4(b) stays not established.

**Control (2026-11-18):** the same recipe lifts the Qwen source as much as Jet (qa_1 0.45 -> 0.76 at 16K, 0.36 -> 0.76 at
32K). The real-QA gain above is what this training gives any model, and "closes the single-document gap" holds only against
the untrained source: after equal training the 2B gap at 32K is 0.28-0.32, against 0.24 before. Section "Control".

**Control at 8B (2026-11-19):** the same recipe lifts Llama-3.1-8B-Instruct by 0.05-0.07 on qa_1 (0.97 / 0.89 / 0.90).
After equal training the 8B gap at 32K is 0.12-0.18, against 0.64 before, and the gate fails there for all three seeds:
at 8B too, "closes the single-document gap" holds only against the untrained source. Counted on the first line of the
output only, one seed of three fails. Section "Control at 8B".

## Question
Exp04 left three things open. The adapter trained only on synthetic key lists repairs 58% of the single-document gap at
32K at both scales (Jet 0.12 -> 0.26 against Qwen2.5-1.5B at 0.36; Mamba-in-the-Llama 0.19 -> 0.56 against Llama-3.1-8B
at 0.83); it leaves the 8B two-hop deficit untouched (qa_2 0.36 vs 0.57 at 32K, and 0.51 vs 0.67 already at 4K); and the
8B gentle adapter costs 0.05 on single-document QA at 4K. Every training document so far was filler text with planted
six-digit codes. Does adding real-document QA to the training mix close the remaining 42% of the single-document gap
and the 8B two-hop deficit, without raising the 4K cost and without losing what the synthetic mix repairs?

## Method
Training data (`recall_guard/real_data.py`, pure; tests in `tests/test_real_data.py`): long documents made of real
Wikipedia paragraphs in exactly RULER's QA framing (the `qa` template, `Document i:` blocks, ` Answer:`), up to eight
real questions per document, loss on the answer tokens only. Sources are the SQuAD v2 **train** split and the HotpotQA
**train** split, fetched once on the cluster into `~/data/rg/realqa` (`fetch_data.sh`; never into the repo). Exp04
evaluates on SQuAD v2 dev and HotpotQA dev-distractor, so the splits are disjoint by construction; in addition every
paragraph and question of the 600 evaluation prompts is removed from the training pools by exact string before
anything is sampled (`disjoint`; the trainer logs how many were removed). A SQuAD document holds the asked questions'
gold paragraphs among the other paragraphs of their article, a HotpotQA document the questions' two gold paragraphs
among their eight natural distractors, then random paragraphs from the rest of the pool up to the length budget,
shuffled and numbered as RULER does. Lengths 8K-32K as the recipe's length cycle gives them.

Mix: every other training document is real (alternating SQuAD and HotpotQA), the rest the synthetic v2 mix
(random / similar / updated / multi-hop), each stream keeping its own seed and length cycle, so the synthetic half is
the first half of the exp03 stream unchanged. Recipes are the exp03 seed-1 ones, so the data is the only variable:
Jet-Nemotron-2B 600 documents at 8K/16K/32K, lr 2e-4; Mamba-in-the-Llama the gentle recipe, 300 documents at 8K/16K,
lr 5e-5; both LoRA r = 16, alpha 32, on every linear projection outside the MLPs, gradient accumulation 4.

Evaluation, one training job and one QA job per model:
- `infra/slurm/robust.sbatch` STAGE=repair with `TRAIN_TAG=-realmix` trains the adapter, then runs the exp03 damage
  checks: synthetic suites seeds 1 and 2 at 16K/32K (n = 100 per cell), held-out parcels, 25 multi-hop cases, the six
  RULER needle variants at 16K/32K (n = 50), ARC-Easy and HellaSwag (500 each), bits per byte on Moby Dick at 16K, and
  the unmerged-adapter and chat-template checks.
- `infra/slurm/realdocs.sbatch` with `ADAPTER=` the new adapter runs the exp04 cases: qa_1 and qa_2 at 4K/16K/32K,
  n = 100 per cell, the same 100 questions at every length, rule `any`, 32 new tokens.

Comparators (no new runs): exp04 base, source and seed-1 synthetic adapters (`repair-seed1` for Jet,
`repair-seed1-gentle` for Mamba-in-the-Llama) for real QA; exp03 base and the same adapters for the damage checks.
Verdict rule: `recall-guard check` (exact one-sided McNemar on shared case ids, per cell and pooled, alpha 0.05 split
over the cells) in both directions: base -> realmix and synthetic -> realmix must lose no cell; the reverse directions
name the cells where realmix gains. n = 100 per real cell: 1 SE is about 0.04-0.05, a cell trips at about ten lost
cases with none gained.

## Predictions
- **P1, the remaining single-document gap closes.** On qa_1 at 32K the realmix adapter reaches at least 80% of the
  base-to-source gap: Jet >= 0.31 (base 0.12, synthetic adapter 0.26, source 0.36), Mamba-in-the-Llama >= 0.70 (0.19,
  0.56, 0.83). `check --baseline synthetic --candidate realmix` passes at every length; the reverse fails qa_1@32K at 8B
  (>= 14 net cases). At 2B the predicted +0.05 is under the gate's power, so the reverse 2B check passes with realmix
  ahead by 5-10 cases.
- **P2, two-hop moves at 8B, not at 4K.** qa_2 at 16K and 32K: realmix >= 0.45 (base 0.34 / 0.35, gentle 0.38 / 0.36,
  Llama 0.64 / 0.57), at least +0.10 over base, and the gentle -> realmix reverse check flags at least one of the two
  cells. At 4K the two-hop deficit is a conversion cost that 8K-16K training does not target: realmix <= 0.59, less than
  half of the 0.16 gap. At 2B both models sit near floor on qa_2 at 16K/32K (0.28-0.39): realmix within 0.05 of the
  synthetic adapter in every qa_2 cell.
- **P3, no 4K cost.** At 4K the realmix adapter is within 1 SE (0.05) of its base on both tasks at both scales and
  base -> realmix loses no 4K cell; at 8B qa_1 at 4K >= 0.83 (base 0.86, gentle 0.81). Mechanism: the gentle adapter's
  4K cost is answer-format drift (every training answer was a six-digit code); real spans in half the mix remove it.
- **P4, nothing lost elsewhere.** (a) Synthetic suites at 32K, n = 100: random, similar and updated >= 0.95, multi-hop
  and held-out >= 0.85 for both models (exp03 synthetic adapters: Jet 1.00 / 1.00 / 1.00 / 0.89 / 0.98, gentle
  1.00 / 0.99 / 1.00 / 0.99 / 1.00); synthetic -> realmix on the suites flags at most multi-hop (half the multi-hop
  documents). (b) RULER needle variants within 0.10 of the synthetic adapter in every cell (n = 50). (c) ARC-Easy and
  HellaSwag within 0.02 of base. (d) Bits per byte on Moby Dick at 16K not above the synthetic adapter's (Jet 1.086
  against base 1.082; gentle 1.065 against base 1.008): natural text in half the documents, even with loss only on the
  answers, should not add to the long-text cost.

What each outcome means. P1 false (realmix within noise of the synthetic adapter at 32K): the remaining gap is not
data coverage but capacity (few surviving attention layers, state size) or the source's own ceiling, and the next lever
is architectural (which layers, qk-only), not data. P2 false: the 8B two-hop deficit is a conversion cost in the
reasoning path that HotpotQA-style supervision through LoRA does not reach; report it as a limit of post-hoc repair.
P3 false (the 4K cost persists): the cost comes from adapting every projection, not from the synthetic answer format,
and qk-only stays the recommendation where short context matters. P4 false (synthetic recall or RULER needles fall):
the two halves compete for one dose, as natural-text replay did in exp03, and the fix is a larger budget, not a split.

## Results
Run dirs `~/runs/rg/robust/20261101-183230-8b5abb6` (training and damage checks) and `~/runs/rg/realdocs/20261101-183233-8b5abb6`
(real QA on the exp04 cases), all at 8b5abb6 on A40s: 1136480 Jet (5 h 22 min, of which training 2 h 09 min: 600 documents, 150
steps, 11.5M tokens, final loss 0.38, 1,480 tok/s), 1136481 Mamba-in-the-Llama (7 h 32 min; training 43 min: 300 documents, 75
steps, 3.7M tokens, final loss 0.30, 1,430 tok/s), 1136482 / 1136483 real QA (30 / 62 min), 1136505 Jet finisher (19 min, nothing
left to evaluate). Comparators: the exp04 base and source rows and the exp03 seed-1 synthetic adapters (Jet `repair-seed1`, 8B
`repair-seed1-gentle`) on the same cases. Every number: `run_all.sh report` (results/tables-qa.md, tables-damage.md,
tables-ruler.md, gates.md); n = 100 per real-QA cell; "a / b" is cases lost / gained by the candidate, p the one-sided exact
McNemar p of `check` (Bonferroni over the seven cells of a gate).

### Real QA, 2B (Jet-Nemotron-2B, 600 documents: 300 real + 300 synthetic)

| task | model | 4K | 16K | 32K |
|---|---|---:|---:|---:|
| qa_1 | Qwen2.5-1.5B (source) | 0.69 | 0.45 | 0.36 |
| qa_1 | Jet-Nemotron-2B | 0.70 | 0.39 | 0.12 |
| qa_1 | + synthetic adapter (exp03) | 0.67 | 0.42 | 0.26 |
| qa_1 | + realmix adapter | **0.79** | **0.75** | **0.44** |
| qa_2 | Qwen2.5-1.5B (source) | 0.50 | 0.39 | 0.32 |
| qa_2 | Jet-Nemotron-2B | 0.50 | 0.28 | 0.27 |
| qa_2 | + synthetic adapter (exp03) | 0.46 | 0.33 | 0.28 |
| qa_2 | + realmix adapter | **0.54** | **0.46** | **0.36** |

- **P1 holds, beyond the prediction.** Base -> realmix passes (no cell lost; pooled 33 / 141). qa_1 at 32K 0.12 -> 0.44 (2 / 34)
  against the predicted >= 0.31: 133% of the base-to-source gap, so the repaired hybrid now passes its own source (0.36; source ->
  realmix 17 / 25, p 0.92, not flagged). At 16K 0.39 -> 0.75 (2 / 38), 0.30 above the source. Synthetic -> realmix passes every
  cell (pooled 32 / 124); the reverse, predicted to pass at 2B, fails pooled (p 3e-14), on qa_1 at 16K (36 / 3, p 2e-8) and at
  32K (23 / 5, p 5e-4).
- **P2 at 2B: two-hop moves, against the prediction of "within 0.05".** qa_2 0.28 -> 0.46 at 16K (8 / 26) and 0.27 -> 0.36 at
  32K (7 / 16), +0.08 to +0.13 over the synthetic adapter (realmix -> synthetic on qa_2 at 16K 20 / 7, p 0.0096, just outside the
  corrected threshold), and above the source in every qa_2 cell (0.46 vs 0.39, 0.36 vs 0.32).
- **P3 holds.** At 4K nothing is lost: qa_1 0.70 -> 0.79 (6 / 15), qa_2 0.50 -> 0.54 (8 / 12); the synthetic adapter's 4K drift
  (-0.03 / -0.04 in exp04) is gone. The +0.09 on qa_1 exceeds the pre-registered "within 0.05" upward.

### Real QA, 8B (Mamba-in-the-Llama, gentle recipe, 300 documents: 150 real + 150 synthetic)

| task | model | 4K | 16K | 32K |
|---|---|---:|---:|---:|
| qa_1 | Llama-3.1-8B-Instruct (source) | 0.92 | 0.82 | 0.83 |
| qa_1 | Mamba-in-the-Llama | 0.86 | 0.65 | 0.19 |
| qa_1 | + gentle adapter (exp03) | 0.81 | 0.76 | 0.56 |
| qa_1 | + realmix adapter | **0.91** | **0.80** | **0.72** |
| qa_2 | Llama-3.1-8B-Instruct (source) | 0.67 | 0.64 | 0.57 |
| qa_2 | Mamba-in-the-Llama | 0.51 | 0.34 | 0.35 |
| qa_2 | + gentle adapter (exp03) | 0.50 | 0.38 | 0.36 |
| qa_2 | + realmix adapter | **0.54** | **0.47** | **0.40** |

- **P1 holds.** qa_1 at 32K 0.19 -> 0.72 (1 / 54), the predicted >= 0.70: 83% of the 0.64 gap, against 58% for the gentle
  adapter. Gentle -> realmix passes every cell (pooled 36 / 83); the reverse fails on qa_1 at 32K (20 / 4, p 8e-4; 16 net, the
  predicted >= 14) and pooled (p 1e-5). The remaining deficit to Llama on qa_1 is 0.11 at 32K (17 / 6, p 0.017, not flagged)
  and 0.01-0.02 at 4K and 16K.
- **P2 holds at 16K and fails at 32K.** qa_2 at 16K 0.34 -> 0.47 (7 / 20; the predicted >= 0.45 and >= +0.10); at 32K 0.35 ->
  0.40 (8 / 13), under both bounds. The reverse flags neither cell (16K 14 / 5, p 0.03 uncorrected). At 4K 0.54, inside the
  predicted <= 0.59. Source -> realmix still fails every qa_2 cell (15 / 2, 22 / 5, 22 / 5): the two-hop deficit, 0.13-0.17,
  remains. The gentle recipe trains at 8K and 16K only, and the one qa_2 cell that moved is the one inside the training lengths.
- **P3 holds, with the predicted mechanism.** qa_1 at 4K 0.86 -> 0.91 (3 / 8), the gentle adapter's -0.05 reversed; qa_2 at 4K
  0.51 -> 0.54 (8 / 11). Realmix -> gentle flags qa_1 at 4K (12 / 2, p 0.006): real answer spans in half the mix remove the
  format drift that six-digit answers caused.

### Damage checks (exp03 suites and RULER; n = 100 per suite cell from s1 + s2, 50 per RULER cell)

Recall at 16K / 32K, synthetic adapter against realmix adapter:

| suite task | Jet synthetic | Jet realmix | 8B gentle | 8B realmix |
|---|---:|---:|---:|---:|
| needle | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 | 1.00 / 1.00 |
| many_random | 1.00 / 1.00 | 1.00 / 0.99 | 1.00 / 1.00 | 0.99 / 1.00 |
| many_similar | 1.00 / 1.00 | 1.00 / 0.97 | 1.00 / 0.99 | 0.96 / 0.97 |
| updated | 1.00 / 1.00 | 1.00 / 0.98 | 1.00 / 1.00 | 1.00 / 1.00 |
| heldout_many | 1.00 / 0.98 | 0.99 / 0.97 | 0.99 / 1.00 | 0.99 / 0.98 |
| multihop | 0.97 / 0.89 | **0.65 / 0.45** | 1.00 / 0.99 | 0.99 / 0.97 |

- **P4(a) holds at 8B and fails at 2B on multi-hop.** Base -> realmix passes every suite file at both scales (8B pooled 2 / 398
  on s1). 8B: every task >= 0.96; synthetic -> realmix fails pooled on s1 only (10 / 1, p 0.006; no cell beyond -0.04) and passes
  s2, held-out and multihop25. Jet: five tasks >= 0.97, but chained-key multi-hop falls to 0.65 / 0.45 (s1 19 / 0 and 25 / 1, s2
  14 / 1 and 20 / 0, all p <= 5e-4) and on the multihop25 file at every length from 1K (0.95 -> 0.65 pooled, 47 / 3, p 2e-11).
  The prediction allowed multi-hop to be flagged but required >= 0.85. The realmix adapter sees 300 synthetic documents where
  the exp03 adapter saw 600, and at 2B the chained-key task is the one that needs the full dose; the 8B recipe halves its
  synthetic dose too (150) and loses nothing, so capacity, not the data, sets the dose.
- **P4(b) fails at both scales: RULER's multi-value and multi-query needles drop, UUID keys improve.** Beyond the pre-registered
  0.10 (first occurrence of each case id; `check` refuses these files because the generator repeats 10 / 4 ids per file, as in
  exp03): Jet at 16K multikey_1 0.92 -> 0.76 (8 / 0, p 0.004), multiquery 0.62 -> 0.48 (17 / 10), multivalue 0.70 -> 0.54
  (11 / 4, p 0.06); 8B multiquery 0.94 -> 0.82 at 16K (7 / 1, p 0.035), multivalue 0.91 -> 0.74 at 16K (9 / 1, p 0.011) and
  0.81 -> 0.64 at 32K (11 / 3, p 0.03). Gains on multikey_3 (UUID keys), the task the synthetic mix never transferred to: Jet
  0.60 -> 0.89 at 16K (2 / 15) and 0.18 -> 0.31 at 32K, 8B 0.31 -> 0.43 at 32K (3 / 9). Single-needle and multikey_1-2 at 8B
  are unchanged (>= 0.94).
- **P4(c) holds on accuracy; the 8B normalised cost equals gentle's.** ARC-Easy / HellaSwag (acc, n = 500, SE 0.022): Jet
  0.764 / 0.508 -> 0.780 / 0.498; 8B 0.848 / 0.600 -> 0.838 / 0.582, all within 0.02. acc_norm at 8B 0.804 / 0.778 -> 0.780 /
  0.736, the same drop as the gentle adapter (0.766 / 0.744).
- **P4(d) holds.** Bits per byte on Moby Dick at 16K: Jet 1.0861 against the synthetic adapter's 1.0862 (base 1.0821); 8B 1.0561
  against gentle's 1.0651 (base 1.0079): natural text in half the documents takes back a sixth of the long-text cost.
- Variants (n = 50 at 32K): the 8B adapter unmerged 0.96-1.00 and under the chat template 0.92-1.00; Jet's chat variant is 0.00
  everywhere, as for every Jet adapter in exp03 (the harness has no chat template for it).

## Failures and limits
- Mispredicted: P2 at 32K (8B qa_2 0.40, predicted >= 0.45), P4(a) on Jet multi-hop (0.45, predicted >= 0.85), P4(b) in six
  RULER cells; the direction of P1-P3 and the "two halves compete for one dose" reading were pre-registered.
- One seed per model; n = 100 per real-QA cell, 50 per RULER cell, 100 per suite cell.
- The jobs ran at 8b5abb6, whose `disjoint` also dropped the 55 SQuAD paragraphs of articles without a surviving question
  (0.3% of the distractor pool, no evaluation string involved); fixed in d6523cd after submission. HotpotQA train came from the
  HuggingFace parquet mirror, converted by `hotpot_from_parquet.py`, because RULER's host did not answer; the same conversion of
  the dev split is byte-identical to exp04's paragraphs.
- The Jet finisher (1136505) found every suite complete but re-ran the bench and bits per byte, whose steps do not skip:
  ARC-Easy 0.778 -> 0.780, HellaSwag 0.492 -> 0.498 between two runs of the same adapter (3 of 500 cases), bits per byte
  identical to ten digits. results/raw holds the finisher's bench file.
- The RULER files repeat 10 (16K) and 4 (32K) case ids (generator, exp03 too), so the needle comparison is by table and
  first-occurrence counts, not by `check`; the suite gates run per file because s1 and s2 reuse case ids and held-out /
  multihop25 share their 16K and 32K ids with the suites.
- Prompts were sized with the Qwen2.5 tokenizer, as in exp04; the training documents with each model's own tokenizer.

## Post-hoc reading (2026-11-02, after the verdict; not pre-registered)
Written from the committed tables plus two things the verdict did not use: the exp03 synthetic adapters' seeds 2 and 3 on real
QA (pulled into exp04's run dir by another session, untracked, unreported) and the raw multi-hop outputs.

1. **The 8B single-document gain depends on the synthetic seed; the 2B gain does not.** McNemar realmix vs each exp03 synthetic
   seed on qa_1 (lost / gained, exact one-sided p), n = 100 per cell:

   | model | length | vs seed 1 | vs seed 2 | vs seed 3 |
   |---|---|---|---|---|
   | Jet-Nemotron-2B | 16K | 3 / 36, < 1e-4 | 1 / 50, < 1e-4 | 4 / 28, < 1e-4 |
   | Jet-Nemotron-2B | 32K | 5 / 23, 5e-4 | 2 / 35, < 1e-4 | 4 / 26, < 1e-4 |
   | Mamba-in-the-Llama 8B | 16K | 8 / 12, 0.25 | 5 / 17, 0.009 | 8 / 16, 0.08 |
   | Mamba-in-the-Llama 8B | 32K | 4 / 20, 8e-4 | 10 / 18, 0.09 | 4 / 20, 8e-4 |

   The gentle seeds score 0.56 / 0.64 / 0.56 at 32K (0.76 / 0.68 / 0.72 at 16K), so the 8B realmix gain is 0.08 to 0.16 by seed.
   Pooled over both lengths realmix beats every seed (12 / 32 p 0.002, 15 / 35 p 0.003, 12 / 36 p 4e-4); per cell three of six
   comparisons pass. P1 at 8B is likely, not established, until realmix seeds 2 and 3 run. At 2B every cell passes against every
   seed (pooled p <= 1e-9).
2. **Every Jet multi-hop failure is stale.** Suite s1 49 / 49, s2 41 / 41, multihop25 52 / 52 wrong answers return a distractor
   code from the chain (never garbage), then keep generating "Question: ... Answer:" pairs; the exp03 synthetic seed 1 had stale
   0.03 / 0.11. Retrieval survived, the second hop did not. The exp03 three-seed floor on multihop25 is 0.84 at every length, so
   the loss is outside seed noise. Two readings fit: the halved synthetic dose, or a single-span answer prior learned from SQuAD,
   which also fits the multi-value / multi-query losses and the UUID multikey_3 gains (Jet 0.58 -> 0.88 at 16K). exp06 (full
   synthetic dose plus the real half) separates them: "dose" = multihop back to >= 0.84; "prior" = failures stay stale at full dose.
3. **The 8B two-hop deficit is flat from 4K, so it is not recall.** qa_2 realmix vs Llama 0.54 / 0.47 / 0.40 vs 0.67 / 0.64 / 0.57:
   deficit 0.13 / 0.17 / 0.17 at 4K / 16K / 32K, where the base's was 0.16 / 0.30 / 0.22. The adapters removed the length-dependent
   part; what remains is present at 4K, i.e. composition lost in distillation. P2 targeted the wrong quantity; two-hop is not a
   repair target for this tool. At 2B realmix two-hop is at or above Qwen at every length (0.54 / 0.46 / 0.36 vs 0.50 / 0.39 / 0.32).
4. **Single-document QA as length curves, not per cent of the gap.** 8B realmix vs Llama 0.91 / 0.80 / 0.72 vs 0.92 / 0.82 / 0.83:
   matched through 16K, -0.11 at 32K, the one length outside the gentle recipe (8192 / 16384). 2B realmix vs Qwen 0.79 / 0.75 / 0.44
   vs 0.69 / 0.45 / 0.36: above the source everywhere, but Jet's 16K -> 32K drop is 0.31 against Qwen's 0.09, so the 2B still has
   a 32K problem the source comparison hides. The per-cent-of-gap figures in Results are the wrong yardstick; the within-model
   drop is the right one.
5. **A synthetic adapter can pass every gate and lose real QA.** exp03 Jet seed 2 keeps multihop >= 0.88 at every length in exp03,
   yet scores qa_1 0.37 / 0.26 / 0.11 at 4K / 16K / 32K against base 0.70 / 0.39 / 0.12 (qa_2 0.20 / 0.17 / 0.15 vs 0.50 / 0.28 /
   0.27): a 0.33 loss at 4K that no synthetic suite, RULER cell or bench caught. Synthetic-only repair leaves real QA to the seed
   lottery, and the standard damage check had no real-document cell. Verified since: the run matches seed 1 (case ids, prompt
   token counts, 100 rows per cell; markers 95766ca vs 734dbf3 with no code change between), and 4abb5e8 added the cell to the
   gate: `exp03_robust/results/gates.md` fails seed 2 (qa_1@4K 41 lost / 8 gained, p 9.8e-7) and passes Jet seeds 1 and 3 and
   the three 8B gentle seeds; realmix passes the same gate here.

What this changes in Next: item 1 is now a two-outcome test (dose vs prior), running as exp06; item 2 is the single lever for the
8B qa_1 residual at 32K; two-hop (P2-type predictions) is dropped as a repair target.

## Seeds 2 and 3 (2026-11-07, after the verdict; not pre-registered)
Same recipes and run dirs with TRAIN_SEED 2 and 3, at 26d25e8 (it differs from 8b5abb6 only by d6523cd, which puts the 55
SQuAD paragraphs back in the distractor pool), on A40s, all COMPLETED: Jet 1152548 / 1152556 (5 h 07 min / 6 h 47 min),
Mamba-in-the-Llama 1152550 / 1152558 (7 h 10 min / 7 h 09 min), real QA 1152549 / 1152557 / 1152551 / 1152559 (29-60 min).
Every number: `run_all.sh report`, whose tables now list seeds 1-3 and whose gates add base -> realmix per seed and file.

| cell | realmix, seeds 1 / 2 / 3 | comparator |
|---|---|---|
| 8B qa_1 at 32K | 0.72 / 0.78 / 0.78 | gentle seeds 0.56 / 0.64 / 0.56; Llama 0.83 |
| 8B qa_2 at 16K / 32K | 0.47 / 0.50 / 0.53, 0.40 / 0.53 / 0.50 | gentle seed 1 0.38 / 0.36; Llama 0.64 / 0.57 |
| 2B qa_1 at 32K | 0.44 / 0.47 / 0.48 | synthetic seed 1 0.26; Qwen 0.36 |
| Jet multi-hop suite at 16K / 32K | 0.65 / 0.63 / 0.65, 0.45 / 0.49 / 0.57 | synthetic seeds 0.94-0.97, 0.81-0.89 |
| Jet RULER multi-value / multi-query at 16K | 0.52 / 0.62 / 0.48, 0.48 / 0.40 / 0.48 | synthetic seeds 0.48-0.70, 0.36-0.62 |
| 8B RULER multi-value at 32K | 0.60 / 0.86 / 0.56 | gentle seeds 0.80 / 0.72 / 0.68 |
| bits per byte, 2B / 8B | 1.0861 / 1.0868 / 1.0863, 1.0561 / 1.0447 / 1.0364 | synthetic seed 1 1.0862; gentle seeds 1.063-1.083 |

- **P1 at 8B is now established**, the open point of post-hoc item 1: every realmix seed beats every gentle seed on qa_1 at
  32K, by 0.08 to 0.22, and stays 0.05-0.11 below Llama. At 2B all three seeds sit above the Qwen source.
- **P2 at 32K** misses on seed 1 only (0.40); seeds 2 and 3 reach 0.53 / 0.50 against the 0.45 prediction.
- **P4(a) replicates**: Jet multi-hop at 32K is 0.45-0.57 at every seed, below every synthetic seed, and nearly every
  failure is stale (0.43-0.55 of cases).
- **P4(b) is not established.** Jet's multi-value and multi-query at 16K and the 8B multi-value at 32K overlap the
  synthetic adapters' seed ranges, so the single-seed gaps of 0.12-0.20 in these 50-case cells do not show a loss.
- The damage check passes at every seed: base -> realmix flags no cell in real QA or the four synthetic files (20 new
  gates). Bench stays within 0.01 of seed 1 at both scales.

## Control: the 2B recipe on the source (pre-registered 2026-11-18, before the run)
**Verdict: training, and the deficit stays open at 32K.** The source gains 0.31 on qa_1 at 16K and 0.40 at 32K from the
same recipe, as much as Jet. After equal training the source holds 0.76 from 16K to 32K and Jet falls from 0.72-0.75 to
0.44-0.48: the gap at 32K is 0.28-0.32, against 0.24 before any training.

**Question.** Jet's realmix adapters score 0.72-0.75 on qa_1 at 16K, where the Qwen2.5-1.5B it was converted from scores
0.45. The adapters trained on SQuAD and HotpotQA documents in the evaluation's own framing, so part of that gain may be
what this training gives any model, and the source never got it. exp04's control (the synthetic adapter on the source)
stayed flat, but it saw no real documents.

**Method.** The Jet recipe unchanged (600 documents, half real, lr 2e-4, 8K-32K, seed 1, tag `-realmix`) on
`Qwen/Qwen2.5-1.5B`, env `modern`, through `robust.sbatch` in exp05's run dirs, then `realdocs.sbatch` on the exp04 cases.
Decodes run with `RG_AUTOTUNE=1`, the path of the stored Qwen2.5 runs (Qwen2.5 has no autotuned kernel; the variable
removes the doubt). The code is origin/main 01cb0b7; the trainer has not changed since 26d25e8.

**Outcomes**, on qa_1, n = 100 per cell. G is the control's gain: source + realmix minus source. Jet's gain is 0.33-0.36
at 16K and 0.32-0.36 at 32K over three seeds.
- **repair**: G <= 0.10 at 16K and at 32K. The source barely moves, so Jet's gain is recall the conversion lost.
- **training**: G >= 0.20 at 16K or at 32K. A full-attention model gains from the same documents, so Jet's gain is at
  least partly what the training gives any model, and "repairs" has to become "raises".
- **mixed**: anything else.
- Read separately, the deficit after equal training: `check` from source + realmix to Jet + realmix (seeds 1, 2, 3) over
  the six real-QA cells. **closed** if every seed passes, **open** if a cell fails for at least two seeds, otherwise
  seed-dependent.
- Reported, not criteria: qa_2, the 4K cells, and the control's damage checks (suites, RULER, benchmarks, bits per byte).

Expectation, not a criterion: training 0.55, mixed 0.25, repair 0.20. Deficit: open 0.55 (at 32K), closed 0.25.

**Results.** Jobs 1185235 (training 49 min, then the damage checks) and 1185236 (real QA, 29 min) on 2026-11-18 at
01cb0b7, both on a256-a40-05 (`sacct`). Departure from the method: 1185236 was released from its dependency once the
adapter was saved (19:02), so it ran beside the damage checks, not after them. `train_stats.json` matches Jet's seed 1: 600
documents, 150 steps, lr 2e-4, rank 16, the same pools and bans. The source has four kinds of projection to adapt (0.28% of
its weights) where Jet has nine, and ends at loss 0.209 against Jet's 0.381. The sha256 of the three result files matches
the cluster. Every number: `run_all.sh report` (results/tables-qa.md, results/gates.md; it prints the label).

| qa_1 | 4K | 16K | 32K |
|---|---:|---:|---:|
| Qwen2.5-1.5B | 0.69 | 0.45 | 0.36 |
| Qwen2.5-1.5B + realmix (the control) | 0.89 | 0.76 | 0.76 |
| Jet-Nemotron-2B | 0.70 | 0.39 | 0.12 |
| Jet-Nemotron-2B + realmix, seeds 1 / 2 / 3 | 0.79 / 0.86 / 0.85 | 0.75 / 0.72 / 0.72 | 0.44 / 0.47 / 0.48 |
| gain of the control (G) | 0.20 | 0.31 | 0.40 |
| gain of Jet | 0.09-0.16 | 0.33-0.36 | 0.32-0.36 |
| gap, source minus Jet, before training | -0.01 | 0.06 | 0.24 |
| gap after equal training | 0.03-0.10 | 0.01-0.04 | 0.28-0.32 |

**Outcome: training**, by the rule (G = 0.31 at 16K, 0.40 at 32K; 2 lost / 33 gained and 3 lost / 43 gained).
**Deficit after equal training: open.** Source + realmix -> Jet + realmix fails pooled and on qa_1 at 32K for all three
seeds (40 lost / 8 gained, 35 / 6, 37 / 9; p < 3e-5). Seed 1 also fails qa_2 at 32K (19 / 6, p 0.007). No cell at 4K or
16K fails for any seed. Both expectations (training 0.55, open 0.55) were right.

- **Jet's real-QA gain is what the training gives any model.** The source gains about as much: 0.31 against Jet's
  0.33-0.36 at 16K, 0.40 against 0.32-0.36 at 32K, and 0.20 even at 4K, where length is not the difficulty. For real QA
  the adapter raises recall; "repairs" is not shown.
- **The 32K deficit is the hybrid's, and this training does not close it.** At 16K the trained hybrid matches the trained
  source (0.01-0.04 below, passes). At 32K it is 0.28-0.32 below. The trained source no longer loses anything from 16K to
  32K; the trained hybrid loses 0.24-0.31.
- **Against the untrained source the earlier reading stands as measured**: Jet + realmix is above Qwen's 0.36 at 32K. That
  comparison gave one model the training and not the other.
- qa_2 (reported): the control gains 0.07 / 0.17 / 0.17 (0.57 / 0.56 / 0.49). The gap after equal training is 0.01-0.05 at
  4K, 0.08-0.10 at 16K (p 0.03-0.08, not flagged) and 0.04-0.13 at 32K.
- The synthetic adapter is the arm where the source stays flat (exp04, two seeds). Its gain on Jet's qa_1 at 32K is small
  and seed-dependent: 0.12 -> 0.26 / 0.11 / 0.22.

Post hoc, not in the rule: RULER's rule counts the answer anywhere in the output, and every model runs on after its answer.
Scored on the first line only, the control still gains 0.31 at 16K and 0.36 at 32K (0.72), and the gap after equal
training is 0.25-0.28 at 32K. The run-on text does not carry the result.

Limits: one control seed against Jet's three; n = 100 per cell; qa_1 questions are 96% from one article. The 8B pair's
control followed on 2026-11-19 (next section).

**Damage checks** (reported, not criteria). Job 1185235 COMPLETED after 3 h 48 min; ten result files, sha256 as on the
cluster. Every number: `run_all.sh report` (results/tables-damage.md, tables-ruler.md, gates.md, and its bench / bpb
lines). Recall at 16K / 32K, n = 100 per suite cell and 50 per RULER cell:

| | Qwen2.5-1.5B | + synthetic control (exp03, seed 1) | + realmix (this control) |
|---|---:|---:|---:|
| multihop | 0.20 / 0.14 | 0.99 / 0.98 | 0.96 / 0.95 |
| updated | 0.42 / 0.34 | 1.00 / 1.00 | 1.00 / 0.97 |
| many_similar | 0.88 / 0.75 | 0.99 / 0.95 | 0.98 / 0.97 |
| many_random, heldout_many, needle | 0.90-1.00 | 1.00 | 1.00 |
| RULER multi-value | 0.74 / 0.46 | 0.54 / 0.36 | 0.72 / 0.54 |
| RULER multi-query | 0.64 / 0.48 | 0.52 / 0.46 | 0.72 / 0.54 |
| RULER multikey_3 (UUID keys) | 0.40 / 0.40 | 0.62 / 0.64 | 0.60 / 0.46 |
| ARC-Easy / HellaSwag (acc, n = 500) | 0.746 / 0.520 | 0.736 / 0.520 | 0.754 / 0.512 |
| bits per byte, Moby Dick at 16K | 1.0636 | 1.0701 | 1.0757 |

- The control passes all four suite gates: pooled 3 lost / 181 gained (s1), 1 / 168 (s2), 0 / 8 (held-out), 0 / 115
  (multihop25). The benchmarks stay within 0.01 (acc). Bits per byte rise by 0.012, against 0.007 for the synthetic control.
- **Halving the synthetic dose costs the source 0.03 on multi-hop** (0.96 / 0.95 against 0.99 / 0.98). Jet with the same
  recipe reaches only 0.63-0.65 / 0.45-0.57 over three seeds, against 0.94-0.97 / 0.81-0.89 with the full dose (P4(a)).
  That loss needs the hybrid.
- No RULER cell falls more than 0.02 below the source. The synthetic control's drops on multi-value and multi-query
  (0.74 -> 0.54, 0.46 -> 0.36, 0.64 -> 0.52) are absent; the other RULER cells are 0.96-1.00.
- Variants at 32K on suite seed 1 (n = 50): unmerged 0.94-1.00. Under the chat template 0.00-0.12; Qwen2.5-1.5B is a base
  model, and the synthetic control ranged from 0.20 to 0.98 there over two seeds (exp03).

## Control at 8B: the gentle recipe on the source (pre-registered 2026-11-18, before the run)
**Verdict: open, and mixed at 16K.** After the same training Llama scores 0.97 / 0.89 / 0.90 on qa_1, and the trained
hybrid is below it at 32K for all three seeds (0.72-0.78; 19 lost / 1 gained, 14 / 2, 14 / 2) and at 4K for two. The gap
at 32K is 0.12-0.18, against 0.64 before any training. Llama gains 0.07 at 16K, where the hybrid gains 0.15-0.18. Post
hoc: counted on the first line of the output only, the 32K gap is 0.10-0.16 and one seed of three fails, which the rule
would call seed-dependent.

**Question.** The 2B control showed that the realmix recipe lifts the source as much as the hybrid. The 8B numbers still
compare a trained hybrid with an untrained source: Mamba-in-the-Llama + realmix scores 0.72-0.78 on qa_1 at 32K against
Llama-3.1-8B-Instruct's 0.83. What does the same training give Llama, and is the single-document gap still closed after it?

**Method.** The 8B recipe unchanged (300 documents, half real, lr 5e-5, 8K-16K, seed 1, tag `-realmix`) on
`meta-llama/Llama-3.1-8B-Instruct`, env `modern`, through `robust.sbatch` in exp05's run dirs, then `realdocs.sbatch` on
the exp04 cases; `RG_AUTOTUNE=1` as for the 2B control. The real-QA job is queued behind the training job and released
once the adapter is saved, so it runs beside the damage checks (done by hand for the 2B control, planned here). The code
is origin/main 01cb0b7.

**What the run cannot change.** Llama scores 0.82 at 16K and 0.83 at 32K, so its gain G (Llama + realmix minus Llama) is
at most 0.18 and 0.17. The hybrid gained 0.53-0.59 at 32K. So the 2B rule (training: G >= 0.20) cannot fire, and at 32K
the gap after equal training is at most 0.22-0.28, against 0.64 before: at least 56% of it closes whatever the control
shows.

**Outcomes**, on qa_1, n = 100 per cell.
- **Deficit after equal training** (the criterion): `check` from Llama + realmix to Mamba-in-the-Llama + realmix (seeds 1,
  2, 3), read on the three qa_1 cells. Against the untrained Llama no qa_1 cell fails for any seed (closest: 32K seed 1,
  17 lost / 6 gained, p 0.017; 4K seed 2, 10 / 3, p 0.046). **closed**: still none. **open**: a qa_1 cell fails for at
  least two seeds. Otherwise **seed-dependent**.
- **Gain of the source at 16K**, the length where the hybrid's gain (0.15-0.18) fits in the source's room: **repair** if
  G <= 0.05, **training** if G >= 0.10, otherwise **mixed**. These are the 2B thresholds in proportion: about 30% and 60%
  of the hybrid's gain.
- Reported, not criteria: G at 4K and 32K and the gap after equal training at each length; the same counted on the first
  line of the output only; qa_2 (against the untrained Llama it already fails at 16K for all three seeds); the control's
  damage checks.

Expectation, not a criterion: deficit seed-dependent 0.40, open 0.30, closed 0.30; at 16K repair 0.40, mixed 0.30,
training 0.30. Power is low: one control seed and n = 100, and the 16K labels are five cases apart.

**Results.** Jobs 1187070 (training 44 min, then the damage checks) and 1187071 (real QA, 51 min) on 2026-11-18 and 19 at
01cb0b7, both on a256-a40-04 (`sacct`). Departure from the method: 1187071 was not released early (the Mac slept and the
loop never ran), so it started when 1187070 ended, after the damage checks. `train_stats.json`: 300 documents, 75 steps,
lr 5e-5, rank 16, 3,675,752 tokens. The hybrid's seed 1 saw 3,676,252: it was trained at 8b5abb6, before d6523cd put 55
paragraphs back in the distractor pool; seeds 2 and 3 have them, as the control does. Llama has four kinds of projection
to adapt (0.17% of its weights, training log) where the hybrid has six, and ends at loss 0.223 against the hybrid's 0.304.
The sha256 of the three result files matches the cluster. Every number: `run_all.sh report` (results/tables-qa.md,
results/gates.md; it prints the gains, the label and the first-line lines).

| qa_1 | 4K | 16K | 32K |
|---|---:|---:|---:|
| Llama-3.1-8B-Instruct | 0.92 | 0.82 | 0.83 |
| Llama-3.1-8B-Instruct + realmix (the control) | 0.97 | 0.89 | 0.90 |
| Mamba-in-the-Llama | 0.86 | 0.65 | 0.19 |
| Mamba-in-the-Llama + realmix, seeds 1 / 2 / 3 | 0.91 / 0.85 / 0.88 | 0.80 / 0.83 / 0.80 | 0.72 / 0.78 / 0.78 |
| gain of the control (G) | 0.05 | 0.07 | 0.07 |
| gain of the hybrid | -0.01 to 0.05 | 0.15-0.18 | 0.53-0.59 |
| gap, source minus hybrid, before training | 0.06 | 0.17 | 0.64 |
| gap after equal training | 0.06-0.12 | 0.06-0.09 | 0.12-0.18 |

**Deficit after equal training: open.** Llama + realmix -> Mamba-in-the-Llama + realmix fails qa_1 at 32K for all three
seeds (19 lost / 1 gained, 14 / 2, 14 / 2; p 2e-5, 0.002, 0.002) and qa_1 at 4K for seeds 2 and 3 (13 / 1, 9 / 0; p 0.0009,
0.002). At 16K no seed fails (13 / 4, 11 / 5, 14 / 5; p 0.02-0.11). All three seeds fail pooled (113 / 13, 90 / 16,
97 / 19). **Gain of the source at 16K: mixed** (G = 0.07; 2 lost / 9 gained), two cases above the repair threshold.
Neither was the expected outcome: seed-dependent and repair had 0.40 each, open and mixed 0.30.

- **The 8B gap is not closed, but most of it is.** Against the untrained Llama no qa_1 cell failed (0.83 against
  0.72-0.78 at 32K). The same training lifts Llama to 0.90, and the gap at 32K is then 0.12-0.18. It was 0.64 before any
  training, so 72-81% of it closes; 56% was certain before the run.
- **Unlike at 2B, the source gains much less than the hybrid.** Llama gains 0.05 / 0.07 / 0.07, the hybrid 0.15-0.18 at
  16K and 0.53-0.59 at 32K. So at least 0.46 of the hybrid's gain at 32K is not what this training gives the source.
  Llama had only 0.17-0.18 of room there, so the two gains cannot be compared in size; the gap after equal training is
  the fair number.
- The control's own gain shows pooled (16 lost / 55 gained over the six cells) and in no single cell at the corrected
  level (qa_1: 0 / 5, 2 / 9, 2 / 9).
- qa_2 (reported): the control gains 0.04 / 0.06 / 0.10 (0.71 / 0.70 / 0.67). The gap after equal training is 0.10-0.17
  at 4K, 0.17-0.23 at 16K and 0.14-0.27 at 32K, against 0.16 / 0.30 / 0.22 before training. The gate fails at 16K and
  32K for all three seeds and at 4K for seeds 1 and 3. Two-document questions stay the larger deficit.

Post hoc, not in the rule (the first-line counts were pre-registered as reported; the paired test on them was not).
RULER's rule counts the answer anywhere in the output. The trained Llama runs on with further `Answer:` lines, and in nine
qa_1 cases (5 / 2 / 2 at 4K / 16K / 32K) only a later line holds the gold answer; in six of the nine the first line names
a different answer (my reading of the outputs the report prints). The untrained Llama has no such case and the trained
hybrid 0-2 per cell. On the first line only:
- Llama's gain is 0.00 / 0.05 / 0.05, so the 16K gain sits on the repair threshold.
- The gap after equal training is 0.03-0.07 at 4K, 0.04-0.08 at 16K and 0.10-0.16 at 32K.
- At 32K the gate reads 19 lost / 3 gained (p 0.0004), 14 / 4 (p 0.015) and 13 / 3 (p 0.011). Only seed 1 is under the
  corrected level of 0.0083, which the rule would call seed-dependent. No 4K or 16K cell fails (4K: 7 / 4, 10 / 3, 7 / 3).

So the 4K failures come from the later lines. The 32K gap is there on both counts and in all three seeds; on the first
line it clears the corrected level for one seed.

Limits: one control seed against the hybrid's three; n = 100 per cell; qa_1 questions are 96% from one article; the
first-line gate is post hoc; the gentle synthetic adapter has no control on Llama.

**Damage checks** (reported, not criteria). Job 1187070 COMPLETED after 6 h 40 min; ten result files, sha256 as on the
cluster. Every number: `run_all.sh report` (results/tables-damage.md, tables-ruler.md, gates.md, and its bench / bpb
lines). Recall at 16K / 32K, n = 100 per suite cell and 50 per RULER cell:

| | Llama-3.1-8B-Instruct | + realmix (this control) |
|---|---:|---:|
| multihop | 0.63 / 0.49 | 0.99 / 0.93 |
| updated | 0.87 / 0.74 | 1.00 / 0.99 |
| many_similar | 0.95 / 1.00 | 1.00 / 0.99 |
| many_random, heldout_many, needle | 0.99-1.00 | 1.00 |
| RULER multi-value | 0.92 / 0.98 | 0.94 / 1.00 |
| RULER multi-query | 1.00 / 1.00 | 1.00 / 1.00 |
| RULER multikey_3 (UUID keys) | 0.98 / 0.96 | 1.00 / 0.98 |
| ARC-Easy / HellaSwag (acc, n = 500) | 0.808 / 0.598 | 0.814 / 0.596 |
| bits per byte, Moby Dick at 16K | 0.7997 | 0.8414 |

- The control passes all four suite gates: pooled 2 lost / 70 gained (s1), 2 / 58 (s2), 0 / 0 (held-out), 0 / 52
  (multihop25). The benchmarks stay within 0.01 (acc). Bits per byte rise by 0.042, against 0.028-0.048 for the hybrid's
  three realmix seeds.
- The synthetic half lifts Llama's multi-hop from 0.63 / 0.49 to 0.99 / 0.93 and updated from 0.87 / 0.74 to 1.00 / 0.99.
  The trained hybrid scores 0.97-0.99 / 0.90-0.97 on multi-hop over three seeds, around the control (no gate was run on
  that pair).
- No RULER cell falls below the source.
- Variants at 32K on suite seed 1 (n = 50): unmerged 0.92-1.00, chat template 0.88-1.00; multi-hop is the lowest in both.

## Next
1. Budget, not split: Jet with the full 600 synthetic documents plus 600 real (the pre-registered reading of a P4 failure), to
   keep qa_1 at 0.44 without losing chained-key multi-hop; then the 8B recipe at 300 synthetic + 300 real.
2. 32K documents in the 8B recipe (the gentle recipe stops at 16K and qa_2 moved only at 16K): 8K / 16K / 32K, same 300 documents.
3. Seeds 2 and 3 of the realmix adapters on the headline cells (qa_1 at 32K, both scales; 8B qa_2 at 16K): done 2026-11-07,
   section "Seeds 2 and 3".
4. qk-only + real QA: exp04's qk-only adapter moved qa_2 everywhere with no 4K cost; the real half may stack with it.

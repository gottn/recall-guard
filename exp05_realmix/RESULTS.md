# Experiment 5: real-document QA in the repair mix

**Verdict: pending.** Predictions P1-P4 below were written on 2026-10-26 before any model ran; the Results section is
filled in only from `results/raw` by `run_all.sh report`.

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
Pending. Every number: `run_all.sh report` (results/tables-qa.md, results/tables-damage.md, results/gates.md).

## Failures and limits
Pending.

## Next
Pending.

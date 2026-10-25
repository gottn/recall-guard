# Experiment 4: recall on real documents

**Verdict: pending.** Predictions below were written on 2026-10-25 before any model ran; the Results section is filled in
only from `results/raw` by `run_all.sh report`.

## Question
Every number so far comes from synthetic documents: filler text with planted six-digit codes, for the deficit (exp01,
exp03) and for the repair training (exp02, exp03). Two things are untested. Does the converted hybrid's multi-key deficit
show on real documents with real questions? And does the adapter, trained only on synthetic key lists, hold on real
documents without damaging them? docs/robustness.md item 6 pre-registered the second as "QA at 8-32K"; only its
perplexity half was run.

## Method
RULER's two QA tasks over real Wikipedia paragraphs, generated with NVIDIA's `qa.py` (recipe and checksums in
RULER-PROVENANCE.md):
- `qa_1`: SQuAD v2 dev questions; the gold paragraph sits among the other paragraphs of the same article first, then
  paragraphs of other articles (topically similar distractors: the natural counterpart of `many_similar`).
- `qa_2`: HotpotQA dev (distractor setting) questions; two gold paragraphs among paragraphs from other questions (the
  natural counterpart of `multihop`).
Prompts are sized under the Qwen2.5-1.5B tokenizer to 4K, 16K and 32K; 100 questions per cell, the same 100 questions at
every length (RULER takes them in order), so length is the only variable. Completion prompts, greedy decoding, 32 new
tokens (RULER's budget for QA), no chat template. Scoring is RULER's `string_match_part`: one of the reference answers
appears anywhere in the completion, case-insensitive (rule `any`).

Models, one job each (`infra/slurm/realdocs.sbatch`, A40):
- 2B pair: Qwen2.5-1.5B and Jet-Nemotron-2B, each base and with its exp03 seed-1 adapter. The adapter on the source is the
  control: a change it produces is format familiarity, not repair.
- 8B pair: Llama-3.1-8B-Instruct base; Mamba-in-the-Llama base, with the gentle seed-1 adapter and with the qk-only
  seed-1 adapter.

Verdict rule: `recall-guard check` (exact one-sided McNemar on shared case ids, per cell and pooled, alpha 0.05 split over
the six cells). n = 100 per cell: 1 SE is about 0.04 at a rate of 0.8; a cell trips at about ten lost cases with none gained.

## Predictions
- **P1, the deficit is real.** From 4K to 32K the hybrid loses more than its source on both tasks, and
  `check --baseline source --candidate hybrid` fails at 32K. Expected gap at 32K: 0.10-0.30, smaller than the 0.6-0.8 on
  sixteen planted keys, because one gold paragraph among topical distractors sits between our needle and our 16-key task.
  Prior: Jet's RULER multi-key gap at 32K was 0.38 on MK1 and 0.44 on multi-value (exp03 item 1); the 8B pair's 0.60-1.00.
- **P2, the repair transfers.** `check --baseline hybrid --candidate repaired` passes at every length (no cell lost), and the
  repaired hybrid closes at least half of its 32K gap to the source. The control adapter on the source changes nothing
  beyond noise (its pooled row passes in both directions).
- **P3, no damage at short length** (item 6). At 4K the repaired hybrid is within 1 SE of its base on both tasks.

What each outcome means. P1 false: the synthetic deficit is a template effect and the tool's claim narrows to a weakness
that real QA at these lengths does not expose. P2 false with P1 true: the repair is template-bound; the next step is to
add real-document QA to the training mix. P3 false: the adapter costs short-context QA and the gentle or qk-only recipe is
the one to ship.

## Results
Pending. Eight jobs submitted 2026-10-25 at 734dbf3 (1121123-1121130, run dir
`~/runs/rg/realdocs/20261025-161716-734dbf3`, see STATE.md); then pull and `run_all.sh report`.

# Experiment 4: recall on real documents

**Verdict, 2B stage (2026-10-25): the deficit is real on real documents (Jet 0.12 vs Qwen 0.36 on single-document QA at 32K,
equal at 4K), and the adapter trained only on synthetic key lists repairs about half of it (0.26) with no cell lost and no
measurable damage at 4K; two-hop QA is near floor for both models at 32K. 8B stage pending.** Predictions below were written
on 2026-10-25 before any model ran; the Results section is filled in only from `results/raw` by `run_all.sh report`.

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
Run dir `~/runs/rg/realdocs/20261025-161716-734dbf3`, jobs 1121123-1121130 at 734dbf3. Every number: `run_all.sh report`
(results/tables.md, results/gates.md); n = 100 per cell; "a / b" is cases lost / gained by the candidate, p the one-sided exact
McNemar p of `check`.

### 2B pair (complete 2026-10-25, ~35 min per job on an A40)

| task | model | 4K | 16K | 32K |
|---|---|---:|---:|---:|
| qa_1 | Qwen2.5-1.5B | 0.69 | 0.45 | 0.36 |
| qa_1 | Qwen2.5-1.5B + control adapter | 0.70 | 0.50 | 0.38 |
| qa_1 | Jet-Nemotron-2B | 0.70 | 0.39 | 0.12 |
| qa_1 | Jet-Nemotron-2B + adapter | 0.67 | 0.42 | 0.26 |
| qa_2 | Qwen2.5-1.5B | 0.50 | 0.39 | 0.32 |
| qa_2 | Qwen2.5-1.5B + control adapter | 0.44 | 0.34 | 0.38 |
| qa_2 | Jet-Nemotron-2B | 0.50 | 0.28 | 0.27 |
| qa_2 | Jet-Nemotron-2B + adapter | 0.46 | 0.33 | 0.28 |

- **P1 holds on qa_1.** Source -> hybrid fails the gate pooled (110 / 65, p 4e-4) and on qa_1 at 32K (0.36 vs 0.12; 26 / 2,
  p 1.5e-6); the two are equal at 4K (0.69 vs 0.70). The gap, 0.24, is inside the predicted 0.10-0.30. On qa_2 the gap is 0.11
  at 16K (24 / 13, p 0.049, under the corrected threshold) and 0.05 at 32K (13 / 8): both models are near floor there.
- **P2 holds on qa_1.** Hybrid -> repaired passes the gate everywhere (no cell lost) and lifts qa_1 at 32K from 0.12 to 0.26
  (2 / 16, p 7e-4 for the gain), closing 0.14 of the 0.24 gap (58%). The control adapter leaves the source unchanged (qa_1 at
  32K 0.36 -> 0.38, 11 / 13), so the lift is repair, not format familiarity. qa_2 is unchanged (0.27 -> 0.28).
- **P3 holds, narrowly.** At 4K the repaired hybrid is 0.03 and 0.04 below its base (qa_1 14 / 11, p 0.35; qa_2 9 / 5, p 0.21;
  both tasks pooled 23 / 16, p 0.17), within 1 SE (0.05); the control shows the same direction on qa_2 (0.50 -> 0.44, 8 / 2,
  p 0.055). A cost of a few points at short length cannot be excluded at n = 100.
- Context: both models lose recall with length on real QA (source qa_1 0.69 -> 0.36); the hybrid-specific part is the extra
  drop, and the adapter recovers about half of it on real documents against all of it on synthetic keys (exp03).

### 8B pair
Pending: jobs 1121127-1121130.

# Robustness plan (set 2026-10-16, after exp01 and exp02)

Each item names the test, the bar it must clear, and the cost. Items 1-7 harden the two existing results; 8-11 make
them general; 12-13 make them reproducible by others. Predictions are written before the runs so results cannot be
re-interpreted afterwards.

| # | Test | Bar | Cost (A100 h) |
|---|---|---|---:|
| 1 | Power: n = 50 per cell at 16K / 32K, 2 suite seeds, 3 training seeds; report mean ± SE | every headline gap ≥ 3 SE; the 16K gap either confirmed or dropped | 6 |
| 2 | RULER multi-key (MK1-3, MV, MQ) on the same four models, before and after repair | state plainly whether RULER sees the same failure; if yes, the harness claim becomes "document-derived + repair", not "detection" | 2 |
| 3 | Length generalisation: train at ≤ 16K, test at 32K and 64K | ≥ 0.8 at 32K when never trained there; report the 64K number whatever it is | 4 |
| 4 | Capacity frontier: 16 / 32 / 64 / 128 keys at 32K, before and after repair | a curve with the key count where the repaired state drops below 0.5 | 3 |
| 5 | Repair data coverage: add multi-hop, aggregation and overwrite questions to the mix | no task scores below its pre-repair value; multi-hop ≥ control | 3 |
| 6 | Damage on long inputs: LongBench subset or QA at 8-32K plus perplexity on long natural text, alongside ARC / HellaSwag | all within 1 SE of before | 2 |
| 7 | Alternative explanations: unmerged vs merged adapter; chat-template prompting; exact vs contains scoring; per-model token counts | all agree within noise, or the discrepancy is reported | 2 |
| 8 | Repair ablations: attention-only vs Jet-block-only vs both; rank 4 / 16 / 64; answer-only vs full LM loss; data mix | the minimal recipe that reaches the control's level | 8 |
| 9 | Second conversion family at 8B: LoLCATs-Llama-3-8B vs Llama-3-8B (and a 50%-softmax Lizard-style hybrid as the expected null) | deficit and repair replicate at 8B; parity for the 50% hybrid | 20 |
| 10 | Native hybrids: Qwen3.5-4B, Falcon-H1-7B at 64 keys and 64K | a measured breaking point per model, or a statement that none was found in range | 6 |
| 11 | Step 2: ordinary instruction SFT (≈10K samples at ≤ 4K) on repaired Jet and on Qwen3.5-4B; freeze ablation | recall change after SFT with SE; a freeze rule if a drop exists | 10 |
| 12 | Reproducibility: pinned env, one-command rerun per table, suites and raw outputs committed, rerun on a different GPU type | a third party reproduces every table within SE | 2 |
| 13 | Pre-registration: predictions and bars for 3, 4, 9, 11 written in this file before submission | no bar changed after a result is seen | 0 |

Total ≈ 70 A100 hours. Order: 1, 2, 5, 6, 7 first (they can change what we claim), then 3, 4, 8 (they shape the recipe),
then 9, 10, 11 (they decide whether it travels).

## Predictions (written 2026-10-16, before running)
- Item 1: the 32K gaps survive; the 16K gap for random keys shrinks below 3 SE.
- Item 2: RULER MK1 at 32K also flags Jet-Nemotron-2B; MK2/MK3 flag it more strongly than our 16-key task.
- Item 3: training at ≤ 16K gives ≥ 0.7 at 32K; 64K drops below 0.5.
- Item 4: the repaired state holds 32 keys at 32K above 0.8 and falls below 0.5 between 64 and 128.
- Item 9: the deficit replicates for LoLCATs-8B (it fails single needle too, so it will be larger); repair works but needs more steps.
- Item 11: SFT on the repaired Jet erases most of the repair unless the Jet blocks are frozen; Qwen3.5-4B loses little.

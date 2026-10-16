# Experiment 3 — robustness of exp01 and exp02 (interim: base stage complete, repair seeds running)

Run dir `~/runs/rg/robust/20261016-171229-9f67d4b`, commit `9f67d4b`, A100-SXM4-40GB. Reproduce: `exp03_robust/run_all.sh`.
Items refer to docs/robustness.md. Predictions there were written before these numbers.

## Base-stage verdicts (2026-10-16 night)

1. **RULER's own multi-key tasks see the Jet-Nemotron failure (item 2, prediction confirmed).** On NVIDIA's generator
   output, 50 cases per cell, RULER rule (every expected string anywhere in the output):

   | RULER task at 32K | Jet-Nemotron-2B | Qwen2.5-1.5B |
   |---|---:|---:|
   | niah_single_1 (noise haystack) | 1.00 | 1.00 |
   | niah_multikey_1 (essay, 4 keys) | 0.56 | 0.94 |
   | niah_multikey_2 (needle haystack) | 0.26 | 0.72 |
   | niah_multikey_3 (uuid keys) | 0.16 | 0.40 |
   | niah_multivalue | 0.02 | 0.46 |
   | niah_multiquery | 0.00 | 0.48 |

   At 16K the multi-value and multi-query variants are even more sensitive (0.24 / 0.08 vs 0.74 / 0.64).
   Consequence, as pre-registered: the harness has **no detection advantage over RULER** for this failure. Its value is
   the paired converted-vs-source measurement, document-derived facts, and the repair recipe, not detection.

2. **The 16K gap is confirmed, not weakened (item 1; prediction 1 was wrong).** Two fresh suites, 50 cases each, pooled
   to n = 100 per cell (SE about 0.05):

   | task | length | Jet | Qwen2.5 | gap |
   |---|---:|---:|---:|---:|
   | needle | 16K | 1.00 | 1.00 | 0.00 |
   | needle | 32K | 0.86 | 1.00 | 0.14 |
   | many_random | 16K | 0.57 | 0.90 | **0.33** |
   | many_random | 32K | 0.31 | 0.90 | **0.59** |
   | many_similar | 16K | 0.70 | 0.88 | 0.18 |
   | many_similar | 32K | 0.22 | 0.75 | **0.53** |
   | heldout_many | 32K | 0.45 | 0.94 | 0.49 |
   | updated | 32K | 0.58 | 0.34 | hybrid ahead |

   Two corrections to exp01's wording: Jet's needle at 32K is 0.86 at n = 100, not 1.00 (the single-needle vs
   multi-key dissociation stands, 0.86 vs 0.31, but "passes the needle perfectly" was an n = 25 artifact; on RULER's
   noise haystack it is 1.00); and near-duplicate keys are no harder than random keys at 16K (0.70 vs 0.57).

3. **Generation is deterministic (item 7).** The held-out suite's 150 prompts are byte-identical to exp02's; all 150
   completions of both models are byte-identical across the two runs (same GPU type, bf16, SDPA, Triton kernels).

4. **Base damage-check values** (for the after-numbers to be compared against): bits per byte on Moby Dick at 16K,
   Jet 1.082, Qwen2.5 1.064; ARC-Easy / HellaSwag as in exp02 (Jet 0.764 / 0.508, Qwen2.5 0.746 / 0.520).

## Repair stage, Jet seeds 1 and 2 complete (v2 mix with multi-hop; seed 3 and the controls pending)

5. **Repair replicates across training seeds and the multi-hop regression is gone (items 1, 5).** At 32K, n = 100:
   many_random 1.00 / 0.97, many_similar 1.00 / 0.97, held-out parcels 0.98 / 0.95, needle 1.00 / 1.00, updated 1.00 / 1.00,
   and multi-hop 0.88 / 0.88 (base 0.11; the exp02 v1 mix had driven it to 0.03).
6. **Transfer to RULER is real for numeric values and absent for UUIDs (item 2, after repair, seed 1).** multikey_1 at 32K
   0.56 to 0.90 (source model 0.94); multikey_2 0.26 to 0.53 (0.72); multivalue at 16K 0.24 to 0.68 (0.74); multiquery
   at 16K 0.08 to 0.62 (0.64); multikey_3 with UUID keys and values unchanged (0.16 to 0.18). The repair data only
   contained numeric values, so the model learned numeric retrieval: coverage of the training mix sets the boundary.
7. **Damage (item 6):** ARC-Easy 0.764 to 0.776 / 0.770, HellaSwag 0.508 to 0.492 / 0.510 (SE 0.022, unchanged); bits per
   byte on Moby Dick at 16K 1.082 to 1.086 / 1.087, a consistent +0.4% across seeds and across all 8 windows. Small, but
   it is a real cost and should be reported as one.

## Pending (jobs 1089546-1089548)
Repair with the v2 mix (multi-hop included), Jet seeds 1-3 and Qwen2.5 seeds 1-2, then the same evaluations plus the
unmerged-adapter and chat-template checks. Items 5, 6, 7 are decided by those.

## Notes
- The n = 50 suites include `heldout_many` as a sixth task (it is in the task registry), so pooled held-out numbers above
  come from 100 fresh cases, not the 25-case exp02 file.
- RULER values are 7-digit numbers and UUIDs; the `contains` rule scores them. `exact` is undefined for that rule.

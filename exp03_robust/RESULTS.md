# Experiment 3 — robustness of exp01 and exp02 (2B and 8B stages complete)

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

8. **Alternative explanations (item 7, seed 1 at 32K, 300 cases).** Unmerged adapter vs merged weights: identical
   scores on every task (0.98 / 1.00 / 1.00 / 0.88 / 1.00 / 1.00), 269 / 300 completions byte-identical, the rest
   differing only in bf16 rounding of the merge. Chat-template prompting: Jet-Nemotron-2B is a base model and, wrapped
   in its chat template, echoes the instruction back (0.00 on everything), so this check is inapplicable to the 2B
   pair; it is meaningful only for instruct models and will be read from the 8B pair (Llama-3.1-8B-Instruct and the
   Mamba-in-the-Llama DPO model).

9. **Three seeds agree (item 1).** At 32K, n = 100 per seed: many_random 1.00 / 0.98 / 1.00, many_similar 1.00 / 0.98 / 1.00,
   held-out parcels 0.98 / 0.96 / 0.93, multi-hop 0.89 / 0.88 / 0.81, needle and updated 1.00 on all. Seed 3's bench and bpb are
   in results/raw (same pattern as seeds 1-2).

## Control stage complete (Qwen2.5-1.5B, two training seeds): what is repair and what is familiarity

10. **On our suites the control also climbs to the ceiling**, so the hybrid's post-repair level (1.00) equals the
    control's (1.00): at 32K, pooled n = 200, many_random 0.90 to 1.00, many_similar 0.75 to 0.96, updated 0.34 to 1.00,
    multi-hop 0.14 to 0.99, held-out 0.94 to 0.99. The hybrid's only remaining shortfall after repair is multi-hop
    (0.86 vs 0.99).
11. **On RULER the control was already at the ceiling for numeric multi-key, so the hybrid's gains there are repair,
    not familiarity.** Pooled over seeds (control n = 100, hybrid n = 150) at 32K:

    | RULER task | control before | control after | hybrid before | hybrid after |
    |---|---:|---:|---:|---:|
    | multikey_1 | 0.94 | 0.96 | 0.56 | 0.81 |
    | multikey_2 | 0.72 | 0.97 | 0.26 | 0.49 |
    | multikey_3 (UUID) | 0.40 | 0.57 | 0.16 | 0.19 |
    | multivalue | 0.46 | 0.37 | 0.02 | 0.12 |
    | multiquery | 0.48 | 0.50 | 0.00 | 0.05 |

    At 16K the hybrid recovers more (multikey_1 0.85, multikey_2 0.86, multivalue 0.62, multiquery 0.49) while the
    control *drops* on multivalue (0.74 to 0.57) and multiquery (0.64 to 0.54).
12. **The repair format has a side effect: single-answer training hurts multi-answer questions.** The control's drop on
    multivalue and multiquery, and the hybrid's weak recovery on them, follow from a training mix in which every
    question has exactly one value. This is the third instance of the coverage rule (after multi-hop and UUIDs), and it
    is a cost, not a footnote: a production repair mix must include multi-answer questions.
13. **Damage is a property of the recipe, not of hybrids.** Control after training: ARC-Easy 0.746 to 0.736 / 0.732,
    HellaSwag 0.520 to 0.520 / 0.518 (within SE), bits per byte 1.064 to 1.070 / 1.068 (+0.4-0.6%), the same small cost
    the hybrid pays.

## Verdicts against docs/robustness.md (2B)
- Item 1 (power): headline gaps ≥ 3 SE at n = 100; three seeds agree. **Met.** Prediction 1 was wrong in direction.
- Item 2 (RULER): RULER detects the failure. **No detection advantage**, as pre-registered. Prediction 2 confirmed.
- Item 5 (coverage): multi-hop regression removed by the v2 mix. **Met**, with a new gap found (multi-answer questions).
- Item 6 (damage): ARC/HellaSwag flat; bpb +0.4-0.6% in both models. **Met with a stated cost.**
- Item 7 (alternatives): merge exact; chat-template check inapplicable to base models; generation deterministic. **Met.**
- Items 3, 9 (length generalisation, 8B): decided by jobs 1091447-1091449 (8B base x2, 8B repair trained ≤16K).

## 8B pair, base stage (item 9): the signature at scale, on fresh suites and on RULER

14. **Fresh suites, n = 100 per cell.** Mamba-in-the-Llama 8B vs Llama-3.1-8B-Instruct, the model it was initialised from:

    | task | 16K hybrid | 16K Llama | 32K hybrid | 32K Llama |
    |---|---:|---:|---:|---:|
    | needle | 1.00 | 1.00 | 1.00 | 1.00 |
    | many_random | 0.25 | 0.99 | 0.25 | 0.99 |
    | many_similar | 0.11 | 0.95 | 0.09 | 1.00 |
    | updated | 0.42 | 0.87 | 0.16 | 0.74 |
    | multihop | 0.15 | 0.63 | 0.06 | 0.49 |
    | heldout_many (parcels) | 0.33 | 1.00 | 0.17 | 1.00 |

15. **RULER at 16K, n = 50.** Hybrid vs Llama-3.1-8B-Instruct: single_1 1.00 / 1.00, multikey_1 0.72 / 1.00, multikey_2
    0.40 / 1.00, multikey_3 (UUID) 0.10 / 0.98, multivalue 0.32 / 0.91, multiquery 0.14 / 1.00. At 32K the hybrid is at
    0.40 / 0.10 / 0.00 / 0.00 / 0.00 on the five multi-key variants with single_1 still 1.00 (Llama's 32K rows pending).
16. **Reading.** This conversion keeps half its attention layers and still collapses from 4K, far earlier than Jet-Nemotron-2B
    with two of 28. Attention-layer count alone does not predict the deficit; Lizard's 50%-softmax conversion reported parity.
    Whatever the conversion's training did or did not teach matters more than how many softmax layers survive.
    The repair (job 1091466, trained at <= 16K, evaluated to 32K) is the test of whether that can be fixed post hoc at 8B.

17. **Llama-3.1-8B-Instruct on RULER at 32K (n = 50): 1.00 / 1.00 / 0.96 / 0.98 / 1.00** on multikey_1/2/3, multivalue,
    multiquery, against the hybrid's 0.40 / 0.10 / 0.00 / 0.00 / 0.00. The 8B conversion's RULER deficit is total.
18. **Base damage baselines, 8B.** Hybrid: ARC-Easy 0.848 / 0.804, HellaSwag 0.600 / 0.778, bits per byte 1.008 at 16K.
    Llama-3.1-8B-Instruct: 0.808 / 0.748, 0.598 / 0.768, bits per byte 0.800. The conversion itself costs 26% in long-text
    bits per byte relative to the model it came from, a cost the repair cannot be expected to recover.

## 8B repair, trained at <= 16K, evaluated at 32K (item 3, length generalisation): interim, first suite only

19. **The repair generalises past its training length.** At 32K, which the adapter never saw (about 20 cases per cell so far):

    | task at 32K | 8B hybrid before | after repair (<= 16K training) |
    |---|---:|---:|
    | needle | 1.00 | 1.00 |
    | many_random | 0.25 | 0.95 |
    | many_similar | 0.09 | 0.87 |
    | updated | 0.16 | 1.00 |
    | multihop | 0.06 | 0.88 |
    | heldout_many | 0.17 | 0.91 |

    At 16K (trained length) every key task is at 1.00. Prediction 3 (>= 0.7 at 32K) is exceeded. Full counts, the
    second suite, RULER after repair and the damage checks follow when job 1091466 completes.

## 8B repair, final (one seed, trained at <= 16K, 600 docs, lr 2e-4): recall wins, the recipe costs more at 8B

20. **Recall, fresh suites, n = 100 per cell** (hybrid before -> after | Llama-3.1-8B-Instruct):

    | task | 16K | 32K (never trained) |
    |---|---|---|
    | needle | 1.00 -> 1.00 \| 1.00 | 1.00 -> 1.00 \| 1.00 |
    | many_random | 0.25 -> 1.00 \| 0.99 | 0.25 -> **0.98** \| 0.99 |
    | many_similar | 0.11 -> 0.99 \| 0.95 | 0.09 -> **0.91** \| 1.00 |
    | updated | 0.42 -> 1.00 \| 0.87 | 0.16 -> 1.00 \| 0.74 |
    | multihop | 0.15 -> 0.93 \| 0.63 | 0.06 -> 0.85 \| 0.49 |
    | heldout_many | 0.33 -> 0.94 \| 1.00 | 0.17 -> 0.95 \| 1.00 |

    Length generalisation (item 3) holds: trained at <= 16K, the 32K recall reaches the full-attention model's level.
21. **RULER after repair** (hybrid before -> after | Llama), 32K: multikey_1 0.40 -> **1.00** | 1.00; multikey_2 0.10 ->
    **0.96** | 1.00; multikey_3 (UUID) 0.00 -> 0.30 | 0.96; multivalue 0.00 -> 0.42 | 0.98; multiquery 0.00 -> 0.50 | 1.00.
    16K: 1.00 / 0.98 / 0.58 / 0.68 / 0.72. Numeric multi-key recovers fully; UUIDs and multi-answer questions partially,
    the same coverage boundary as at 2B.
22. **Damage at 8B is real and larger than at 2B.** ARC-Easy 0.848 -> 0.836 (acc_norm 0.804 -> 0.776), HellaSwag
    0.600 -> 0.566 (acc_norm 0.778 -> 0.728, about 2 SE), bits per byte on long text 1.008 -> 1.156 (**+15%**, every
    window worse). The same recipe that cost 0.4% at 2B costs 15% of long-text modelling at 8B. Training loss reached
    0.000, so this is over-fitting of a larger model to 11M synthetic tokens; a lighter recipe (fewer documents, lower
    learning rate, or natural text mixed in) is the obvious next run (item 8) and is submitted as `-gentle`.
23. The unmerged-adapter and chat-template checks did not run at 8B (the unmerged check crashed on a layer reading
    `.weight` off the wrapper; fixed in 3787674). Merge exactness stands from the 2B check.

## 8B anti-forgetting runs (item 8), first result: replay reverses the perplexity damage

24. **gentle + replay** (300 docs, lr 5e-5, every other example a War-and-Peace window with full LM loss, weight decay 0.01):
    bits per byte **0.978**, below the unrepaired hybrid's 1.008 (the heavy repair: 1.156); HellaSwag 0.582 / 0.744 and
    ARC-Easy 0.826 / 0.776, within one to two SE of base. Recall on the first suite at 32K: random keys 0.98, similar keys
    0.78, multi-hop 0.26, held-out 0.84: under-trained at this learning rate. So replay removes the damage and even
    recovers part of the conversion's own long-text loss; the remaining question is whether full-strength replay keeps
    recall (run `-replay`, 600 docs, lr 2e-4). `-gentle` (no replay) and `-qk` are pending.

25. **gentle** (300 docs, lr 5e-5, no replay): bits per byte **1.065** (+5.7% vs base; the heavy recipe was +15%), HellaSwag
    0.586 / 0.744, ARC-Easy 0.842 / 0.766 (within one to two SE of base), with full recall at 32K on the fresh suites
    (random keys 1.00, similar 1.00, multi-hop ~0.98, held-out 1.00). Dose alone removes two thirds of the damage at no
    recall cost; replay removes all of it. The full-strength replay run is expected to combine the two.

26. **replay, full strength** (600 docs, lr 2e-4, every other example natural text): bits per byte **0.992** (below base),
    HellaSwag 0.574 / 0.746, ARC-Easy 0.822 / 0.782 (within noise); recall at 32K: random keys 0.99, similar 0.86,
    multi-hop 0.36, held-out 0.92; RULER multikey_1 0.80, multikey_2 0.43, multivalue 0.00. Replay removes the damage
    and halves the retrieval signal: the harder tasks are the ones that go. The two levers oppose each other; the next
    recipe (`-gentle2-replay25`: 800 examples, lr 5e-5, one in four natural) looks for the point that keeps both.

## Verdicts, complete
- Items 1, 2, 5, 6, 7 (2B): as above. Item 3 (length generalisation): **met at 8B**, 32K recall at the full-attention
  level after <= 16K training. Item 9 (8B): the failure signature and the repair both **replicate**, with the damage
  caveat in 22. Item 6 at 8B: **not met** with this recipe; the recall result stands, the "no damage" claim is 2B-only
  until the lighter recipe is measured.
Repair with the v2 mix (multi-hop included), Jet seeds 1-3 and Qwen2.5 seeds 1-2, then the same evaluations plus the
unmerged-adapter and chat-template checks. Items 5, 6, 7 are decided by those.

## Notes
- The n = 50 suites include `heldout_many` as a sixth task (it is in the task registry), so pooled held-out numbers above
  come from 100 fresh cases, not the 25-case exp02 file.
- RULER values are 7-digit numbers and UUIDs; the `contains` rule scores them. `exact` is undefined for that rule.

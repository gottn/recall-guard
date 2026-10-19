# Experiment 2 — can training repair a converted hybrid's long-context recall?

Run: 2026-10-16, AAU `nv-ai-04` (A100-SXM4-40GB), run dir `~/runs/rg/exp02/20261016-132629-5c3e622`, commit `5c3e622`.
Reproduce: `exp02_repair/run_all.sh` (cluster commands in its header; `report` rebuilds `results/tables.md`).

## Verdict

**Yes: 42 minutes of LoRA on one A100 repairs it fully.** Jet-Nemotron-2B went from **0.16 to 0.92** on 16 random keys
at 32K and from **0.20 to 0.88** on near-duplicate keys, matching the full-attention control trained the same way
(0.92 and 0.92). The gain **transfers to a template never trained on** (parcels and pickup codes: 0.24 to 0.84 at
32K) and **ARC-Easy and HellaSwag do not move** (all deltas within one standard error of 0.022).

Reading: the converted model's fixed-size state had the capacity for 16 keys at 32K all along. The conversion
left its linear-attention layers untrained for long-range multi-key retrieval, and 0.75% of the parameters
(every linear projection outside the MLPs) learned it from 11M synthetic tokens.

**One regression.** Multi-hop, which the repair data never asked, fell from about 0.20 to about 0.03. The repaired
model answers 124 of 150 multi-hop questions with the person's name, the one-hop value next to the locker key.
That is a learned shortcut, not lost capacity (the control's multi-hop rose from 0.16 to 0.31 on the same data),
and it means repair data must cover the question types of the workload.

**Correction to exp01.** The "hybrids beat full attention on overwritten facts" surprise is downgraded: after training,
the full-attention control scores 1.00 on `updated` at every length. Its earlier deficit was a prompt-following habit
of the base model (echoing the first assignment), not a memory property.

## Recall (contains), n = 25 per cell; before = exp01 / base stage, after = with the merged adapter

| model | task | 1K | 2K | 4K | 8K | 16K | 32K |
|---|---|---:|---:|---:|---:|---:|---:|
| Jet before | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Jet after | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Jet before | many_random | 1.00 | 0.92 | 0.88 | 0.80 | 0.72 | 0.16 |
| Jet after | many_random | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **0.92** |
| Jet before | many_similar | 1.00 | 1.00 | 0.92 | 0.76 | 0.76 | 0.20 |
| Jet after | many_similar | 1.00 | 0.96 | 1.00 | 1.00 | 1.00 | **0.88** |
| Jet before | updated | 0.92 | 0.56 | 0.68 | 0.84 | 0.84 | 0.60 |
| Jet after | updated | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Jet before | multihop | 0.20 | 0.08 | 0.12 | 0.20 | 0.24 | 0.20 |
| Jet after | multihop | 0.00 | 0.04 | 0.00 | 0.00 | 0.00 | 0.08 |
| Jet before | heldout_many (parcels) | 1.00 | 1.00 | 0.96 | 0.96 | 0.96 | 0.24 |
| Jet after | heldout_many (parcels) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | **0.84** |
| Qwen2.5-1.5B before | many_random | 0.96 | 0.92 | 0.88 | 0.92 | 0.96 | 0.72 |
| Qwen2.5-1.5B after | many_random | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.92 |
| Qwen2.5-1.5B before | many_similar | 0.96 | 0.88 | 0.92 | 0.96 | 0.76 | 0.68 |
| Qwen2.5-1.5B after | many_similar | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.92 |
| Qwen2.5-1.5B before | updated | 0.64 | 0.48 | 0.56 | 0.32 | 0.36 | 0.44 |
| Qwen2.5-1.5B after | updated | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen2.5-1.5B before | multihop | 0.28 | 0.16 | 0.08 | 0.08 | 0.20 | 0.16 |
| Qwen2.5-1.5B after | multihop | 0.40 | 0.44 | 0.40 | 0.40 | 0.40 | 0.28 |
| Qwen2.5-1.5B before | heldout_many (parcels) | 0.96 | 1.00 | 1.00 | 0.92 | 0.92 | 0.88 |
| Qwen2.5-1.5B after | heldout_many (parcels) | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.92 |

General-damage check, 500 items each, standard error 0.022:

| model | ARC-Easy acc | acc_norm | HellaSwag acc | acc_norm |
|---|---:|---:|---:|---:|
| Jet before | 0.764 | 0.728 | 0.506 | 0.632 |
| Jet after | 0.768 | 0.716 | 0.504 | 0.628 |
| Qwen2.5-1.5B before | 0.746 | 0.712 | 0.520 | 0.664 |
| Qwen2.5-1.5B after | 0.748 | 0.700 | 0.520 | 0.662 |

## Method

- Training data: 600 synthetic documents (seed 0) cycling random keys, near-duplicate keys and overwritten keys,
  16-48 keys each (8-24 for overwrites), 8 questions per document, lengths cycling 8K / 16K / 32K; loss only on the
  answer tokens (`recall_guard/train_data.py`). The locker template only; `heldout_many` uses parcels.
- LoRA (`recall_guard/backends/lora.py`, own implementation): rank 16, alpha 32, float32 A/B on every `nn.Linear`
  outside the MLPs, head and embeddings. Jet: 232 layers wrapped, 14.8M of 1.98B parameters (0.75%). Control: q/k/v/o
  of 28 attention layers. AdamW, lr 2e-4, gradient accumulation 4 (150 optimizer steps), gradient checkpointing.
- Cost: Jet 11.47M tokens in 2520 s (42 min), peak 16.2 GB; control 23 min, peak 10.3 GB. Final training loss 0.000 for both.
- Evaluation: the exp01 suite file (byte-identical prompts), the held-out suite (seed 1, 25 cases x 6 lengths),
  ARC-Easy and HellaSwag validation subsets (seed 0). Adapter merged into the weights, so inference cost is unchanged.

## Robustness and limits

- n = 25 per cell (SE about 0.10 at p = 0.5, 0.06 at p = 0.9). The 32K gains (+0.76, +0.68, +0.60 held-out) are far
  outside noise. One seed, one training run per model.
- Training included 32K documents, so this does not test repair beyond the trained length. Train at 16K and test at
  32K / 64K is the next question.
- Training loss reached zero (memorisation of the training distribution), but the held-out template gain shows the
  learned skill is not tied to the locker wording.
- ARC-Easy and HellaSwag are narrow checks of damage; a long-context natural task (summarisation, QA) is not covered.
- Model scale is 2B. The result says nothing yet about 7B+ hybrids.

## Next

1. Length generalisation: train at <= 16K, evaluate at 32K and 64K.
2. Add multi-hop (and other question types) to the repair data; verify the multi-hop regression disappears.
3. Capacity frontier after repair: 32, 64, 128 keys at 32K. Where does the repaired state run out?
4. Scale: LoLCATs-Llama-3-8B or Mamba-in-the-Llama against Llama-3-8B.
5. Step 2: does an ordinary instruction fine-tune undo this (or break an unrepaired hybrid)?

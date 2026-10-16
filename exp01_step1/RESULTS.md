# Experiment 1 — do the stressors separate hybrid from full attention where the needle does not?

Run: 2026-10-16, AAU `nv-ai-04` (A100-SXM4-40GB), run dir `~/runs/rg/step1/20261016-121320-8beb29d`.
Reproduce: `exp01_step1/run_all.sh` (cluster commands in its header; `report` rebuilds `results/tables.md` from `results/raw/*.jsonl`).

## Verdict

**Yes, for the matched pair.** Jet-Nemotron-2B (hybrid: Qwen2.5-1.5B MLPs, attention mostly replaced) and its
full-attention base both score **1.00 on the needle at every length up to 32K**. With 16 planted keys the hybrid
falls to **0.16–0.20 at 32K** while the base holds **0.68–0.72**; the gap opens at 16K for random keys (+0.24).
A needle test passes this model at 32K; the many-key test fails it.

The unmatched pair (Qwen3.5-4B hybrid vs Qwen3-4B full) shows **no key-recall deficit** (the hybrid is at 1.00 on
both many-key tasks at every length, above Qwen3-4B's 0.84 at 32K) but a **multi-hop deficit of 0.24–0.28 at
8K–16K** with the needle flat. Those two models differ in pretraining data, so this is suggestive only.

Two results the design did not predict:

- **Overwritten facts favour the hybrids.** Jet beats its base on `updated` at every length (+0.08 to +0.56), and
  Qwen3.5-4B beats Qwen3-4B at 2K–16K (+0.16 to +0.36). This matches the Stage A finding that delta-rule style
  states overwrite cleanly, but note the full-attention base models show a primacy bias (they echo the first
  assignment), which is a prompt-following property, not a memory-capacity one.
- **Near-duplicate keys were not harder than random keys** for any model at ≤16K (`many_similar` ≈ `many_random`).
  The key-geometry stressor from Stage A did not appear at 16 keys; at 32K Jet collapses on both.

## Recall (contains) by reference length, n = 25 per cell

| model | task | 1K | 2K | 4K | 8K | 16K | 32K |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen2.5-1.5B (full) | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen2.5-1.5B (full) | many_random | 0.96 | 0.92 | 0.88 | 0.92 | 0.96 | 0.72 |
| Qwen2.5-1.5B (full) | many_similar | 0.96 | 0.88 | 0.92 | 0.96 | 0.76 | 0.68 |
| Qwen2.5-1.5B (full) | updated | 0.64 | 0.48 | 0.56 | 0.32 | 0.36 | 0.44 |
| Qwen2.5-1.5B (full) | multihop | 0.28 | 0.16 | 0.08 | 0.08 | 0.20 | 0.16 |
| Jet-Nemotron-2B (hybrid) | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Jet-Nemotron-2B (hybrid) | many_random | 1.00 | 0.92 | 0.88 | 0.80 | 0.72 | **0.16** |
| Jet-Nemotron-2B (hybrid) | many_similar | 1.00 | 1.00 | 0.92 | 0.76 | 0.76 | **0.20** |
| Jet-Nemotron-2B (hybrid) | updated | 0.92 | 0.56 | 0.68 | 0.84 | 0.84 | 0.60 |
| Jet-Nemotron-2B (hybrid) | multihop | 0.20 | 0.08 | 0.12 | 0.20 | 0.24 | 0.20 |
| Qwen3-4B (full) | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen3-4B (full) | many_random | 0.96 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 |
| Qwen3-4B (full) | many_similar | 1.00 | 0.96 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen3-4B (full) | updated | 0.96 | 0.68 | 0.56 | 0.72 | 0.64 | 0.92 |
| Qwen3-4B (full) | multihop | 0.80 | 0.64 | 0.52 | 0.68 | 0.68 | 0.44 |
| Qwen3.5-4B (hybrid) | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen3.5-4B (hybrid) | many_random | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen3.5-4B (hybrid) | many_similar | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen3.5-4B (hybrid) | updated | 1.00 | 1.00 | 0.92 | 0.88 | 0.88 | 0.76 |
| Qwen3.5-4B (hybrid) | multihop | 0.76 | 0.52 | 0.36 | 0.44 | 0.40 | **0.36** |

Verdict rule (first length where full − hybrid ≥ 0.20 and |needle gap| < 0.20), computed by `recall_guard.aggregate.separations`:

| hybrid | full | task | first length | full − hybrid |
|---|---|---|---:|---:|
| Jet-Nemotron-2B | Qwen2.5-1.5B | many_random | 16K | +0.24 |
| Jet-Nemotron-2B | Qwen2.5-1.5B | many_similar | 32K | +0.48 |
| Qwen3.5-4B | Qwen3-4B | multihop | 8K | +0.24 |

Full per-cell rows (exact and stale rates, wall seconds) are in `results/tables.md`.

## Method

- Suite: 5 tasks × 6 lengths × 25 cases = 750 prompts, generated once at commit `8beb29d` (seed 0, sized with the
  Qwen2.5-1.5B tokenizer; `results/suite.prov.json`). Every model saw byte-identical prompts.
- Tasks: `needle` (1 key), `many_random` / `many_similar` (16 keys, unrelated vs near-duplicate), `updated` (8 keys,
  each overwritten once; answer is the latest value), `multihop` (8 locker→person→code chains). Values are
  six-digit codes; filler has no digits.
- Decoding: completion-style prompt, no chat template, greedy, 32 new tokens, bf16, SDPA. Models whose tokenizer
  has a `<think>` token (Qwen3, Qwen3.5) get the official empty block `<think>\n\n</think>\n\n` prefilled.
- Scoring: `contains` = answer among six-digit codes on the first visible line (think blocks stripped);
  `stale` = a planted distractor appears instead.
- Cost: 0.2–4 s per case on one A100; 25–45 min per model. Jet-Nemotron needs its own venv
  (transformers 4.53, jet-ai fla fork) and `TRITON_LIBCUDA_PATH` inside singularity.

## Robustness

- n = 25 per cell: binomial SE ≈ 0.10 at p = 0.5, ≈ 0.04 at p = 0.96. The 32K gaps (+0.48, +0.56) exceed 4 SE.
  The 16K gap (+0.24) is ≈ 2.4 SE and needs n = 100 to be called.
- One seed, one suite. No variation of key count or depth yet.
- Every long-context miss inspected (≥16K, all models) was a well-formed answer carrying another planted code,
  not a formatting failure.

## Failures and corrections during the run

- Qwen3.5-4B opened every completion with `<think>` and scored 0 at 1K; the run was discarded and rerun with the
  empty-block prefill (both 4B models rerun so the pair shares one regime).
- The `updated` question originally omitted "current"; base models echoed the first assignment (stale rate 1.00
  in the smoke). Fixed before the step 1 suite was generated.
- Multi-hop is near floor (≤ 0.28) for both 1.5–2B models, so that task has no power at small scale.
- Cluster traps (ENV collision, Triton libcuda, QOS, self-updating submit script, temp-file race) are in STATE.md.

## Next

1. Confirm the 16K gap: n = 100 at 16K and 32K for the Jet pair, three seeds (≈1 h of A100).
2. Capacity curve: vary keys (16 → 32 → 64) and extend Jet to 64K (its trained length).
3. A second matched pair: LoLCATs-Llama-3-8B or Mamba-in-the-Llama vs Llama-3-8B (fits one A100-40GB in bf16).
4. Then step 2: fine-tune a hybrid and use this suite as the before/after recall metric.

# Experiment 14: does pinning the kernel configurations make the two layouts agree?

**Verdict: pending.** The outcomes below were written on 2026-11-18 before any run; the Results section is filled in only
from `results/raw` by `run_all.sh report`.

## Question
exp13 found that the first prompt a process decodes sets the path of its 32K answers, and that one autotuned kernel
(`l2norm_fwd_kernel`) keeps a different configuration in processes that start at 16K and at 32K. That is a correlation
over four processes. If the kept configuration is the cause, then a decode in which no kernel is tuned by timing must
give the same 32K answers whatever the process decoded first.

## The pin
`hf.pin_autotune` (called by `cli run` before the model loads) replaces `triton.autotune` so that every kernel imported
afterwards is offered only the first configuration of its list. Triton then times nothing and prints no autotuning line.
All 138 autotuned kernels of the `fla` fork go through `triton.autotune`; Jet's own convolution kernels are not
autotuned. For the l2norm kernel the first configuration is BT 8 with 1 warp, the one the processes starting at 16K kept.

## Method
- **Model, cases, decoding.** As exp12 and exp13: Jet-Nemotron-2B with exp05's realmix seed 2 adapter, the 200 RULER
  multi-answer cases (`~/data/rg/ruler-mvmq/ruler-mvmq.jsonl`), `--max-new-tokens 64`, greedy.
- **Jobs.** Two, `step1.sbatch` through `infra/cluster/submit.sh` at the commit that holds the pin, one process each, on an
  A40 of a256-a40-04, with `TRITON_PRINT_AUTOTUNING=1`:
  - **pin32**: the 100 cases at 32K alone (`--lengths 32768`), so the first prompt has 32K tokens;
  - **pinmix**: all 200 cases, so the process decodes the 16K cases first (`cli run` sorts by length).
- **Comparison**, exact, on output strings: pin32 against the 32K half of pinmix. Unpinned, the same two layouts differ in
  28 of 100 (exp13: only32 against cap64).

## Outcomes, pre-registered
- **pinned**: pin32 and the 32K half of pinmix are identical in 100 / 100. The kept configuration was the cause, and a
  decode no longer depends on the first prompt.
- **not pinned**: at least one output differs. If a log still prints autotuning lines, the pin missed those kernels and
  they are named; if neither does, the cause lies outside the autotuned kernels and exp13's reading is wrong.
- Reported, not criteria: the autotuning lines in the two logs (none expected) and the line the pin prints; which stored
  path the pinned answers follow at 32K (S, the stored run, or C, exp12's cap64); the 16K half of pinmix against the
  stored run; verdicts; seconds per case against the unpinned runs.

Expectation, not a criterion: pinned 0.85. Given pinned, the 32K answers equal C in 100 / 100 with 0.60, because the
l2norm kernel's first configuration is the one C's process kept and the other differing kernels looked neutral in exp13.

## What follows
- **pinned**: the pin stays. Runs from this commit on can be compared across layouts; a run from before it can be
  compared with a newer one only at a length where both followed the same path. The README says so in one sentence.
  Then one pair of layouts on the 8B model, whose kernels (env `mil`) the pin also reaches but which nothing has tested.
- **not pinned**: the pin is removed again, and the two paths are documented as a property of the layout.

## Limits
One adapter, one node, RULER multi-answer cases, two layouts. The pin trades speed for repeatability: the first
configuration is not the fastest one.

## Results
Pending. Submitted 2026-11-18 at 0416769: pin32 1184260, pinmix 1184261. Departure from the method above: the jobs are
not held to a256-a40-04, whose three GPUs were booked for about 20 more hours; the nodes are reported. Then
`run_all.sh report`.

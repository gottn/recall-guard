# Experiment 13: does what a process decodes first set the path of its 32K answers?

**Verdict: pending.** The outcomes below were written on 2026-11-11 before any run; the Results section is filled in only
from `results/raw` by `run_all.sh report`.

## Question
exp12 found that a rerun reproduces itself, while the stored run differs from the reruns in 28 of 100 outputs at 32K and
in none at 16K. Six of the seven adapters stored on A40s show that split; budget seed 3 shows its mirror. The layouts
differ: the stored job decodes each length's RULER file (six variants, 300 cases) in a process of its own, and the reruns
decode 100 cases at 16K and then 100 at 32K in one process. Is the 32K path set by the layout, and by which part of it:
what the process decoded first, or the other variants in the file?

## Mechanism suspected, read from the code (no run)
The linear-attention kernels of the `jet` environment (`fla`, written in Triton) are autotuned. At a kernel's first call
in a process, Triton times a list of configurations and keeps the fastest for the rest of that process
(`fla/ops/common/chunk_delta_h.py`: `BV` 32 or 64, 2 or 4 warps, 2 to 4 stages; the key `H, K, V, BT, USE_G` holds no
sequence length). A process whose first prompt has 16K tokens and one whose first prompt has 32K can keep different
configurations. That would change rounding, and so near-tied tokens, in every later case. A choice made by timing can
also flip now and then, which is what budget seed 3 looks like. `recall_guard` itself keeps nothing between cases
(`backends/hf.complete` calls `generate` once per case).

## Method
- **Model.** Jet-Nemotron-2B with exp05's realmix seed 2 adapter, as in exp12.
- **Decoding.** `--max-new-tokens 64`, greedy, completion prompt: the stored settings.
- **Jobs.** Four, `step1.sbatch` through `infra/cluster/submit.sh` at origin/main 3e4d01f (no code change), one process
  each, on an A40 of a256-a40-04 (the node of the stored run and of exp12):
  - **full16**: `~/data/rg/ruler/ruler-16384.jsonl`, the stored 16K file, 300 cases;
  - **full32**: `~/data/rg/ruler/ruler-32768.jsonl`, the stored 32K file, 300 cases;
  - **only32**: the 100 multi-answer cases at 32K alone (`ruler-mvmq.jsonl` with `--lengths 32768`);
  - **rev**: the 200 multi-answer cases with the 32K half first (`ruler-mvmq-rev.jsonl`, lines kept byte for byte).
- `TRITON_PRINT_AUTOTUNING=1` is set in every job, so the logs name the configuration each kernel keeps. It is the one
  departure from the stored job; it prints and does nothing else.
- **Comparisons**, exact, on output strings: S is the stored run (exp05 job 1152548), C is exp12's cap64.

## Outcomes, pre-registered
- **not layout**: full32 differs from S in at least one of the 100 multi-answer cases at 32K. The stored path does not
  follow from the layout, and the rest is reported without a reading.
- Otherwise the layout reproduces the stored run, and only32 names the part:
  - **first prompt**: only32 matches S in 100 / 100. The other variants do not matter; the 16K cases decoded first do.
  - **composition**: only32 matches C in 100 / 100. The other variants in the file set the path.
  - **mixed**: anything else.
- rev, read separately: **one state per process** if its 32K half matches S in 100 / 100 and its 16K half differs from S
  in at least 10 of 100 (budget seed 3's mirror, made on purpose); **one state per length** if both halves match S;
  otherwise reported.
- Reported, not criteria: full16 and full32 against S on all 300 cases, the nodes, the verdicts each comparison moves,
  and the autotune lines of the four logs (which kernel keeps a different configuration in a process that starts at
  16K and in one that starts at 32K).

Expectation, not a criterion: first prompt 0.55, not layout 0.25, mixed 0.15, composition 0.05. For rev: one state per
process 0.50, one state per length 0.20, other 0.30.

## What follows
- **first prompt**, with different configurations in the logs: the autotuner sets the path. Pin one configuration per
  kernel in the `jet` backend, show that both layouts then give the same outputs, and record it in the result rows.
  Until then `check` compares only files decoded in the same layout.
- **composition** or **mixed**: something carries over between cases. Find it in the model code before any new
  comparison.
- **not layout**: the stored 32K outputs cannot be reproduced. Single-run comparisons at 32K (exp05-exp07) carry up to 5
  verdicts of 100, and a recipe comparison needs each arm decoded twice.

## Limits
One adapter, one node, RULER multi-answer cases. The 8B model runs other kernels (env `mil`) and is not tested here.

## Results
Pending. Submitted 2026-11-11 at 3e4d01f, pinned to a256-a40-04: full16 1163668, full32 1163672, only32 1163673, rev
1163674; `ruler-mvmq-rev.jsonl` has sha256 bf32921339a0deae.... Then `run_all.sh report`.

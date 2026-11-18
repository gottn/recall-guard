# Experiment 13: does what a process decodes first set the path of its 32K answers?

**Verdict (2026-11-18): first prompt.** The stored layout reproduces the stored run in 300 of 300 outputs at both lengths,
and the 100 multi-answer cases at 32K decoded alone give the stored answers in 100 of 100. So the path of the 32K answers
is set by what the process decodes first, not by the other variants in the file. The logs name the suspected mechanism:
the l2norm kernel keeps one configuration when the process starts at 16K (BT 8, 1 warp) and another when it starts at 32K
(BT 16, 16 warps), and it is the only one of nine autotuned kernels whose configuration follows the outputs. The rev arm
is void: `cli run` decodes shortest first, so it repeated cap64's layout. The outcomes below were written on 2026-11-11
before any run; the Results section is filled in only from `results/raw` by `run_all.sh report`, plus `sacct`.

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
Jobs 1163668 (full16, 23 min), 1163672 (full32, 31 min), 1163673 (only32, 10 min) and 1163674 (rev, 16 min) completed on
2026-11-11 at 3e4d01f, all on a256-a40-04 (`sacct`); `ruler-mvmq-rev.jsonl` has sha256 bf32921339a0deae.... Pulled
2026-11-18; the sha256 of the four result files and the four `autotune.txt` matches the cluster.

| comparison | outputs identical | verdicts that differ |
|---|---|---|
| full16 against S, all six variants | 300 / 300 | 0 |
| full32 against S, all six variants | 300 / 300 | 0 |
| full32 against C, multi-answer | 72 / 100 | 3 |
| only32 against S | 100 / 100 | 0 |
| only32 against C | 72 / 100 | 3 |
| rev, 32K half against S | 72 / 100 | 3 |
| rev, 32K half against C | 100 / 100 | 0 |
| rev, 16K half against S | 100 / 100 | 0 |

**Outcome: first prompt**, by the rule.
- The stored layout reproduces the stored run on every case of both files. The stored answers are not an accident of
  that job or that date, and `TRITON_PRINT_AUTOTUNING` changed nothing.
- The 100 cases at 32K alone give the stored answers too, so the other RULER variants do not matter. What matters is
  whether the process decoded 16K cases before them.

**rev is void as a test of order.** `cli run` decodes a file shortest prompt first (`sorted(todo, key=ref_tokens)` in
`cmd_run`), whatever the order of its lines. rev therefore ran its 16K half first: it is cap64's layout a third time,
and it reproduces cap64 in 200 of 200. The rule reads it as "other", but the rule assumed the file's order. No job here
starts at 32K and then decodes 16K, so "one state per process" against "one state per length" is not tested by outputs.
The arm was designed without reading `cmd_run`.

### The kernel configurations (`autotune.txt`, printed by Triton)
Each process autotunes nine kernels, once. Three keep the same configuration in all four jobs. Six do not, and one of
those follows the outputs:

| | full16 | rev | full32 | only32 |
|---|---|---|---|---|
| first prompt decoded | 16K | 16K | 32K | 32K |
| `l2norm_fwd_kernel` | BT 8, 1 warp | BT 8, 1 warp | BT 16, 16 warps | BT 16, 16 warps |
| `chunk_fwd_kernel_o` | BK 32 | BK 64 | BK 32 | BK 64 |
| path of its 32K answers | - | C | S | S |

- The l2norm key is `(96, 1, bfloat16, bfloat16)`. Its second entry is a size bucket (rows / `autotune_interval`), and
  Jet passes an interval of 524,288 rows, so both lengths fall in bucket 1 and one tuning serves the whole process.
- The other five are excluded. full32 and only32 give identical outputs although `chunk_fwd_kernel_o` (BK 32 / 64),
  `chunk_local_cumsum_scalar_kernel`, `chunk_scaled_dot_kkt_fwd_kernel` and `merge_16x16_to_64x64_inverse_kernel`
  (warps, stages) differ between them. full16 and rev give identical 16K outputs although `chunk_fwd_kernel_o`, the
  cumsum, the kkt and `solve_tril_16x16_kernel` differ.
- The reading: the first prompt decides which l2norm configuration wins the timing, and that configuration sets the
  rounding of every later case. This is a correlation over four processes with the other kernels excluded. The proof
  is the pinned decode under Next.

## What it means
- Jet-Nemotron-2B's answers have two paths, and a process takes one of them at its first (shortest) prompt. At 32K
  the paths differ in 28-36 outputs of 100 and in 0-5 verdicts of 100 (exp12).
- Decodes of one suite file start at the same prompt, so base against adapter on the same file is like for like, as
  in exp01-exp08. A filtered decode against a full one is not, and neither is a resumed decode: it starts at a longer
  prompt than the run it continues.
- exp12's budget seed 3 stays the one pair where the same layout gave the other path. A timing choice can flip; none of
  the four processes here did.

## Next
- Pin one configuration per autotuned kernel in the `jet` backend, then decode only32 and cap64's layout again. The
  32K outputs must then agree in 100 of 100. That is both the test of the reading and the fix.
- The 8B model (env `mil`) runs other Triton kernels. One pair of decodes in two layouts tells whether it has paths.

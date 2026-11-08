# Experiment 12: does a rerun reproduce the stored answers?

**Verdict: pending.** The outcomes below were written on 2026-11-08 before any run; the Results section is filled in only
from `results/raw` by `run_all.sh report`.

## Question
exp11 re-decoded 2,200 stored RULER multi-answer cases with 192 new tokens instead of 64. 505 outputs left the stored
greedy path within the first value or two, and 37 verdicts moved (19 up, 18 down) with no change to any model. For realmix
seed 2, 28 of 200 outputs diverged although the two runs share the node (a256-a40-04), the GPU model (A40), the evaluation
path (`cli run --adapter`, one case at a time) and the code (nothing in `recall_guard/`, `infra/` or `pyproject.toml`
changed between 26d25e8 and 3e4d01f). What is left:
- **noise**: a rerun with identical settings does not reproduce itself;
- **token limit**: `--max-new-tokens` changes the computation before the cap;
- **surroundings**: what else differed between the runs. The stored run decoded each length's full RULER file (six
  variants) in its own process; exp11 decoded the 200 filtered cases in one process; the environment may have been rebuilt.

`check` compares two runs, so the gate has to know which of these moves verdicts. exp03 found 150 of 150 completions
identical across runs (STATE.md); exp11 is the first comparison at 16K-32K with a changed token limit.

## Method
- **Cases.** The exp11 file `~/data/rg/ruler-mvmq/ruler-mvmq.jsonl` (200 cases, sha256 f0ddab0152f83713...), unchanged.
- **Model.** Jet-Nemotron-2B with exp05's realmix seed 2 adapter
  (`~/runs/rg/robust/20261101-183230-8b5abb6/adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix`).
- **Jobs.** Two, `step1.sbatch` through `infra/cluster/submit.sh` at 3e4d01f, A40, everything else as exp11:
  - **rerun192**: exp11's realmix seed 2 job again, `--max-new-tokens 192`;
  - **cap64**: the same with `--max-new-tokens 64`.
- **Comparisons**, exact, on output strings and verdicts:
  - rerun192 against exp11's run (job 1155282, 192 tokens);
  - cap64 against the stored run (exp05 job 1152548, 64 tokens; `exp05_realmix/results/raw/damage/ruler-{16384,32768}-repair-seed2-realmix-*.jsonl`, filtered to the two tasks);
  - cap64, and the stored run, as prefixes of exp11's output.
- Nodes come from `sacct` and are reported.

## Outcomes, pre-registered
- **noise**: rerun192 differs from exp11's output in at least one of 200 cases. A rerun with identical settings does not
  reproduce itself; the verdicts it moves are the noise floor a gate has to allow.
- **token limit**: rerun192 matches exp11 in 200 / 200, and cap64 matches the stored run in 200 / 200. The token limit alone
  moves the greedy path.
- **surroundings**: rerun192 matches exp11 in 200 / 200, cap64 differs from the stored run, and cap64 is a prefix of exp11's
  output in 200 / 200. The token limit does not matter; the file composition, the process history or the environment does.
- **mixed**: anything else.
- Reported, not criteria: the nodes, the verdicts each comparison moves, and where outputs diverge.

Expectation, not a criterion: token limit 0.45, noise 0.25, surroundings 0.20, mixed 0.10.

## What follows
- **noise**: `check` needs a noise floor. Run the baseline twice, and count a cell as dropped only beyond the discordance
  between the two baseline runs. The single-run comparisons of exp05-exp11 carry that noise.
- **token limit**: runs reproduce when decoding settings match. Result rows should record `max_new_tokens`, and `check`
  should refuse to compare files decoded with different settings. exp11's 64-against-192 reading stays valid on the stored
  path only, as it was read.
- **surroundings**: one more job, the full RULER files at 64 tokens as `robust.sbatch` runs them, to find which.
- **mixed**: reported; no change.

## Results
Pending: job ids, then `run_all.sh report`.

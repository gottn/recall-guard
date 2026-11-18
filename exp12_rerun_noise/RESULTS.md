# Experiment 12: does a rerun reproduce the stored answers?

**Verdict (2026-11-11): surroundings.** A rerun with identical settings reproduces itself: rerun192 matches exp11's run in
200 of 200 outputs. The token limit does not move the greedy path: cap64 is a prefix of exp11's output in 200 of 200. The
stored run is the odd one: cap64 differs from it in 28 outputs and 3 verdicts. So the 28 divergences exp11 found for this
adapter are neither noise nor `--max-new-tokens`; they come from what else differed between the stored job and the reruns.
Post-hoc: all 28 are 32K cases, and six of the seven adapters stored on A40s show the same split against exp11. The
expectation (token limit 0.45) was wrong. The outcomes below were written on 2026-11-08 before any run; the Results section
is filled in only from `results/raw` by `run_all.sh report`, plus `sacct` and the job logs where named.

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
Jobs 1155969 (rerun192, 38 min) and 1155970 (cap64, 18 min) completed on 2026-11-08 at 3e4d01f, both on a256-a40-04, an
A40. exp11's job 1155282 and the stored exp05 job 1152548 ran on the same node (`sacct`). Pulled 2026-11-11; the sha256 of
both result files matches the cluster.

| comparison | outputs that match | verdicts that differ |
|---|---|---|
| rerun192 against exp11's run (192 tokens), identical | 200 / 200 | 0 |
| cap64 against the stored run (64 tokens), identical | 172 / 200 | 3 |
| cap64 as a prefix of exp11's output | 200 / 200 | 5 |
| the stored run as a prefix of exp11's output | 172 / 200 | 8 |

**Outcome: surroundings**, by the rule.
- Not noise. Two jobs with the same settings on the same node give the same 200 outputs, character for character.
- Not the token limit. The 64-token output is the start of the 192-token one in every case. The 5 verdicts that differ
  between them are multi-query answers at 16K that the cap cut (0.40 at 64 tokens, 0.50 at 192), which exp11 counted.
- The stored run differs from all three reruns in the same 28 cases, at a median of 32 characters in. The 3 verdicts it
  moves are hits the reruns lose, all at 32K (multi-value 0.10 -> 0.08, multi-query 0.06 -> 0.02).

### Post-hoc, 2026-11-11 (not pre-registered; `run_all.sh report` prints the counts)
- **All 28 are 32K cases** (22 multi-query, 6 multi-value). The 100 cases at 16K are identical to the stored run.
- **The split is not this adapter's.** exp11's runs against their stored ones by the prefix test, outputs that diverge of
  100 per length:

  | stored on | variant | 16K | 32K |
  |---|---|---|---|
  | A40 | realmix seeds 1 / 2 / 3 | 0 / 0 / 0 | 33 / 28 / 34 |
  | A40 | budget seeds 1 / 2 / 3 | 0 / 0 / **33** | 36 / 34 / **0** |
  | A40 | syn1200 | 0 | 32 |
  | A100 | base; synthetic seeds 1 / 2 / 3 | 34; 32 / 36 / 23 | 33; 43 / 41 / 33 |

  Six of the seven A40 adapters reproduce every 16K output and lose about a third of the 32K ones. Budget seed 3 is the
  mirror image. A change of GPU model moves both lengths. These are exp11's 505 divergences: 158 at 16K, 347 at 32K.
- **Excluded.** The node: three of the six pairs changed node (a256-a40-05 to -07, -07 to -06, -06 to -04) and three did
  not, with the same split. The environment: `~/pydeps/rg-jet` dates from 2026-10-16, the container image from 2025-10-20,
  and both logs print torch 2.9.0a0+50eac811a6.nv25.09. The evaluation path: both are `cli run --adapter`, merged, with
  the same job settings. Resumed jobs: one process wrote every stored and rerun file ("0 already in"). File composition
  at 16K: the stored 16K file interleaves six RULER variants, the rerun file holds two, and the outputs are identical.
- **What is left for the 32K cases.** In the stored jobs a fresh process decodes the 32K file. In exp11 and exp12 the 32K
  cases follow 100 cases at 16K in the same process. Either what a process decoded earlier changes its 32K computation,
  or the other variants in the stored 32K file do. Neither explains budget seed 3. One state per process, fixed at its
  start, would explain it with a single event; nothing here tests that.

## What it means for the gate
- A rerun in the same layout needs no noise floor: 200 of 200 (one adapter, one node).
- Two runs of one model in different layouts are not the same measurement at 32K: 28-36 outputs of 100 differ and 0-5
  verdicts of 100 move. `check` should compare only files decoded the same way: the same suite file, one process per
  file. Result rows record neither.
- exp11 compared its arms on the new runs only, all in one layout, so its readings stand. The stored comparisons of
  exp05-exp07 share the stored layout, but budget seed 3 shows that one layout does not guarantee one path.

## Next
Three decodes at 64 tokens with this adapter, pre-registered before they run, to tell process history from file
composition: the full RULER files as `robust.sbatch` runs them (the follow-up named above; it should reproduce the stored
run), the 100 cases at 32K alone, and the 200 cases with the 32K half first.

2026-11-18: exp13 ran them. The first prompt a process decodes sets the path, through the configuration the l2norm
kernel keeps from its autotuning (exp13_decode_layout/RESULTS.md).

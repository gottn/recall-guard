# Style: functional code, structured commits

## Code

1. **Pure by default.** A function's output depends only on its arguments. No hidden state, no module-level mutables, no mutation of arguments. Return new objects (frozen dataclasses, tuples).
2. **Effects at the edges.** File I/O, network, model loading and GPU calls live only in `recall_guard/backends/` and `recall_guard/cli.py`. Everything else runs without a model, a GPU or a disk. `check.sh` greps for this.
3. **Explicit state.** Seeds, tokenizers, paths and devices are parameters. Randomness is a `random.Random(seed)` instance passed in or created from an explicit seed; never the module-level `random.*`.
4. **Compute and write are separate.** A function that returns a table never writes it.
5. **Determinism.** The suite is a data artifact: same `(spec, seed, reference tokenizer)` gives byte-identical JSONL. Every number in a RESULTS.md names the one script that reproduces it.
6. **Units in names.** `ref_tokens`, `wall_s`, `recall_contains`. No bare floats whose unit the reader must guess.
7. **Small, typed, tested.** Type hints on every signature. Pure helpers get a pytest in `tests/`. `./check.sh` passes before every commit.
8. **Minimal.** No classes with behaviour; no abstractions for one call site; standard library first.

## Experiments

- One folder per experiment: `expNN_slug/` with `run_all.sh`, `results/`, `RESULTS.md`.
- RESULTS.md leads with the verdict, then method, table, robustness, failures, next steps.
- Suites and results are dated artifacts with the generating commit recorded. Never regenerate in place; make a new name.

## Commits (Conventional Commits, enforced by `.githooks/commit-msg`)

```
<type>(<scope>): <what changed> — <measured effect when there is one>

<why, in one or two sentences>
<how it was verified>
```

- Types: `feat`, `fix`, `exp`, `data`, `refactor`, `test`, `docs`, `chore`, `perf`, `ci`.
- Scope: `tasks`, `suite`, `score`, `backend`, `cli`, `cluster`, `exp01`, `docs`, `repo`.
- Subject ≤ 100 characters, imperative, no trailing period.
- `exp` and `feat` subjects state the measured effect after ` — `.
- `refactor` subjects state what was proven unchanged.
- One logical change per commit; aim for ≤150 changed lines, 300 hard limit.

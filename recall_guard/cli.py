"""Thin shell: parse arguments, do the I/O, call pure functions.

  generate  --out suite.jsonl --tokenizer Qwen/Qwen2.5-1.5B [--seed 0] [--cases 25] [--lengths ...] [--tasks ...]
  run       --suite suite.jsonl --model <id> --out results.jsonl [--attn sdpa] [--trust-remote-code] [--limit N]
  report    --results a.jsonl b.jsonl [--pair hybrid=full ...] [--out RESULTS.md]
"""

import argparse
import json
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path

from recall_guard.aggregate import gap_markdown, gaps, markdown, pivot_markdown, rows, separation_markdown, separations
from recall_guard.score import to_result
from recall_guard.suite import LENGTHS, SuiteSpec, build_suite
from recall_guard.tasks import TASKS
from recall_guard.types import Case, Result

MAX_NEW_TOKENS = 32  # multihop answers often restate the question first (~14 tokens)


def read_jsonl(path: Path) -> tuple[dict, ...]:
    if not path.exists():
        return ()
    with path.open() as f:
        return tuple(json.loads(line) for line in f if line.strip())


def case_from(d: dict) -> Case:
    return Case(**{**d, "distractors": tuple(d["distractors"])})


def cmd_generate(a: argparse.Namespace) -> None:
    from transformers import AutoTokenizer

    tok = AutoTokenizer.from_pretrained(a.tokenizer)
    spec = SuiteSpec(tuple(a.tasks), tuple(a.lengths), a.cases)
    t0 = time.perf_counter()
    cases = build_suite(spec, a.seed, lambda s: len(tok(s).input_ids))
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_name(f"{out.name}.{os.getpid()}.tmp")  # per-process temp, then rename: parallel jobs never collide
    with tmp.open("w") as f:
        f.writelines(json.dumps(asdict(c)) + "\n" for c in cases)
    tmp.replace(out)
    prov = {"tokenizer": a.tokenizer, "seed": a.seed, "spec": asdict(spec), "cases": len(cases), "wall_s": time.perf_counter() - t0}
    out.with_suffix(".prov.json").write_text(json.dumps(prov, indent=1))
    print(f"wrote {len(cases)} cases to {out} in {prov['wall_s']:.1f}s", file=sys.stderr)


def cmd_run(a: argparse.Namespace) -> None:
    from recall_guard.backends import hf

    cases = tuple(case_from(d) for d in read_jsonl(Path(a.suite)))
    if a.tasks:
        cases = tuple(c for c in cases if c.task in a.tasks)
    if a.lengths:
        cases = tuple(c for c in cases if c.length_bucket in a.lengths)
    cases = cases[: a.limit] if a.limit else cases
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    done = {d["case_id"] for d in read_jsonl(out)}
    todo = tuple(c for c in cases if c.id not in done)
    print(f"{a.model}: {len(todo)} cases to run ({len(done)} already in {out})", file=sys.stderr)
    tok, model = hf.load(a.model, a.attn, a.trust_remote_code)
    prefill = "" if a.allow_think else hf.no_think_prefill(tok)
    print(f"  prefill after Answer: {prefill!r}", file=sys.stderr)
    with out.open("a") as f:
        for i, case in enumerate(sorted(todo, key=lambda c: c.ref_tokens), 1):
            text, wall_s = hf.complete(tok, model, case.prompt, prefill, MAX_NEW_TOKENS)
            r = to_result(case, a.model, text, wall_s)
            f.write(json.dumps(asdict(r)) + "\n")
            f.flush()
            if i % 25 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)} {case.id} contains={r.contains} wall={wall_s:.1f}s", file=sys.stderr)


def cmd_report(a: argparse.Namespace) -> None:
    results = tuple(Result(**d) for p in a.results for d in read_jsonl(Path(p)))
    table = rows(results)
    pairs = tuple(tuple(p.split("=", 1)) for p in a.pair)
    text = "\n\n".join(
        s for s in (
            "## Recall (contains) by reference length\n\n" + pivot_markdown(table),
            "## Verdict rule: first length where a stressor separates the pair and the needle does not\n\n"
            + separation_markdown(separations(table, pairs)) if pairs else "",
            "## Hybrid minus full attention\n\n" + gap_markdown(gaps(table, pairs)) if pairs else "",
            "## All rows\n\n" + markdown(table),
        ) if s
    )
    if a.out:
        Path(a.out).write_text(text + "\n")
    else:
        print(text)


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(prog="recall-guard", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("generate")
    g.add_argument("--out", required=True)
    g.add_argument("--tokenizer", default="Qwen/Qwen2.5-1.5B")
    g.add_argument("--seed", type=int, default=0)
    g.add_argument("--cases", type=int, default=25)
    g.add_argument("--lengths", type=int, nargs="+", default=list(LENGTHS))
    g.add_argument("--tasks", nargs="+", default=sorted(TASKS))
    g.set_defaults(fn=cmd_generate)
    r = sub.add_parser("run")
    r.add_argument("--suite", required=True)
    r.add_argument("--model", required=True)
    r.add_argument("--out", required=True)
    r.add_argument("--attn", default="sdpa")
    r.add_argument("--trust-remote-code", action="store_true")
    r.add_argument("--limit", type=int, default=0)
    r.add_argument("--allow-think", action="store_true", help="do not prefill the empty <think> block")
    r.add_argument("--tasks", nargs="*", default=())
    r.add_argument("--lengths", type=int, nargs="*", default=())
    r.set_defaults(fn=cmd_run)
    t = sub.add_parser("report")
    t.add_argument("--results", nargs="+", required=True)
    t.add_argument("--pair", nargs="*", default=(), help="hybrid=full model id pairs")
    t.add_argument("--out", default="")
    t.set_defaults(fn=cmd_report)
    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()

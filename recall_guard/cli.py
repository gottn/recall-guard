"""Thin shell: parse arguments, do the I/O, call pure functions.

  generate  --out suite.jsonl --tokenizer Qwen/Qwen2.5-1.5B [--seed 0] [--cases 25] [--lengths ...] [--tasks ...]
  run       --suite suite.jsonl --model <id> --out results.jsonl [--adapter DIR] [--attn sdpa] [--trust-remote-code] [--limit N]
  train     --model <id> --out DIR [--n-docs 600] [--lengths 8192 12288 16384] [--lr 2e-4] [--rank 16] [--max-steps N]
  bench     --model <id> [--adapter DIR] [--n 500] --out bench.json
  report    --results a.jsonl b.jsonl [--pair hybrid=full ...] [--out RESULTS.md]
"""

import argparse
import json
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path

from recall_guard.aggregate import (
    gap_markdown,
    gaps,
    markdown,
    pivot_markdown,
    rows,
    separation_markdown,
    separations,
)
from recall_guard.score import to_result
from recall_guard.suite import LENGTHS, SuiteSpec, build_suite
from recall_guard.tasks import TASKS
from recall_guard.types import Case, Result

MAX_NEW_TOKENS = 32  # multihop answers often restate the question first (~14 tokens); RULER multi-value needs 64


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


def add_restore_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--restore-qk", default="", help="hf id of the conversion source: copy its q/k projections into the matching layers (training-free baseline)")
    p.add_argument("--restore-pattern", default="", help="regex on parameter names to restore (default: self_attn q/k weight and bias)")


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
    t0 = time.perf_counter()
    tok, model = hf.load(a.model, a.attn, a.trust_remote_code, a.adapter, a.adapter_mode, restore_from=a.restore_qk, restore_pattern=a.restore_pattern)
    print(f"  loaded in {time.perf_counter() - t0:.0f}s, {hf.peak_memory_gib():.1f} GiB", file=sys.stderr)
    prefill = "" if a.allow_think else hf.no_think_prefill(tok)
    print(f"  prefill after Answer: {prefill!r}; chat={a.chat}; adapter_mode={a.adapter_mode}", file=sys.stderr)
    with out.open("a") as f:
        for i, case in enumerate(sorted(todo, key=lambda c: c.ref_tokens), 1):
            text, wall_s, n_tok = hf.complete(tok, model, case.prompt, prefill, a.max_new_tokens, a.chat)
            tag = ("+qk-restore" if a.restore_qk else "") + (f"+{Path(a.adapter).name}" if a.adapter else "") + ("+unmerged" if a.adapter_mode == "attach" else "") + ("+chat" if a.chat else "")
            r = to_result(case, a.model + tag, text, wall_s, n_tok)
            f.write(json.dumps(asdict(r)) + "\n")
            f.flush()
            if i % 25 == 0 or i == len(todo):
                print(f"  {i}/{len(todo)} {case.id} contains={r.contains} wall={wall_s:.1f}s", file=sys.stderr)
    print(f"  peak GPU memory {hf.peak_memory_gib():.1f} GiB", file=sys.stderr)


def cmd_train(a: argparse.Namespace) -> None:
    from recall_guard.backends.train import TrainConfig, train

    cfg = TrainConfig(a.model, a.out, a.n_docs, tuple(a.lengths), a.seed, a.lr, a.rank, a.alpha, a.grad_accum, a.max_steps, a.trust_remote_code,
                      a.targets, a.weight_decay, a.replay_text, a.replay_frac)
    stats = train(cfg)
    Path(a.out).mkdir(parents=True, exist_ok=True)
    (Path(a.out) / "train_stats.json").write_text(json.dumps({**stats, "config": asdict(cfg)}, indent=1))
    print(f"trained {stats['steps']} steps on {stats['tokens']} tokens in {stats['wall_s']:.0f}s, final loss {stats['final_loss']:.3f}", file=sys.stderr)


def cmd_bench(a: argparse.Namespace) -> None:
    from recall_guard.backends import hf, mc

    tok, model = hf.load(a.model, a.attn, a.trust_remote_code, a.adapter, restore_from=a.restore_qk, restore_pattern=a.restore_pattern)
    out = {b: mc.accuracy(tok, model, mc.load_items(b, a.n, a.seed)) for b in mc.BENCHES}
    out["model"] = a.model + ("+qk-restore" if a.restore_qk else "") + (f"+{Path(a.adapter).name}" if a.adapter else "")
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print(json.dumps(out), file=sys.stderr)


def cmd_import_ruler(a: argparse.Namespace) -> None:
    """RULER generator output (<dir>/<length>/<task>/validation.jsonl) -> one Case JSONL per length."""
    from recall_guard.ruler import to_case

    root = Path(a.dir)
    for length_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        cases = [to_case(t.name, int(length_dir.name), d) for t in sorted(length_dir.iterdir()) for d in read_jsonl(t / "validation.jsonl")]
        out = Path(a.out_dir) / f"ruler-{length_dir.name}.jsonl"
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w") as f:
            f.writelines(json.dumps(asdict(x)) + "\n" for x in cases)
        print(f"wrote {len(cases)} cases to {out}", file=sys.stderr)


def cmd_ppl(a: argparse.Namespace) -> None:
    """Bits per byte on windows of long natural text (a file), one window per --windows, at --window-tokens each."""
    from recall_guard.backends import hf

    tok, model = hf.load(a.model, a.attn, a.trust_remote_code, a.adapter, restore_from=a.restore_qk, restore_pattern=a.restore_pattern)
    text = Path(a.text).read_text()
    step = len(text) // a.windows
    vals = [hf.bits_per_byte(tok, model, text[i * step :], a.window_tokens) for i in range(a.windows)]
    out = {"model": a.model + ("+qk-restore" if a.restore_qk else "") + (f"+{Path(a.adapter).name}" if a.adapter else ""), "window_tokens": a.window_tokens, "windows": a.windows,
           "bpb_mean": sum(vals) / len(vals), "bpb_values": vals, "text": a.text}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print(json.dumps({k: v for k, v in out.items() if k != "bpb_values"}), file=sys.stderr)


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
    r.add_argument("--max-new-tokens", type=int, default=MAX_NEW_TOKENS)
    r.add_argument("--allow-think", action="store_true", help="do not prefill the empty <think> block")
    r.add_argument("--adapter", default="", help="adapter directory (adapter.pt + adapter_config.json)")
    r.add_argument("--adapter-mode", choices=("merge", "attach"), default="merge")
    add_restore_args(r)
    r.add_argument("--chat", action="store_true", help="wrap the prompt in the model chat template")
    r.add_argument("--tasks", nargs="*", default=())
    r.add_argument("--lengths", type=int, nargs="*", default=())
    r.set_defaults(fn=cmd_run)
    tr = sub.add_parser("train")
    tr.add_argument("--model", required=True)
    tr.add_argument("--out", required=True)
    tr.add_argument("--n-docs", type=int, default=600)
    tr.add_argument("--lengths", type=int, nargs="+", default=[8192, 12288, 16384])
    tr.add_argument("--seed", type=int, default=0)
    tr.add_argument("--lr", type=float, default=2e-4)
    tr.add_argument("--rank", type=int, default=16)
    tr.add_argument("--alpha", type=int, default=32)
    tr.add_argument("--grad-accum", type=int, default=4)
    tr.add_argument("--max-steps", type=int, default=0)
    tr.add_argument("--trust-remote-code", action="store_true")
    tr.add_argument("--targets", default="", help="regex on leaf names, e.g. 'q_proj|k_proj'")
    tr.add_argument("--weight-decay", type=float, default=0.0)
    tr.add_argument("--replay-text", default="", help="natural long text; every other example is a window with full LM loss")
    tr.add_argument("--replay-frac", type=float, default=0.5)
    tr.set_defaults(fn=cmd_train)
    b = sub.add_parser("bench")
    b.add_argument("--model", required=True)
    b.add_argument("--adapter", default="")
    add_restore_args(b)
    b.add_argument("--attn", default="sdpa")
    b.add_argument("--trust-remote-code", action="store_true")
    b.add_argument("--n", type=int, default=500)
    b.add_argument("--seed", type=int, default=0)
    b.add_argument("--out", required=True)
    b.set_defaults(fn=cmd_bench)
    ir = sub.add_parser("import-ruler")
    ir.add_argument("--dir", required=True)
    ir.add_argument("--out-dir", required=True)
    ir.set_defaults(fn=cmd_import_ruler)
    pp = sub.add_parser("ppl")
    pp.add_argument("--model", required=True)
    pp.add_argument("--adapter", default="")
    add_restore_args(pp)
    pp.add_argument("--attn", default="sdpa")
    pp.add_argument("--trust-remote-code", action="store_true")
    pp.add_argument("--text", required=True, help="path to a long plain-text file")
    pp.add_argument("--window-tokens", type=int, default=16384)
    pp.add_argument("--windows", type=int, default=8)
    pp.add_argument("--out", required=True)
    pp.set_defaults(fn=cmd_ppl)
    t = sub.add_parser("report")
    t.add_argument("--results", nargs="+", required=True)
    t.add_argument("--pair", action="append", default=[], help="hybrid=full model id pair (repeatable)")
    t.add_argument("--out", default="")
    t.set_defaults(fn=cmd_report)
    a = p.parse_args(argv)
    a.fn(a)


if __name__ == "__main__":
    main()

"""Table bodies for the preprint, computed from the committed raw results and written to paper/tab/*.tex, which
main.tex inputs. Run: .venv/bin/python paper/fig/make_tables.py (or `make tables` in paper/). Rates are rounded
half up to two decimals; a seed mean is the mean of the per-seed rates."""

import glob
import json
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
E3 = ROOT / "exp03_robust/results/raw"
OUT = ROOT / "paper/tab"
JET, QWEN = "jet-ai_Jet-Nemotron-2B", "Qwen_Qwen2.5-1.5B"
MIL, LLAMA = "JunxiongWang_Llama3.1-Mamba2-8B-dpo", "meta-llama_Llama-3.1-8B-Instruct"
SUITE = ("needle", "many_random", "many_similar", "multihop", "heldout_many")
RULER = ("single_1", "multikey_1", "multikey_2", "multikey_3", "multivalue", "multiquery")


def rate(files, task, length):
    k = n = 0
    for f in files:
        for line in open(f):
            r = json.loads(line)
            if r["task"] == task and r["length_bucket"] == length:
                n += 1
                k += r["contains"]
    return k / n


def r2(x):
    return str(Decimal(repr(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def r3(x):
    return str(Decimal(repr(x)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))


def suite(tag, model, task, length=32768):
    return rate(glob.glob(str(E3 / f"suite-s?-{tag}-{model}.jsonl")), task, length)


def ruler(tag, model, task, length=32768):
    return rate([str(E3 / f"ruler-{length}-{tag}-{model}.jsonl")], f"ruler_niah_{task}", length)


def mean(values):
    return sum(values) / len(values)


def seeds(tags, fn, *args):
    return mean([fn(t, *args) for t in tags])


def bpb(tag, model):
    return json.load(open(E3 / f"bpb-{tag}-{model}.json"))


def bench(tag, model, name):
    return json.load(open(E3 / f"bench-{tag}-{model}.json"))[name]["acc"]


def write(name, spec, header, rows):
    """A complete tabular: LaTeX's \\input cannot sit between table rows and a rule, so the whole environment is generated."""
    OUT.mkdir(exist_ok=True)
    lines = [f"\\begin{{tabular}}{{{spec}}}", "\\toprule", header + r" \\", "\\midrule", *rows, "\\bottomrule", "\\end{tabular}"]
    (OUT / f"{name}.tex").write_text("\n".join(lines) + "\n")


def signature():  # Table 1: before repair at 32K
    rows = []
    for label, model in (("Qwen2.5-1.5B, source", QWEN), ("Jet-Nemotron-2B, hybrid", JET)):
        rows.append(f"{label} & " + " & ".join(r2(suite("base", model, t)) for t in SUITE) + " & " + " & ".join(r2(ruler("base", model, t)) for t in RULER[1:5]) + r" \\")
    rows.append(r"\addlinespace")
    for label, model in (("Llama-3.1-8B-Instruct, source", LLAMA), ("Mamba-in-the-Llama 8B, hybrid", MIL)):
        rows.append(f"{label} & " + " & ".join(r2(suite("base", model, t)) for t in SUITE) + " & " + " & ".join(r2(ruler("base", model, t)) for t in RULER[1:5]) + r" \\")
    write("signature", "lccccccccc", " & needle & 16 random & 16 similar & multi-hop & parcels & MK1 & MK2 & MK3 & MV", rows)


def repair():  # Table 2: after repair at 32K
    tasks, rtasks = SUITE[1:], ("multikey_1", "multikey_2", "multivalue")
    jet = [f"repair-seed{s}" for s in (1, 2, 3)]
    ctrl = [f"repair-seed{s}" for s in (1, 2)]
    gentle = [f"repair-seed{s}-gentle" for s in (1, 2, 3)]
    rows = [
        "2B & hybrid, before & " + " & ".join(r2(suite("base", JET, t)) for t in tasks) + " & " + " & ".join(r2(ruler("base", JET, t)) for t in rtasks) + r" \\",
        "   & hybrid, repaired (heavy) & " + " & ".join(r2(seeds(jet, suite, JET, t)) for t in tasks) + " & " + " & ".join(r2(seeds(jet, ruler, JET, t)) for t in rtasks) + r" \\",
        "   & source, trained (control) & " + " & ".join(r2(seeds(ctrl, suite, QWEN, t)) for t in tasks) + " & " + " & ".join(r2(seeds(ctrl, ruler, QWEN, t)) for t in rtasks) + r" \\",
        r"\addlinespace",
        "8B & hybrid, before & " + " & ".join(r2(suite("base", MIL, t)) for t in tasks) + " & " + " & ".join(r2(ruler("base", MIL, t)) for t in rtasks) + r" \\",
        "   & hybrid, repaired (gentle) & " + " & ".join(r2(seeds(gentle, suite, MIL, t)) for t in tasks) + " & " + " & ".join(r2(seeds(gentle, ruler, MIL, t)) for t in rtasks) + r" \\",
        "   & source, untrained & " + " & ".join(r2(suite("base", LLAMA, t)) for t in tasks) + " & " + " & ".join(r2(ruler("base", LLAMA, t)) for t in rtasks) + r" \\",
    ]
    write("repair", "llccccccc", " & & 16 random & 16 similar & multi-hop & parcels & MK1 & MK2 & MV", rows)


def recipes():  # Table 3: 8B recipes at 32K; (label, synthetic docs, natural windows, lr, tags)
    specs = (
        ("heavy", 600, 0, r"$2\times10^{-4}$", ["repair-seed1-le16k"]),
        ("gentle (3 seeds)", 300, 0, r"$5\times10^{-5}$", [f"repair-seed{s}-gentle" for s in (1, 2, 3)]),
        ("25\\% replay", 600, 200, r"$5\times10^{-5}$", ["repair-seed1-gentle2-replay25"]),
        ("50\\% replay, lr $5\\times10^{-5}$", 150, 150, r"$5\times10^{-5}$", ["repair-seed1-gentle-replay"]),
        ("50\\% replay, lr $2\\times10^{-4}$", 300, 300, r"$2\times10^{-4}$", ["repair-seed1-replay"]),
        ("query and key only", 600, 0, r"$2\times10^{-4}$", ["repair-seed1-qk"]),
    )
    base = [r2(suite("base", MIL, t)) for t in ("many_random", "many_similar", "multihop")] + [r2(ruler("base", MIL, t)) for t in ("multikey_1", "multikey_3")]
    rows = ["unrepaired & -- & -- & " + " & ".join([*base, r3(bpb("base", MIL)["bpb_mean"]), r3(bench("base", MIL, "hellaswag"))]) + r" \\"]
    for label, docs, natural, lr, tags in specs:
        recall = [r2(seeds(tags, suite, MIL, t)) for t in ("many_random", "many_similar", "multihop")]
        mk = [r2(seeds(tags, ruler, MIL, t)) for t in ("multikey_1", "multikey_3")]
        b = [bpb(t, MIL)["bpb_mean"] for t in tags]
        h = [bench(t, MIL, "hellaswag") for t in tags]
        cost = [r3(min(b)) + "--" + r3(max(b)), r3(min(h)) + "--" + r3(max(h))] if len(tags) > 1 else [r3(b[0]), r3(h[0])]
        rows.append(f"{label} & {docs} + {natural} & {lr} & " + " & ".join(recall + mk + cost) + r" \\")
    write("recipes", "llcccccccc", "recipe & documents & lr & 16 random & 16 similar & multi-hop & MK1 & MK3 & bits/byte & HellaSwag", rows)


def collateral():  # Table 4: every model and adapter
    specs = (
        ("Qwen2.5-1.5B, untrained", QWEN, "base"), ("Qwen2.5-1.5B, trained, seed 1", QWEN, "repair-seed1"), ("Qwen2.5-1.5B, trained, seed 2", QWEN, "repair-seed2"),
        ("Jet-Nemotron-2B, untrained", JET, "base"), ("Jet-Nemotron-2B, repaired, seed 1", JET, "repair-seed1"),
        ("Jet-Nemotron-2B, repaired, seed 2", JET, "repair-seed2"), ("Jet-Nemotron-2B, repaired, seed 3", JET, "repair-seed3"),
        None,
        ("Llama-3.1-8B-Instruct, untrained", LLAMA, "base"), ("Mamba-in-the-Llama 8B, untrained", MIL, "base"), ("Mamba-in-the-Llama 8B, heavy", MIL, "repair-seed1-le16k"),
        ("Mamba-in-the-Llama 8B, gentle, seed 1", MIL, "repair-seed1-gentle"), ("Mamba-in-the-Llama 8B, gentle, seed 2", MIL, "repair-seed2-gentle"),
        ("Mamba-in-the-Llama 8B, gentle, seed 3", MIL, "repair-seed3-gentle"), ("Mamba-in-the-Llama 8B, 25\\% replay", MIL, "repair-seed1-gentle2-replay25"),
        ("Mamba-in-the-Llama 8B, 50\\% replay, lr $5\\times10^{-5}$", MIL, "repair-seed1-gentle-replay"),
        ("Mamba-in-the-Llama 8B, 50\\% replay, lr $2\\times10^{-4}$", MIL, "repair-seed1-replay"),
        ("Mamba-in-the-Llama 8B, query and key projections only", MIL, "repair-seed1-qk"),
    )
    rows = []
    for spec in specs:
        if spec is None:
            rows.append(r"\addlinespace")
            continue
        label, model, tag = spec
        vals = bpb(tag, model)["bpb_values"]
        m = mean(vals)
        se = (sum((v - m) ** 2 for v in vals) / (len(vals) - 1)) ** 0.5 / len(vals) ** 0.5
        rows.append(f"{label} & {r3(bench(tag, model, 'arc_easy'))} & {r3(bench(tag, model, 'hellaswag'))} & {r3(m)} $\\pm$ {r3(se)} \\\\")
    write("collateral", "lccc", "model & ARC-Easy & HellaSwag & bits/byte", rows)


def ruler_all():  # Table 5: six RULER variants at 16K and 32K
    specs = (
        ("Qwen2.5-1.5B, untrained", QWEN, ["base"]), ("Qwen2.5-1.5B, trained (2 seeds)", QWEN, ["repair-seed1", "repair-seed2"]),
        ("Jet-Nemotron-2B, untrained", JET, ["base"]), ("Jet-Nemotron-2B, repaired (3 seeds)", JET, ["repair-seed1", "repair-seed2", "repair-seed3"]),
        None,
        ("Llama-3.1-8B-Instruct, untrained", LLAMA, ["base"]), ("Mamba-in-the-Llama 8B, untrained", MIL, ["base"]),
        ("Mamba-in-the-Llama 8B, gentle (3 seeds)", MIL, [f"repair-seed{s}-gentle" for s in (1, 2, 3)]),
    )
    rows = []
    for spec in specs:
        if spec is None:
            rows.append(r"\addlinespace")
            continue
        label, model, tags = spec
        for length in (16384, 32768):
            rows.append(f"{label if length == 16384 else ''} & {length // 1024}K & " + " & ".join(r2(seeds(tags, ruler, model, t, length)) for t in RULER) + r" \\")
    write("ruler", "llcccccc", "model & length & S1 & MK1 & MK2 & MK3 & MV & MQ", rows)


if __name__ == "__main__":
    signature()
    repair()
    recipes()
    collateral()
    ruler_all()
    print("wrote", sorted(p.name for p in OUT.glob("*.tex")))

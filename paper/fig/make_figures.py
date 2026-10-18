"""Figures for the preprint, computed from the committed raw results. Run: .venv/bin/python paper/fig/make_figures.py"""

import glob
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

plt.rcParams.update({
    "font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"], "font.size": 8,
    "axes.labelsize": 8, "axes.titlesize": 8.5, "xtick.labelsize": 7.5, "ytick.labelsize": 7.5,
    "axes.linewidth": 0.6, "xtick.major.width": 0.6, "ytick.major.width": 0.6, "xtick.major.size": 2.5, "ytick.major.size": 2.5,
    "pdf.fonttype": 42, "savefig.dpi": 300,
})

ROOT = Path(__file__).resolve().parents[2]
E1, E3 = ROOT / "exp01_step1/results/raw", ROOT / "exp03_robust/results/raw"
BLUE, ORANGE, AQUA, GRAY = "#2a78d6", "#eb6834", "#1baf7a", "#888780"  # fixed categorical order: source, hybrid, repaired
LENGTHS = (1024, 2048, 4096, 8192, 16384, 32768)


def rate(files, task, length):
    n = k = 0
    for f in files:
        for line in open(f):
            r = json.loads(line)
            if r["task"] == task and r["length_bucket"] == length:
                n += 1
                k += r["contains"]
    return k / n if n else float("nan")


def style(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.set_yticks((0, 0.5, 1.0))
    ax.set_ylim(0, 1.06)


def save(fig, name):
    fig.savefig(ROOT / f"paper/fig/{name}.pdf")
    fig.savefig(ROOT / f"paper/fig/{name}.png")  # preview only; the paper uses the pdf


def fig1():
    pairs = (("2B: Jet-Nemotron-2B vs Qwen2.5-1.5B", "jet-ai_Jet-Nemotron-2B", "Qwen_Qwen2.5-1.5B"),
             ("8B: Mamba-in-the-Llama vs Llama-3.1-8B-Instruct", "JunxiongWang_Llama3.1-Mamba2-8B-dpo", "meta-llama_Llama-3.1-8B-Instruct"))
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.8), sharey=True)
    for ax, (title, hyb, src) in zip(axes, pairs, strict=True):
        for model, color, label in ((src, BLUE, "full attention"), (hyb, ORANGE, "converted hybrid")):
            f = [str(E1 / f"{model}.jsonl")]
            keys = [rate(f, "many_random", ln) for ln in LENGTHS]
            needle = [rate(f, "needle", ln) for ln in LENGTHS]
            ax.plot(LENGTHS, keys, "-o", color=color, lw=1.6, ms=3.2, mec="white", mew=0.6)
            ax.plot(LENGTHS, needle, "--", color=color, lw=1.1)
            dy = -9 if label == "full attention" else 9
            ax.annotate(f"{label}, 16 keys", (LENGTHS[-1], keys[-1]), xytext=(0, dy), textcoords="offset points", color=color, fontsize=7, ha="right", va="center")
        ax.annotate("needle, both models", (LENGTHS[0], 1.0), xytext=(4, 6), textcoords="offset points", color="#444441", fontsize=7, ha="left", va="bottom")
        ax.set_xscale("log", base=2)
        ax.set_xticks(LENGTHS, [f"{ln // 1024}K" for ln in LENGTHS])
        ax.set_xlim(900, 36000)
        ax.set_title(title)
        ax.set_xlabel("context length (tokens)")
        style(ax)
    axes[0].set_ylabel("recall")
    fig.subplots_adjust(left=0.08, right=0.99, wspace=0.18, bottom=0.2, top=0.88)
    save(fig, "fig1_signature")


def fig2():
    tasks = (("many_random", "16 random\nkeys"), ("many_similar", "16 similar\nkeys"), ("multihop", "multi-hop"), ("heldout_many", "held-out\ntemplate"))
    ruler = ("ruler_niah_multikey_1", "RULER MK1")
    specs = (
        ("2B, 32K", "jet-ai_Jet-Nemotron-2B", "Qwen_Qwen2.5-1.5B", "repair-seed{s}", (1, 2, 3)),
        ("8B, 32K (trained at <=16K)", "JunxiongWang_Llama3.1-Mamba2-8B-dpo", "meta-llama_Llama-3.1-8B-Instruct", "repair-seed{s}-gentle", (1, 2, 3)),
    )
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.9), sharey=True)
    for ax, (title, hyb, src, tag, seeds) in zip(axes, specs, strict=True):
        labels, before, after, full = [], [], [], []
        for task, name in tasks:
            labels.append(name)
            before.append(rate(glob.glob(str(E3 / f"suite-s?-base-{hyb}.jsonl")), task, 32768))
            after.append(sum(rate(glob.glob(str(E3 / f"suite-s?-{tag.format(s=s)}-{hyb}.jsonl")), task, 32768) for s in seeds) / len(seeds))
            full.append(rate(glob.glob(str(E3 / f"suite-s?-base-{src}.jsonl")), task, 32768))
        labels.append(ruler[1])
        before.append(rate([str(E3 / f"ruler-32768-base-{hyb}.jsonl")], ruler[0], 32768))
        after.append(sum(rate([str(E3 / f"ruler-32768-{tag.format(s=s)}-{hyb}.jsonl")], ruler[0], 32768) for s in seeds) / len(seeds))
        full.append(rate([str(E3 / f"ruler-32768-base-{src}.jsonl")], ruler[0], 32768))
        x = range(len(labels))
        w = 0.27
        ax.bar([i - w for i in x], before, w, color=ORANGE, label="hybrid, before repair", linewidth=0)
        ax.bar(list(x), after, w, color=AQUA, label="hybrid, repaired (mean of 3 seeds)", linewidth=0)
        ax.bar([i + w for i in x], full, w, color=BLUE, label="full-attention source", linewidth=0)
        ax.set_xticks(list(x), labels, fontsize=7)
        ax.set_title(title)
        style(ax)
    axes[0].set_ylabel("recall at 32K")
    handles, labels_ = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels_, fontsize=7, frameon=False, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.0))
    fig.subplots_adjust(left=0.08, right=0.99, wspace=0.12, bottom=0.2, top=0.8)
    save(fig, "fig2_repair")


def fig3():
    M = "JunxiongWang_Llama3.1-Mamba2-8B-dpo"
    base_bpb = json.load(open(E3 / f"bpb-base-{M}.json"))["bpb_mean"]
    runs = (("heavy (2B dose)", "repair-seed1-le16k"), ("gentle s1", "repair-seed1-gentle"), ("gentle s2", "repair-seed2-gentle"),
            ("gentle s3", "repair-seed3-gentle"), ("gentle + 25% replay", "repair-seed1-gentle2-replay25"),
            ("gentle + 50% replay", "repair-seed1-gentle-replay"), ("50% replay, full lr", "repair-seed1-replay"), ("q/k only", "repair-seed1-qk"))
    fig, ax = plt.subplots(figsize=(4.2, 3.0))
    offsets = {"heavy (2B dose)": (-6, -12), "gentle s1": (6, -12), "gentle s2": None, "gentle s3": None, "gentle + 25% replay": (6, 4),
               "gentle + 50% replay": (6, -10), "50% replay, full lr": (6, 4), "q/k only": (6, 2)}
    for name, stage in runs:
        bpb = json.load(open(E3 / f"bpb-{stage}-{M}.json"))["bpb_mean"]
        hop = rate(glob.glob(str(E3 / f"suite-s?-{stage}-{M}.jsonl")), "multihop", 32768)
        dx = 100 * (bpb / base_bpb - 1)
        color = AQUA if name.startswith("gentle s") else GRAY
        ax.scatter(dx, hop, s=30, color=color, zorder=3, linewidths=0)
        if offsets[name] is not None:
            text = "gentle, 3 seeds" if name == "gentle s1" else name
            ax.annotate(text, (dx, hop), fontsize=6.5, xytext=offsets[name], textcoords="offset points", color="#444441")
    ax.axvline(0, color="#c3c2b7", lw=0.8)
    ax.set_xlabel("long-text bits per byte, change from unrepaired (%)")
    ax.set_ylabel("multi-hop recall at 32K")
    ax.set_xlim(-6, 19)
    style(ax)
    fig.subplots_adjust(left=0.15, right=0.98, bottom=0.17, top=0.97)
    save(fig, "fig3_tradeoff")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("wrote", sorted(p.name for p in (ROOT / "paper/fig").glob("*.pdf")))

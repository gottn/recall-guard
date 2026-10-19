"""README figures, light and dark, built from the committed raw results: the signature (Figure 1 of the paper at feed
size) and the repair as a dumbbell chart. Run from the repo: .venv/bin/python paper/fig/make_readme.py (or `make readme`
in paper/). Writes docs/img/{hero,repair}-{light,dark}.png. `card(out)` draws a 4:5 social card with the same data.
Colours: the paper's categorical order (source blue, hybrid orange, repaired aqua), validated for each surface; text
wears ink, never a series colour."""

import glob
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from make_figures import E3, LENGTHS, rate, signature_rate
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs/img"
MODES = {
    "light": {"surface": "#fcfcfb", "ink": "#1f1f1d", "ink2": "#5c5b56", "grid": "#e6e5e0", "source": "#2a78d6", "hybrid": "#eb6834", "repaired": "#1baf7a"},
    "dark": {"surface": "#1a1a19", "ink": "#ecebe4", "ink2": "#a5a39b", "grid": "#303030", "source": "#2a78d6", "hybrid": "#e06a3a", "repaired": "#1baf7a"},
}
JET, QWEN = "jet-ai_Jet-Nemotron-2B", "Qwen_Qwen2.5-1.5B"
MIL, LLAMA = "JunxiongWang_Llama3.1-Mamba2-8B-dpo", "meta-llama_Llama-3.1-8B-Instruct"
PAIRS = (("2B: Jet-Nemotron-2B vs Qwen2.5-1.5B", JET, QWEN, "repair-seed{s}"),
         ("8B: Mamba-in-the-Llama vs Llama-3.1-8B-Instruct", MIL, LLAMA, "repair-seed{s}-gentle"))
TASKS = (("many_random", "16 random keys"), ("many_similar", "16 similar keys"), ("multihop", "multi-hop"), ("heldout_many", "held-out template"))


def style(ax, c, fs=14):
    ax.set_facecolor(c["surface"])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(c["grid"])
    ax.tick_params(colors=c["ink2"], labelsize=fs, width=1, length=4)
    ax.grid(axis="y", color=c["grid"], lw=1)
    ax.set_axisbelow(True)


def base(c, w, h):
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"], "savefig.dpi": 100,
                         "text.color": c["ink"], "axes.labelcolor": c["ink2"], "axes.edgecolor": c["grid"]})
    return plt.figure(figsize=(w, h), dpi=100, facecolor=c["surface"])


def hero(mode, out=None):
    c = MODES[mode]
    fig = base(c, 16, 9)
    axes = fig.subplots(1, 2, sharey=True)
    for ax, (title, hyb, src, _) in zip(axes, PAIRS, strict=True):
        style(ax, c)
        for model, col in ((src, c["source"]), (hyb, c["hybrid"])):
            keys = [signature_rate(model, "many_random", ln) for ln in LENGTHS]
            needle = [signature_rate(model, "needle", ln) for ln in LENGTHS]
            ax.plot(LENGTHS, needle, "--", color=col, lw=2.5)
            ax.plot(LENGTHS, keys, "-o", color=col, lw=3.5, ms=10, mec=c["surface"], mew=2)
            ax.annotate(f"{keys[-1]:.2f}", (LENGTHS[-1], keys[-1]), xytext=(12, 0), textcoords="offset points", fontsize=15, color=c["ink"], va="center", fontweight="bold")
        ax.set_xscale("log", base=2)
        ax.set_xticks(LENGTHS, [f"{ln // 1024}K" for ln in LENGTHS])
        ax.set_xlim(900, 44000)
        ax.set_ylim(0, 1.08)
        ax.set_yticks((0, 0.5, 1.0))
        ax.set_title(title, fontsize=18, color=c["ink"], pad=12, loc="left")
        ax.set_xlabel("context length (tokens)", fontsize=15)
    axes[0].set_ylabel("recall", fontsize=15)
    handles = [Line2D([0], [0], color=col, lw=3, ls=ls, label=lab) for lab, col, ls in
               (("full-attention source", c["source"], "-"), ("converted hybrid", c["hybrid"], "-"), ("single needle (dashed)", c["ink2"], "--"), ("one of 16 planted facts (solid)", c["ink2"], "-"))]
    fig.legend(handles=handles, loc="upper center", ncol=4, frameon=False, fontsize=14, bbox_to_anchor=(0.5, 0.905), labelcolor=c["ink"])
    fig.suptitle("Converted hybrids pass the needle test and lose multi-key recall", fontsize=24, fontweight="bold", x=0.06, ha="left", y=0.975, color=c["ink"])
    fig.text(0.06, 0.02, "Recall of one of 16 planted facts, 1K to 32K tokens; 25 cases per point to 8K, 100 at 16K and 32K. github.com/gottn/recall-guard", fontsize=12.5, color=c["ink2"])
    fig.subplots_adjust(left=0.06, right=0.97, wspace=0.12, bottom=0.13, top=0.8)
    out = out or OUT / f"hero-{mode}.png"
    fig.savefig(out, facecolor=c["surface"])
    plt.close(fig)
    return out


def repair_values(hyb, src, tag, seeds=(1, 2, 3)):
    rows = []
    for task, label in TASKS:
        before = rate(glob.glob(str(E3 / f"suite-s?-base-{hyb}.jsonl")), task, 32768)
        after = sum(rate(glob.glob(str(E3 / f"suite-s?-{tag.format(s=s)}-{hyb}.jsonl")), task, 32768) for s in seeds) / len(seeds)
        source = rate(glob.glob(str(E3 / f"suite-s?-base-{src}.jsonl")), task, 32768)
        rows.append((label, before, after, source))
    r = "ruler_niah_multikey_1"
    rows.append(("RULER multi-key 1", rate([str(E3 / f"ruler-32768-base-{hyb}.jsonl")], r, 32768),
                 sum(rate([str(E3 / f"ruler-32768-{tag.format(s=s)}-{hyb}.jsonl")], r, 32768) for s in seeds) / len(seeds),
                 rate([str(E3 / f"ruler-32768-base-{src}.jsonl")], r, 32768)))
    return rows


def dumbbell(ax, rows, c, fs=14, ms=150):
    ys = list(range(len(rows)))[::-1]
    for y, (_, before, after, source) in zip(ys, rows, strict=True):
        ax.plot([before, after], [y, y], color=c["grid"], lw=3, solid_capstyle="round", zorder=1)
        ax.scatter([source], [y], marker="|", s=ms * 2.2, color=c["source"], lw=3, zorder=2)
        ax.scatter([before], [y], s=ms, color=c["hybrid"], edgecolor=c["surface"], lw=2, zorder=3)
        ax.scatter([after], [y], s=ms, color=c["repaired"], edgecolor=c["surface"], lw=2, zorder=3)
        ax.annotate(f"{before:.2f}", (before, y), xytext=(0, -16 - ms / 40), textcoords="offset points", ha="center", fontsize=fs - 1, color=c["ink2"])
        ax.annotate(f"{after:.2f}", (after, y), xytext=(0, 11 + ms / 40), textcoords="offset points", ha="center", fontsize=fs - 1, color=c["ink"], fontweight="bold")
    ax.set_yticks(ys, [r[0] for r in rows], fontsize=fs)
    ax.set_xlim(0, 1.06)
    ax.set_ylim(-0.8, len(rows) - 0.2)
    ax.set_xticks((0, 0.5, 1.0))
    ax.grid(axis="x", color=c["grid"], lw=1)
    ax.grid(axis="y", visible=False)


def legend_handles(c, before="hybrid before repair", after="hybrid after repair (mean of 3 seeds)", source="full-attention source, untrained"):
    return [Line2D([0], [0], marker="o", color="none", markerfacecolor=c["hybrid"], ms=11, label=before),
            Line2D([0], [0], marker="o", color="none", markerfacecolor=c["repaired"], ms=11, label=after),
            Line2D([0], [0], marker="|", color=c["source"], lw=0, markeredgewidth=3, ms=16, label=source)]


def repair(mode, out=None):
    c = MODES[mode]
    fig = base(c, 16, 9)
    axes = fig.subplots(1, 2)
    for ax, (title, hyb, src, tag) in zip(axes, PAIRS, strict=True):
        style(ax, c)
        ax.spines["left"].set_visible(False)
        dumbbell(ax, repair_values(hyb, src, tag), c)
        ax.set_title(title, fontsize=18, color=c["ink"], pad=12, loc="left")
        ax.set_xlabel("recall at 32K tokens", fontsize=15)
    fig.legend(handles=legend_handles(c), loc="upper center", ncol=3, frameon=False, fontsize=14, bbox_to_anchor=(0.5, 0.905), labelcolor=c["ink"])
    fig.suptitle("45 minutes of LoRA on under 1% of the weights restores it", fontsize=24, fontweight="bold", x=0.06, ha="left", y=0.975, color=c["ink"])
    fig.text(0.06, 0.02, "Suite cells: 100 cases each; RULER: 50. The 8B adapter was trained only on documents up to 16K tokens. github.com/gottn/recall-guard", fontsize=12.5, color=c["ink2"])
    fig.subplots_adjust(left=0.13, right=0.97, wspace=0.42, bottom=0.13, top=0.8)
    out = out or OUT / f"repair-{mode}.png"
    fig.savefig(out, facecolor=c["surface"])
    plt.close(fig)
    return out


def card(out):
    """4:5 social card: the hero number and a two-row dumbbell."""
    c = MODES["light"]
    fig = base(c, 10.8, 13.5)
    fig.text(0.08, 0.90, "One of 16 facts, recalled at 32K tokens", fontsize=26, color=c["ink2"])
    fig.text(0.08, 0.76, "0.25", fontsize=120, fontweight="bold", color=c["hybrid"], va="center")
    fig.text(0.40, 0.76, "→", fontsize=90, color=c["ink2"], va="center", family="DejaVu Sans")  # Helvetica has no arrow glyph
    fig.text(0.56, 0.76, "1.00", fontsize=120, fontweight="bold", color=c["repaired"], va="center")
    fig.text(0.08, 0.655, "Mamba-in-the-Llama 8B, before and after 45 minutes of LoRA\non under 1% of the weights, trained only on documents up to 16K.", fontsize=22, color=c["ink"], linespacing=1.4)
    ax = fig.add_axes([0.24, 0.19, 0.70, 0.33])
    style(ax, c, fs=18)
    ax.spines["left"].set_visible(False)
    rows = []
    for label, hyb, src, tag in (("2B hybrid", JET, QWEN, "repair-seed{s}"), ("8B hybrid", MIL, LLAMA, "repair-seed{s}-gentle")):
        r = repair_values(hyb, src, tag)[0]  # 16 random keys
        rows.append((label, r[1], r[2], r[3]))
    dumbbell(ax, rows, c, fs=20, ms=320)
    ax.set_xlabel("recall of one of 16 random keys at 32K", fontsize=18)
    ax.legend(handles=legend_handles(c, "before", "after repair", "the transformer it was built from"), loc="upper center", bbox_to_anchor=(0.5, 1.22), ncol=3, frameon=False, fontsize=17, labelcolor=c["ink"])
    fig.text(0.08, 0.06, "Jet-Nemotron-2B vs Qwen2.5-1.5B; Mamba-in-the-Llama 8B vs Llama-3.1-8B-Instruct.\nEvery number and raw completion: github.com/gottn/recall-guard", fontsize=16, color=c["ink2"], linespacing=1.5)
    fig.savefig(out, facecolor=c["surface"])
    plt.close(fig)
    return out


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for mode in ("light", "dark"):
        print("wrote", hero(mode).name, repair(mode).name)

"""Explainer graphics for people outside the field, built from the committed raw results: three pictures of a document
(one fact hidden, sixteen hidden, the same after repair) with the rate found as the headline. Writes
docs/img/explainer-{light,dark}.png (16:9), docs/img/explainer-tall.png (4:5) and, with `--carousel OUT.pdf`, a seven-slide
LinkedIn document. Run from the repo: .venv/bin/python paper/fig/make_explainer.py [--carousel ../recall-guard-launch/carousel.pdf]
Numbers are the 8B pair's (Mamba-in-the-Llama 8B vs Llama-3.1-8B-Instruct); the 2B pair's appear in the footnote."""

import glob
import sys
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from make_figures import E3, rate
from make_readme import JET, LLAMA, MIL, MODES, OUT, QWEN
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch


def pct(x):
    return f"{round(x * 100)}%"


def numbers():
    """(needle, sixteen, source sixteen, repaired sixteen) at 32K for both pairs, as fractions."""
    out = {}
    for name, hyb, src, tag in (("8B", MIL, LLAMA, "repair-seed{s}-gentle"), ("2B", JET, QWEN, "repair-seed{s}")):
        base = glob.glob(str(E3 / f"suite-s?-base-{hyb}.jsonl"))
        rep = [f for s in (1, 2, 3) for f in glob.glob(str(E3 / f"suite-s?-{tag.format(s=s)}-{hyb}.jsonl"))]
        out[name] = (rate(base, "needle", 32768), rate(base, "many_random", 32768),
                     rate(glob.glob(str(E3 / f"suite-s?-base-{src}.jsonl")), "many_random", 32768), rate(rep, "many_random", 32768))
    return out


def canvas(c, w, h):
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"], "savefig.dpi": 100, "text.color": c["ink"]})
    fig = plt.figure(figsize=(w, h), dpi=100, facecolor=c["surface"])
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def document(ax, x, y, w, h, facts, c, lines=22, fact_color=None):
    """A page: grey text lines with `facts` of them highlighted, spread evenly through the page."""
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.08", fc=c["surface"], ec=c["grid"], lw=2.5, zorder=1))
    step = h / (lines + 1)
    marked = {round((i + 0.5) * lines / facts) for i in range(facts)} if facts else set()
    for i in range(lines):
        ly = y + h - (i + 1) * step
        if i in marked:
            ax.plot([x + 0.12 * w, x + 0.62 * w], [ly, ly], color=fact_color or c["hybrid"], lw=4.5, solid_capstyle="round", zorder=2)
        else:
            ax.plot([x + 0.12 * w, x + (0.88 if i % 3 else 0.7) * w], [ly, ly], color=c["grid"], lw=3, solid_capstyle="round", zorder=2)


def tile(ax, cx, top, c, header, facts, value, color, note=None, doc_w=2.3, doc_h=2.6, big=62):
    """One column: header, document picture, the big number, a note under it."""
    ax.text(cx, top, header, ha="center", va="top", fontsize=17, color=c["ink"], linespacing=1.35)
    y0 = top - 0.95 - doc_h
    document(ax, cx - doc_w / 2, y0, doc_w, doc_h, facts, c, fact_color=color if facts else None)
    ax.text(cx, y0 - 0.3, value, ha="center", va="top", fontsize=big, fontweight="bold", color=color)
    ax.text(cx, y0 - 0.3 - big / 55, "found", ha="center", va="top", fontsize=17, color=c["ink2"])
    if note:
        ax.text(cx, y0 - 0.3 - big / 55 - 0.5, note, ha="center", va="top", fontsize=15, color=c["ink2"], linespacing=1.35)


def beside(fig, ax, text_obj, label, c, gap=0.25, fs=17):
    """Place `label` just right of a drawn text object, baseline-aligned to its bottom third."""
    fig.canvas.draw()
    bb = text_obj.get_window_extent().transformed(ax.transData.inverted())
    ax.text(bb.x1 + gap, bb.y0 + 0.12, label, ha="left", va="bottom", fontsize=fs, color=c["ink2"])


def explainer(mode, tall=False, out=None):
    c = MODES[mode]
    n = numbers()
    needle, sixteen, source, repaired = n["8B"]
    n2 = n["2B"]
    headers = ("One fact hidden in a\n32,000-token document.\nAsk for it.", "Sixteen facts hidden.\nAsk for one of them.", "The same model after\n45 minutes of training\non under 1% of its weights.")
    specs = ((1, pct(needle), c["hybrid"], f"its source transformer: {pct(1.0)}"), (16, pct(sixteen), c["hybrid"], f"its source transformer: {pct(source)}"), (16, pct(repaired), c["repaired"], "trained only on documents\nhalf this long"))
    title = "A hybrid LLM finds one fact in a long document.\nHide sixteen, and it finds one in four."
    foot = (f"Mamba-in-the-Llama 8B, a converted hybrid, against Llama-3.1-8B-Instruct, the transformer it was built from. The 2B pair "
            f"(Jet-Nemotron-2B vs Qwen2.5-1.5B): {pct(n2[0])}, {pct(n2[1])} and {pct(n2[3])}.   github.com/gottn/recall-guard")
    if not tall:
        fig, ax = canvas(c, 16, 9)
        ax.text(0.6, 8.6, title, ha="left", va="top", fontsize=27, fontweight="bold", color=c["ink"], linespacing=1.25)
        for cx, h, (facts, value, color, note) in zip((2.9, 8.0, 13.1), headers, specs, strict=True):
            tile(ax, cx, 7.0, c, h, facts, value, color, note)
        ax.annotate("", (10.8, 4.75), (10.2, 4.75), arrowprops={"arrowstyle": "-|>", "color": c["ink2"], "lw": 2.5})
        ax.text(0.6, 0.38, foot, ha="left", va="center", fontsize=11.5, color=c["ink2"], wrap=True)
    else:
        fig, ax = canvas(c, 10.8, 13.5)
        ax.text(0.6, 13.0, title, ha="left", va="top", fontsize=27, fontweight="bold", color=c["ink"], linespacing=1.25, wrap=True)
        for cy, h, (facts, value, color, note) in zip((11.0, 7.4, 3.8), headers, specs, strict=True):
            document(ax, 0.9, cy - 2.9, 2.0, 2.6, facts, c, fact_color=color if facts else None)
            ax.text(3.5, cy - 0.3, h.replace("\n", " "), ha="left", va="top", fontsize=18, color=c["ink"], wrap=True, linespacing=1.3)
            number = ax.text(3.5, cy - 1.45, value, ha="left", va="top", fontsize=56, fontweight="bold", color=color)
            beside(fig, ax, number, "found", c)
            ax.text(3.5, cy - 2.55, note.replace("\n", " "), ha="left", va="top", fontsize=14, color=c["ink2"])
        ax.text(0.6, 0.45, foot, ha="left", va="center", fontsize=11, color=c["ink2"], wrap=True)
    out = out or OUT / ("explainer-tall.png" if tall else f"explainer-{mode}.png")
    fig.savefig(out, facecolor=c["surface"])
    plt.close(fig)
    return out


def wrap(text, width):
    return "\n".join(textwrap.fill(p, width) if p else "" for p in text.split("\n"))


def slide(c, title, body=None, size=(10.8, 13.5), body_top=None):
    """Title, then the body right under it, wrapped to the page with a margin on both sides."""
    fig, ax = canvas(c, *size)
    t = ax.text(0.8, size[1] - 1.0, wrap(title, 26), ha="left", va="top", fontsize=40, fontweight="bold", color=c["ink"], linespacing=1.2)
    fig.canvas.draw()
    y = t.get_window_extent().transformed(ax.transData.inverted()).y0 - 0.8
    if body:
        ax.text(0.8, body_top or y, wrap(body, 38), ha="left", va="top", fontsize=28, color=c["ink"], linespacing=1.4)
    ax.text(0.8, 0.6, "github.com/gottn/recall-guard", ha="left", va="center", fontsize=16, color=c["ink2"])
    return fig, ax


def page(pdf, fig):
    pdf.savefig(fig)
    plt.close(fig)


def carousel(out):
    c = MODES["light"]
    n = numbers()
    needle, sixteen, source, repaired = n["8B"]
    with PdfPages(out) as pdf:
        fig, ax = slide(c, "The standard long-context test\nis too easy.", "It hides one fact in a long document and asks for it.\n\nHybrid language models pass it.\n\nSo I hid sixteen.")
        page(pdf, fig)
        fig, ax = slide(c, "What a hybrid is", "A transformer remembers every word it reads, so its memory grows with the document.\n\nA hybrid replaces most of that with a memory of fixed size. Reading gets cheap.\n\nSeveral recipes now turn an existing transformer into a hybrid.")
        ax.text(0.8, 4.9, "transformer memory: grows with the document", fontsize=18, color=c["ink2"], va="bottom")
        ax.add_patch(FancyBboxPatch((0.8, 3.8), 9.2, 0.9, boxstyle="round,pad=0,rounding_size=0.1", fc=c["source"], ec="none"))
        ax.text(0.8, 3.0, "hybrid memory: fixed size", fontsize=18, color=c["ink2"], va="bottom")
        ax.add_patch(FancyBboxPatch((0.8, 1.9), 2.3, 0.9, boxstyle="round,pad=0,rounding_size=0.1", fc=c["hybrid"], ec="none"))
        page(pdf, fig)
        for header, facts, value, color, note in (("Test 1: one fact hidden in a 32,000-token document. Ask for it.", 1, pct(needle), c["hybrid"], "The hybrid finds it. So does the transformer it was built from."),
                                                   ("Test 2: sixteen facts hidden. Ask for one of them.", 16, pct(sixteen), c["hybrid"], f"The transformer it was built from: {pct(source)}."),
                                                   ("Then 45 minutes of training on one GPU, changing under 1% of the weights.", 16, pct(repaired), c["repaired"], "Trained only on documents half this long.")):
            fig, ax = slide(c, header)
            document(ax, 0.8, 3.4, 3.6, 4.8, facts, c, fact_color=color)
            number = ax.text(5.2, 7.3, value, ha="left", va="top", fontsize=96, fontweight="bold", color=color)
            beside(fig, ax, number, "found", c, fs=26)
            ax.text(0.8, 2.6, wrap(note, 44), ha="left", va="top", fontsize=24, color=c["ink"], linespacing=1.4)
            page(pdf, fig)
        fig, ax = slide(c, "The ability was there.\nIt had never been trained.", "The conversion left retrieval untrained, and the standard test never asked.\n\nLimit: facts in formats the training data never showed are only partly fixed, and at 2B a gap to the trained control remains on one benchmark.")
        page(pdf, fig)
        fig, ax = slide(c, "Code, training recipe\nand every model answer", "github.com/gottn/recall-guard\n\nPaper: Multi-Key Recall in Converted Hybrid Language Models: A Training Deficit, Not a Capacity Limit. Link in the comments.\n\nModels: Jet-Nemotron-2B vs Qwen2.5-1.5B; Mamba-in-the-Llama 8B vs Llama-3.1-8B-Instruct.")
        page(pdf, fig)
    return out


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    print("wrote", explainer("light").name, explainer("dark").name, explainer("light", tall=True).name)
    if "--carousel" in sys.argv:
        print("wrote", carousel(Path(sys.argv[sys.argv.index("--carousel") + 1])))

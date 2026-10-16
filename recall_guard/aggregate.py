"""Results -> table rows -> markdown. Pure; the CLI writes the strings."""

from dataclasses import dataclass

from recall_guard.types import Result


@dataclass(frozen=True)
class Row:
    model: str
    task: str
    length_bucket: int
    n: int
    contains_rate: float
    exact_rate: float
    stale_rate: float
    mean_wall_s: float


@dataclass(frozen=True)
class Gap:
    hybrid: str
    full: str
    task: str
    length_bucket: int
    hybrid_rate: float
    full_rate: float


def rows(results: tuple[Result, ...]) -> tuple[Row, ...]:
    keys = sorted({(r.model, r.task, r.length_bucket) for r in results})
    out = []
    for model, task, length in keys:
        rs = [r for r in results if (r.model, r.task, r.length_bucket) == (model, task, length)]
        n = len(rs)
        out.append(
            Row(
                model, task, length, n,
                sum(r.contains for r in rs) / n, sum(r.exact for r in rs) / n, sum(r.stale for r in rs) / n,
                sum(r.wall_s for r in rs) / n,
            )
        )
    return tuple(out)


def gaps(table: tuple[Row, ...], pairs: tuple[tuple[str, str], ...]) -> tuple[Gap, ...]:
    """Hybrid-minus-full recall per (task, length) for each (hybrid, full) model pair, on the contains rate."""
    by_key = {(r.model, r.task, r.length_bucket): r for r in table}
    return tuple(
        Gap(h, f, task, length, by_key[(h, task, length)].contains_rate, by_key[(f, task, length)].contains_rate)
        for h, f in pairs
        for task, length in sorted({(r.task, r.length_bucket) for r in table})
        if (h, task, length) in by_key and (f, task, length) in by_key
    )


def markdown(table: tuple[Row, ...]) -> str:
    head = "| model | task | ref tokens | n | contains | exact | stale | wall s |\n|---|---|---:|---:|---:|---:|---:|---:|"
    body = (
        f"| {r.model} | {r.task} | {r.length_bucket} | {r.n} | {r.contains_rate:.2f} | {r.exact_rate:.2f} "
        f"| {r.stale_rate:.2f} | {r.mean_wall_s:.1f} |"
        for r in table
    )
    return "\n".join((head, *body))


def pivot_markdown(table: tuple[Row, ...]) -> str:
    """One line per (model, task), one column per length: the view that shows where recall breaks."""
    lengths = sorted({r.length_bucket for r in table})
    by_key = {(r.model, r.task, r.length_bucket): r for r in table}
    head = "| model | task | " + " | ".join(str(ln) for ln in lengths) + " |\n|---|---|" + "---:|" * len(lengths)
    body = (
        f"| {model} | {task} | "
        + " | ".join(f"{by_key[(model, task, ln)].contains_rate:.2f}" if (model, task, ln) in by_key else "" for ln in lengths)
        + " |"
        for model, task in sorted({(r.model, r.task) for r in table})
    )
    return "\n".join((head, *body))


def gap_markdown(table: tuple[Gap, ...]) -> str:
    head = "| hybrid | full | task | ref tokens | hybrid | full | gap |\n|---|---|---|---:|---:|---:|---:|"
    body = (
        f"| {g.hybrid} | {g.full} | {g.task} | {g.length_bucket} | {g.hybrid_rate:.2f} | {g.full_rate:.2f} "
        f"| {g.hybrid_rate - g.full_rate:+.2f} |"
        for g in table
    )
    return "\n".join((head, *body))


@dataclass(frozen=True)
class Separation:
    """First length where a stressor separates a pair while the needle does not (the step1 verdict rule)."""

    hybrid: str
    full: str
    task: str
    length_bucket: int
    gap: float
    needle_gap: float


def separations(table: tuple[Row, ...], pairs: tuple[tuple[str, str], ...], threshold: float = 0.2) -> tuple[Separation, ...]:
    """Per (pair, task): the shortest length where full - hybrid >= threshold and |needle gap| < threshold."""
    by_key = {(r.model, r.task, r.length_bucket): r.contains_rate for r in table}
    out = []
    for h, f in pairs:
        for task in sorted({r.task for r in table if r.task != "needle"}):
            for length in sorted({r.length_bucket for r in table}):
                keys = ((h, task, length), (f, task, length), (h, "needle", length), (f, "needle", length))
                if not all(k in by_key for k in keys):
                    continue
                gap = by_key[keys[1]] - by_key[keys[0]]
                needle_gap = by_key[keys[3]] - by_key[keys[2]]
                if gap >= threshold and abs(needle_gap) < threshold:
                    out.append(Separation(h, f, task, length, gap, needle_gap))
                    break
    return tuple(out)


def separation_markdown(table: tuple[Separation, ...]) -> str:
    head = "| hybrid | full | task | first length with gap | full - hybrid | needle gap |\n|---|---|---|---:|---:|---:|"
    body = (f"| {s.hybrid} | {s.full} | {s.task} | {s.length_bucket} | {s.gap:+.2f} | {s.needle_gap:+.2f} |" for s in table)
    return "\n".join((head, *body)) if table else head + "\n| (none) | | | | | |"

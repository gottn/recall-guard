from recall_guard.aggregate import gap_markdown, gaps, markdown, pivot_markdown, rows
from recall_guard.types import Result


def res(model, task, length, contains, stale=False, cid="c"):
    return Result(cid, task, length, model, "", contains, contains, stale, 1.0)


def test_rows_and_gaps():
    results = (
        res("h", "needle", 1024, True), res("h", "needle", 1024, False, stale=True),
        res("f", "needle", 1024, True), res("f", "needle", 1024, True),
    )
    table = rows(results)
    assert [(r.model, r.contains_rate, r.stale_rate) for r in table] == [("f", 1.0, 0.0), ("h", 0.5, 0.5)]
    g = gaps(table, (("h", "f"),))
    assert len(g) == 1 and g[0].hybrid_rate - g[0].full_rate == -0.5
    assert "| h | needle | 1024 |" in markdown(table)
    assert "| h | needle | 0.50 |" in pivot_markdown(table)
    assert "-0.50" in gap_markdown(g)


def test_separation_finds_first_length_where_stressor_splits_but_needle_does_not():
    from recall_guard.aggregate import separations

    results = tuple(
        res(m, t, ln, ok)
        for ln in (1024, 4096)
        for m, t, ok in (
            ("h", "needle", True), ("f", "needle", True),
            ("h", "many", ln == 1024), ("f", "many", True),  # hybrid fails many at 4096 only
        )
    )
    s = separations(rows(results), (("h", "f"),), threshold=0.2)
    assert [(x.task, x.length_bucket, x.gap, x.needle_gap) for x in s] == [("many", 4096, 1.0, 0.0)]


def test_check_flags_a_paired_drop_and_ignores_unshared_cases():
    from recall_guard.aggregate import binomial_tail_half, delta_markdown, deltas, regressions

    assert (binomial_tail_half(5, 5), binomial_tail_half(0, 5), binomial_tail_half(0, 0)) == (1 / 32, 1.0, 1.0)
    base = (*(res("b", "many", 32768, True, cid=f"many-{i}") for i in range(10)), res("b", "needle", 1024, True, cid="unshared"))
    cand = tuple(res("c", "many", 32768, i >= 5, cid=f"many-{i}") for i in range(10))  # candidate loses 5 of 10, gains none
    table = deltas(base, cand)
    assert [(d.task, d.n, d.lost, d.gained, d.p_regress) for d in table] == [("all", 10, 5, 0, 1 / 32), ("many", 10, 5, 0, 1 / 32)]
    assert [d.task for d in regressions(table)] == ["all", "many"]
    assert regressions(deltas(cand, base)) == ()  # the reverse direction is a gain, never a regression
    assert "| many | 32768 | 10 | 1.00 | 0.50 | 5 | 0 | 0.0312 | FAIL |" in delta_markdown(table, regressions(table))

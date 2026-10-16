from recall_guard.aggregate import gap_markdown, gaps, markdown, pivot_markdown, rows
from recall_guard.types import Result


def res(model, task, length, contains, stale=False):
    return Result("c", task, length, model, "", contains, contains, stale, 1.0)


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

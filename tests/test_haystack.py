from recall_guard import haystack
from recall_guard.score import score


def words(text: str) -> int:
    return len(text.split())


def test_p5_is_rulers_noise_line_and_r50_has_no_period():
    assert " ".join(haystack.NOISE[:5]) == "The grass is green. The sky is blue. The sun is yellow. Here we go. There and back again."
    assert len(set(haystack.NOISE)) == 50 and not any(c.isdigit() for s in haystack.NOISE for c in s)
    r = haystack.sentences("r50", 200, 3)
    cycles = [r[i : i + 50] for i in range(0, 200, 50)]
    assert all(sorted(c) == sorted(haystack.NOISE) for c in cycles) and len(set(cycles)) == 4
    assert haystack.sentences("p50", 120, 3)[50:100] == haystack.NOISE and haystack.sentences("r50", 120, 3) == r[:120]
    assert set(haystack.sentences("p1", 7, 3)) == {"The grass is green."}


def test_sweep_hits_targets_shares_needles_and_scores_an_echo_as_stale():
    cells = (("p1", 1), ("p5", 1), ("filler", 1), ("filler", 4))
    a = haystack.build_sweep(cells, (600,), 2, 0, words)
    assert a == haystack.build_sweep(cells, (600,), 2, 0, words) and len({c.id for c in a}) == 8
    for c in a:
        values = c.answer.split("|")
        assert abs(c.ref_tokens - 600) <= 60 and len(values) == int(c.task[-1]), c.id
        assert all(c.prompt.count(v) == 1 for v in values) and c.prompt.count("One of the special magic") == len(values)
        assert c.prompt.endswith("mentioned in the provided text " + ("are" if len(values) > 1 else "is"))
    p1, p5 = a[0], a[2]
    assert p1.answer == p5.answer and p1.prompt != p5.prompt  # same needle, another haystack
    assert score(p5.answer, p5.distractors, "The grass is green. The sky is blue.", "contains") == (False, False, True)
    assert score(p5.answer, p5.distractors, f"The special magic number is {p5.answer}.", "contains") == (True, False, False)

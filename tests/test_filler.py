from recall_guard.filler import filler_sentences


def test_filler_is_deterministic_and_digit_free():
    a, b = filler_sentences(50, 7), filler_sentences(50, 7)
    assert a == b and len(a) == 50
    assert not any(ch.isdigit() for s in a for ch in s)
    assert filler_sentences(50, 8) != a

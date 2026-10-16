from recall_guard.score import score


def test_score_rules():
    assert score("482913", ("111111",), " 482913\n") == (True, True, False)
    assert score("482913", ("111111",), "The code is 482913.") == (True, True, False)
    assert score("482913", ("111111",), "111111") == (False, False, True)
    assert score("482913", ("111111",), "\n\n111111 then 482913") == (True, False, False)
    assert score("482913", (), "") == (False, False, False)
    assert score("482913", (), "48291") == (False, False, False)

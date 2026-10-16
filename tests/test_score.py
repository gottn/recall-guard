from recall_guard.score import score, strip_think


def test_score_rules():
    assert score("482913", ("111111",), " 482913\n") == (True, True, False)
    assert score("482913", ("111111",), "The code is 482913.") == (True, True, False)
    assert score("482913", ("111111",), "111111") == (False, False, True)
    assert score("482913", ("111111",), "\n\n111111 then 482913") == (True, False, False)
    assert score("482913", (), "") == (False, False, False)
    assert score("482913", (), "48291") == (False, False, False)


def test_think_blocks_are_stripped_before_scoring():
    assert score("980205", (), "\n\n<think>\n\n</think>\n\n980205") == (True, True, False)
    assert score("980205", (), "<think>\nreasoning 111111 cut off") == (False, False, False)
    assert strip_think("a<think>x</think>b<think>y") == "ab"


def test_contains_rule_requires_every_part_anywhere():
    assert score("1234567|7654321", (), "The numbers are 1234567 and 7654321.", "contains") == (True, False, False)
    assert score("1234567|7654321", ("9999999",), "Only 1234567 and 9999999.", "contains") == (False, False, True)
    assert score("abc-uuid", (), "\n\nThe uuid is abc-uuid.", "contains") == (True, False, False)

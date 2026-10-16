from recall_guard.ruler import to_case
from recall_guard.score import score


def test_ruler_record_becomes_contains_case():
    rec = {"index": 7, "input": "A magic number is hidden.\\nText text\\nWhat is the number?", "outputs": ["1234567", "7654321"],
           "length": 32700, "answer_prefix": " The numbers are"}
    c = to_case("niah_multivalue", 32768, rec)
    assert c.task == "ruler_niah_multivalue" and c.rule == "contains" and c.ref_tokens == 32700
    assert "\\n" not in c.prompt and c.prompt.endswith("What is the number? The numbers are") and "\n" in c.prompt
    assert score(c.answer, c.distractors, "The numbers are 1234567 and 7654321.", c.rule) == (True, False, False)
    assert score(c.answer, c.distractors, "1234567", c.rule) == (False, False, False)

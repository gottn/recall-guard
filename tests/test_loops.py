from recall_guard import loops


def test_subset_takes_the_first_problems_of_each_level():
    rows = tuple({"unique_id": f"{lv}-{i}", "level": lv} for i in range(3) for lv in (5, 1, 3))
    assert [r["unique_id"] for r in loops.subset(rows, 2)] == ["1-0", "1-1", "3-0", "3-1", "5-0", "5-1"]


def test_stop_position_boxed_answer_and_normal_form():
    assert loops.finished_at([5, 7, 9, 2], (9, 1)) == 3 and loops.finished_at([5, 7], (9,)) == 0
    assert loops.last_boxed("a \\boxed{1} b \\boxed{\\frac{1}{2}} c") == "\\frac{1}{2}"
    assert loops.last_boxed("\\boxed{\\frac{1}{2") == "" and loops.last_boxed("none") == ""
    assert loops.normalize("\\left( 3, \\dfrac{1}{2} \\right)") == loops.normalize("(3,\\frac{1}{2})")
    assert loops.normalize("90^\\circ") == "90" and loops.normalize("\\text{(C)}") == "(C)"


def test_record_grades_only_a_finished_answer_after_its_think_block():
    row = {"unique_id": "test/x.json", "level": 2, "answer": "\\frac{1}{2}"}
    done = loops.record(row, "<think>maybe \\boxed{3}</think>\nSo \\boxed{\\dfrac{1}{2}}.", 40, 64, "m", 1.0)
    assert (done["finished"], done["new_tokens"], done["boxed"], done["correct"]) == (True, 40, "\\dfrac{1}{2}", True)
    cut = loops.record(row, "<think>\\boxed{\\frac{1}{2}} and again and again", 0, 64, "m", 1.0)
    assert (cut["finished"], cut["new_tokens"], cut["boxed"], cut["correct"]) == (False, 64, "", False)

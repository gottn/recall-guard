from recall_guard.suite import SuiteSpec, build_suite, render
from recall_guard.tasks import needle


def words(text: str) -> int:
    return len(text.split())


def test_render_plants_every_fact_and_question():
    inst = needle(1)
    prompt = render(inst, ("Filler one.",) * 20)
    assert inst.facts[0].sentence in prompt and inst.question in prompt and prompt.endswith("Answer:")


def test_suite_hits_targets_and_is_deterministic():
    spec = SuiteSpec(("needle", "updated"), (300, 900), 2)
    a, b = build_suite(spec, 0, words), build_suite(spec, 0, words)
    assert a == b and len(a) == 8
    for case in a:
        assert abs(case.ref_tokens - case.length_bucket) / case.length_bucket < 0.05, case.id
        assert case.answer in case.prompt and case.prompt.count(case.answer) == 1
    assert len({c.id for c in a}) == 8 and len({c.prompt for c in a}) == 8

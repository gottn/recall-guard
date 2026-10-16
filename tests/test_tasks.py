import random

import pytest

from recall_guard.tasks import TASKS, similar_keys, updated


@pytest.mark.parametrize("name", sorted(TASKS))
def test_task_is_deterministic_and_answer_is_planted(name):
    a, b = TASKS[name](3), TASKS[name](3)
    assert a == b
    assert a.task == name
    assert any(a.answer in f.sentence for f in a.facts)
    assert a.answer not in a.distractors
    assert all(0.0 <= f.depth < 1.0 for f in a.facts)
    assert TASKS[name](4) != a


def test_similar_keys_share_letters_and_differ_by_number():
    keys = similar_keys(16, random.Random(1))
    assert len(set(keys)) == 16 and len({k[:2] for k in keys}) == 1


def test_updated_latest_value_comes_after_old_one():
    inst = updated(5)
    old = inst.distractors[0]
    d_old = next(f.depth for f in inst.facts if old in f.sentence)
    d_new = next(f.depth for f in inst.facts if inst.answer in f.sentence)
    assert d_old < d_new
    assert len(inst.facts) == 16


def test_multihop_has_two_facts_per_chain():
    inst = TASKS["multihop"](9)
    assert len(inst.facts) == 16
    assert "assigned to" in inst.question

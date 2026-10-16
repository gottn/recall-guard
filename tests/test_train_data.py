from recall_guard.tasks import heldout_many
from recall_guard.train_data import KINDS, make_document, segments, training_segments


def words(text: str) -> int:
    return len(text.split())


def test_documents_cycle_kinds_and_answers_are_planted():
    for seed in range(6):
        doc = make_document(seed)
        assert doc.kind == KINDS[seed % 3]
        assert 1 <= len(doc.qa) <= 8
        for _q, a in doc.qa:
            assert any(a in f.sentence for f in doc.facts)
        if doc.kind == "updated":
            assert all(q.startswith("What is the current") for q, _ in doc.qa)


def test_segments_train_only_on_answers():
    segs = segments(make_document(1), ("Filler one.",) * 10)
    trained = [s.text for s in segs if s.train]
    assert len(trained) == len(make_document(1).qa) and all(t.endswith("\n") and t.strip().isdigit() for t in trained)
    assert not segs[0].train and segs[0].text.startswith("Read the document")


def test_training_segments_hit_target_and_are_deterministic():
    a = training_segments(3, 600, words, 12.0)
    assert a == training_segments(3, 600, words, 12.0)
    total = words("".join(s.text for s in a))
    assert abs(total - 600) / 600 < 0.1


def test_heldout_task_uses_parcel_template():
    inst = heldout_many(2)
    assert inst.task == "heldout_many" and "parcel" in inst.question and len(inst.facts) == 16
    assert any(inst.answer in f.sentence for f in inst.facts)

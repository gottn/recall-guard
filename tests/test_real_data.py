from recall_guard.real_data import HEAD, TAIL, disjoint, eval_strings, hotpot_pool, real_segments, squad_pool


def words(text: str) -> int:
    return len(text.split())


def squad_data(articles: int = 3, paragraphs: int = 4) -> dict:
    return {"data": [
        {"title": f"A{a}", "paragraphs": [
            {"context": " ".join(f"a{a}p{p}w{w}" for w in range(30)),
             "qas": [{"question": f"Q a{a} p{p} {k}?", "is_impossible": False, "answers": [{"text": f"a{a}p{p}w{k}"}]} for k in range(3)]
                    + [{"question": f"impossible a{a} p{p}?", "is_impossible": True, "answers": []}]}
            for p in range(paragraphs)]}
        for a in range(articles)]}


def hotpot_data(n: int = 6) -> list:
    return [{"question": f"Which of T{i} and T{i + 1}?", "answer": f"T{i}",
             "supporting_facts": [[f"T{i}", 0], [f"T{i + 1}", 0]],
             "context": [[f"T{j}", [f"T{j} sentence one. ", "T{j} sentence two."]] for j in range(i, i + 4)]}
            for i in range(n)]


def test_pools_follow_ruler_rendering():
    sq = squad_pool(squad_data())
    assert len(sq.groups) == 3 and all(len(g.qas) == 12 and len(g.paragraphs) == 4 for g in sq.groups)
    assert len(sq.paragraphs) == 12 and all(q.gold[0] in sq.groups[0].paragraphs for q in sq.groups[0].qas)
    hp = hotpot_pool(hotpot_data())
    assert len(hp.groups) == 6 and len(hp.paragraphs) == 9
    assert hp.groups[0].qas[0].gold == ("T0\nT0 sentence one. T{j} sentence two.", "T1\nT1 sentence one. T{j} sentence two.")


def test_segments_are_ruler_prompts_sized_to_budget_and_deterministic():
    sq = squad_pool(squad_data(articles=20))
    segs = real_segments(sq, 3, 400, words)
    assert segs == real_segments(sq, 3, 400, words)
    prompt = segs[0].text
    assert prompt.startswith(HEAD + "Document 1:\n") and prompt.endswith(TAIL) and not segs[0].train
    n_docs = prompt.count("\n\nDocument ")
    assert all(f"Document {i}:\n" in prompt for i in range(1, n_docs + 1))
    answers = [s.text for s in segs if s.train]
    questions = [s.text for s in segs if not s.train][1:]
    assert len(answers) == 8 and all(a.startswith(" ") and a.endswith("\n") for a in answers)
    assert all(q.startswith("\nQuestion: ") and q.endswith(" Answer:") for q in questions)
    assert all(a.strip() in prompt for a in answers)  # every gold paragraph is in the document
    total = words("".join(s.text for s in segs))
    assert 0.8 * 400 <= total <= 400 + 40


def test_hotpot_documents_ask_several_questions_and_fit_short_budgets():
    hp = hotpot_pool(hotpot_data(40))
    segs = real_segments(hp, 1, 120, words)
    assert 1 <= sum(s.train for s in segs) < 8 and words("".join(s.text for s in segs)) <= 120 + 20
    for q, a in zip([s.text for s in segs if not s.train][1:], [s.text for s in segs if s.train], strict=True):
        assert a.strip() in segs[0].text and q.split("Which of ")[1].split(" and")[0] == a.strip()


def test_eval_strings_remove_paragraphs_and_questions_from_training():
    sq = squad_pool(squad_data(articles=6))
    segs = real_segments(sq, 5, 300, words)
    banned = eval_strings([segs[0].text + segs[1].text])  # a RULER-shaped evaluation prompt
    n_docs = segs[0].text.count("\n\nDocument ")
    assert len(banned) == n_docs + 1 and segs[1].text[len("\nQuestion: "):-len(" Answer:")] in banned
    assert banned - {segs[1].text[len("\nQuestion: "):-len(" Answer:")]} <= set(sq.paragraphs)
    clean = disjoint(sq, banned)
    assert banned.isdisjoint(clean.paragraphs) and all(banned.isdisjoint(q.gold) and q.question not in banned for g in clean.groups for q in g.qas)
    assert all(banned.isdisjoint(g.paragraphs) for g in clean.groups)
    assert len(clean.paragraphs) == len(sq.paragraphs) - n_docs
    assert disjoint(sq, frozenset()) == sq

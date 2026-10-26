"""Real-document repair training: long documents of real Wikipedia paragraphs with real questions, framed exactly as
RULER's QA tasks (its `qa` template, `Document i:` blocks, ` Answer:`), loss only on the answers. Sources are the SQuAD v2
and HotpotQA train splits (exp04 evaluates on their dev splits); `disjoint` removes every evaluation paragraph and
question by exact string before anything is sampled. Pure: the trainer parses the JSON files and passes the objects."""

import random
import re
from collections.abc import Callable, Iterable
from dataclasses import dataclass

from recall_guard.train_data import QUESTIONS_PER_DOC, Segment

INSTRUCTION = "Answer the question based on the given documents. Only give me the answer and do not output any other words."
HEAD = f"{INSTRUCTION}\n\nThe following are given documents.\n\n"
TAIL = f"\n\n{INSTRUCTION}\n"
DOC_BLOCK = re.compile(r"Document \d+:\n(.*?)(?=\n\nDocument \d+:\n|\n\nAnswer the question)", re.S)


@dataclass(frozen=True)
class QA:
    question: str
    answer: str
    gold: tuple[str, ...]  # the paragraphs the answer needs


@dataclass(frozen=True)
class Group:
    """What RULER places next to a question: a SQuAD article's paragraphs, or a HotpotQA question's ten."""

    paragraphs: tuple[str, ...]
    qas: tuple[QA, ...]


@dataclass(frozen=True)
class Pool:
    name: str
    groups: tuple[Group, ...]
    paragraphs: tuple[str, ...]  # every distinct paragraph, sorted: the distractor pool, as RULER's DOCS


def pool(name: str, groups: tuple[Group, ...]) -> Pool:
    return Pool(name, groups, tuple(sorted({p for g in groups for p in g.paragraphs})))


def squad_pool(data: dict) -> Pool:
    """SQuAD JSON: one group per article, its paragraphs and their answerable questions (v2's impossible ones skipped)."""
    return pool("squad", tuple(
        Group(tuple(dict.fromkeys(p["context"] for p in a["paragraphs"])),
              tuple(QA(q["question"], q["answers"][0]["text"], (p["context"],))
                    for p in a["paragraphs"] for q in p["qas"] if not q.get("is_impossible")))
        for a in data["data"]))


def hotpot_pool(data: list) -> Pool:
    """HotpotQA JSON: one group per question, its ten paragraphs rendered as RULER does (title, newline, sentences)."""
    groups = []
    for d in data:
        docs = {t: f"{t}\n{''.join(s)}" for t, s in d["context"]}
        gold = tuple(dict.fromkeys(docs[t] for t, _ in d["supporting_facts"] if t in docs))
        groups.append(Group(tuple(docs.values()), (QA(d["question"], d["answer"], gold),)))
    return pool("hotpot", tuple(groups))


def eval_strings(prompts: Iterable[str]) -> frozenset[str]:
    """Every paragraph and the question of RULER QA prompts: what the training pools must never contain."""
    out: set[str] = set()
    for p in prompts:
        out.update(DOC_BLOCK.findall(p))
        out.add(p.rsplit("Question: ", 1)[1].removesuffix(" Answer:"))
    return frozenset(out)


def disjoint(src: Pool, banned: frozenset[str]) -> Pool:
    """The pool without the banned paragraphs and without any question that is banned or whose gold paragraph is."""
    groups = (Group(tuple(p for p in g.paragraphs if p not in banned),
                    tuple(q for q in g.qas if q.question not in banned and banned.isdisjoint(q.gold))) for g in src.groups)
    return pool(src.name, tuple(g for g in groups if g.qas))


def block(i: int, paragraph: str) -> str:
    return f"Document {i}:\n{paragraph}"


def real_segments(src: Pool, seed: int, target_tokens: int, count_tokens: Callable[[str], int]) -> tuple[Segment, ...]:
    """One sized training example: up to QUESTIONS_PER_DOC questions, their gold paragraphs among their natural
    neighbours (the article; HotpotQA's ten) as far as they fit, then random paragraphs up to the budget, all shuffled
    and numbered as RULER does. Costs are summed per paragraph, so the total lands within a few tokens of the target."""
    rng = random.Random(seed)
    budget = target_tokens - count_tokens(HEAD + TAIL)

    def cost(p: str) -> int:
        return count_tokens(block(1, p) + "\n\n")

    qas: list[QA] = []
    docs: list[str] = []
    used = 0
    for gi in rng.sample(range(len(src.groups)), min(len(src.groups), QUESTIONS_PER_DOC)):
        g = src.groups[gi]
        picked = rng.sample(g.qas, min(len(g.qas), QUESTIONS_PER_DOC - len(qas)))
        gold = tuple(dict.fromkeys(p for q in picked for p in q.gold if p not in docs))
        need = sum(cost(p) for p in gold) + sum(count_tokens(f"\nQuestion: {q.question} Answer: {q.answer}\n") for q in picked)
        if qas and used + need > budget:
            break  # the next group's gold does not fit: stop asking
        qas += picked
        docs += gold
        used += need
        for p in rng.sample(g.paragraphs, len(g.paragraphs)):  # the natural neighbours, as many as fit
            if p not in docs:
                c = cost(p)
                if used + c <= budget:
                    docs.append(p)
                    used += c
        if len(qas) == QUESTIONS_PER_DOC:
            break
    for _ in range(len(src.paragraphs)):  # random filler until the budget is spent
        p = src.paragraphs[rng.randrange(len(src.paragraphs))]
        if p in docs:
            continue
        c = cost(p)
        if used + c > budget:
            break
        docs.append(p)
        used += c
    order = rng.sample(docs, len(docs))
    out = [Segment(HEAD + "\n\n".join(block(i + 1, p) for i, p in enumerate(order)) + TAIL, False)]
    for q in qas:
        out += [Segment(f"\nQuestion: {q.question} Answer:", False), Segment(f" {q.answer}\n", True)]
    return tuple(out)

"""Synthetic repair-training documents: many planted keys, several questions at the end, loss only on the answers.
Pure: returns text segments with a train flag; the trainer tokenizes them. Uses the locker template family only, so
`heldout_many` (parcels) stays unseen."""

import random
from collections.abc import Callable
from dataclasses import dataclass

from recall_guard.filler import filler_sentences
from recall_guard.suite import INSTRUCTION, SENTENCES_PER_LINE
from recall_guard.tasks import (
    FIRST_NAMES,
    LAST_NAMES,
    current_question,
    depths,
    distinct_codes,
    fact_sentence,
    question,
    random_keys,
    similar_keys,
    update_sentence,
)
from recall_guard.types import Fact

KEY_RANGE = (16, 48)
UPDATE_KEY_RANGE = (8, 24)
QUESTIONS_PER_DOC = 8
KINDS = ("random", "similar", "updated", "multihop")  # v2 mix (2026-10-16 evening); v1 lacked multihop
CHAIN_RANGE = (8, 24)


@dataclass(frozen=True)
class Segment:
    text: str
    train: bool


@dataclass(frozen=True)
class Document:
    kind: str
    facts: tuple[Fact, ...]
    qa: tuple[tuple[str, str], ...]  # (question, answer code)


def make_document(seed: int) -> Document:
    """Kind cycles with the seed so a run mixes the three stressors evenly."""
    rng = random.Random(seed)
    kind = KINDS[seed % len(KINDS)]
    if kind == "updated":
        n = rng.randint(*UPDATE_KEY_RANGE)
        keys = random_keys(n, rng)
        old, new = distinct_codes(n, rng), distinct_codes(n, random.Random(seed + 7))
        facts: list[Fact] = []
        for k, a, b in zip(keys, old, new, strict=True):
            d1, d2 = sorted(depths(2, rng))
            facts += [Fact(fact_sentence(k, a), d1), Fact(update_sentence(k, b), d2)]
        asked = rng.sample(range(n), min(QUESTIONS_PER_DOC, n))
        return Document(kind, tuple(facts), tuple((current_question(keys[i]), new[i]) for i in asked))
    if kind == "multihop":
        n = rng.randint(*CHAIN_RANGE)
        keys, codes = random_keys(n, rng), distinct_codes(n, rng)
        names = tuple(f"{f} {s}" for f, s in zip(rng.sample(FIRST_NAMES, n), rng.sample(LAST_NAMES, n), strict=True))
        ds = depths(2 * n, rng)
        facts = tuple(
            f
            for i, (k, nm, c) in enumerate(zip(keys, names, codes, strict=True))
            for f in (Fact(f"Locker {k} is assigned to {nm}.", ds[2 * i]), Fact(f"The access code for {nm} is {c}.", ds[2 * i + 1]))
        )
        asked = rng.sample(range(n), min(QUESTIONS_PER_DOC, n))
        q = "What is the access code for the person assigned to locker {}?"
        return Document(kind, facts, tuple((q.format(keys[i]), codes[i]) for i in asked))
    n = rng.randint(*KEY_RANGE)
    keys = random_keys(n, rng) if kind == "random" else similar_keys(n, rng)
    values = distinct_codes(n, rng)
    facts = tuple(Fact(fact_sentence(k, v), d) for k, v, d in zip(keys, values, depths(n, rng), strict=True))
    asked = rng.sample(range(n), min(QUESTIONS_PER_DOC, n))
    return Document(kind, facts, tuple((question(keys[i]), values[i]) for i in asked))


def render_document(doc: Document, filler: tuple[str, ...]) -> str:
    slots = sorted(((round(f.depth * len(filler)), i) for i, f in enumerate(doc.facts)), reverse=True)
    sentences = list(filler)
    for index, i in slots:
        sentences.insert(index, doc.facts[i].sentence)
    lines = (" ".join(sentences[i : i + SENTENCES_PER_LINE]) for i in range(0, len(sentences), SENTENCES_PER_LINE))
    return f"{INSTRUCTION}\n\nDocument:\n" + "\n".join(lines)


def segments(doc: Document, filler: tuple[str, ...]) -> tuple[Segment, ...]:
    """Document (no loss), then for each QA: question (no loss) and ' code\\n' (loss)."""
    out = [Segment(render_document(doc, filler), False)]
    for q, a in doc.qa:
        out += [Segment(f"\n\nQuestion: {q}\nAnswer:", False), Segment(f" {a}\n", True)]
    return tuple(out)


def training_segments(seed: int, target_tokens: int, count_tokens: Callable[[str], int], tps: float) -> tuple[Segment, ...]:
    """One sized training example. One correction round: training does not need exact lengths."""
    doc = make_document(seed)
    fixed = count_tokens("".join(s.text for s in segments(doc, ())))
    n = max(0, round((target_tokens - fixed) / tps))
    segs = segments(doc, filler_sentences(n, seed))
    measured = count_tokens("".join(s.text for s in segs))
    n = max(0, n + round((target_tokens - measured) / tps))
    return segments(doc, filler_sentences(n, seed))

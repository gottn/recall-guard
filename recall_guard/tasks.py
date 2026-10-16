"""Case generators, one per stressor. Each is a pure function of its seed and returns a TaskInstance.

Vocabulary: keys are lockers ("KX-402"), values are six-digit access codes. Filler has no digits, so a
value in a completion can only have come from a planted sentence (or been invented)."""

import random

from recall_guard.types import Fact, TaskInstance

LETTERS = "ABCDEFGHJKLMNPQRSTUVWXYZ"  # no I or O: they read like digits
FIRST_NAMES = (
    "Maren", "Tobias", "Ingrid", "Lukas", "Freja", "Anders", "Sofie", "Mikkel", "Helle", "Rasmus",
    "Signe", "Jonas", "Astrid", "Emil", "Liv", "Oskar", "Nadia", "Viggo", "Clara", "Benjamin",
    "Ida", "Malthe", "Thea", "Noah", "Alma", "Elias", "Ella", "Villads", "Agnes", "Frederik",
    "Karla", "Storm",
)
LAST_NAMES = (
    "Holm", "Lund", "Berg", "Dahl", "Krog", "Juhl", "Vang", "Bech", "Rask", "Toft", "Munk", "Friis",
    "Bang", "Skov", "Lind", "Hald", "Kjaer", "Moll", "Nord", "Riis", "Stub", "Thor", "Vest", "Wulf",
    "Aaen", "Bork", "Dam", "Eeg", "Fogh", "Gram", "Hoeg", "Ibsen",
)
MANY_KEYS = 16
UPDATED_KEYS = 8
CHAINS = 8


def code(rng: random.Random) -> str:
    """Six digits, no leading zero."""
    return str(rng.randint(100_000, 999_999))


def distinct_codes(n: int, rng: random.Random) -> tuple[str, ...]:
    """`n` distinct six-digit codes that also differ in their first three digits (so no partial-copy credit)."""
    out: list[str] = []
    while len(out) < n:
        c = code(rng)
        if all(c[:3] != o[:3] for o in out):
            out.append(c)
    return tuple(out)


def random_keys(n: int, rng: random.Random) -> tuple[str, ...]:
    """`n` keys with distinct letter pairs and distinct numbers: 'QF-183', 'ZM-927', ..."""
    out: list[str] = []
    while len(out) < n:
        k = f"{rng.choice(LETTERS)}{rng.choice(LETTERS)}-{rng.randint(100, 999)}"
        if all(k[:2] != o[:2] and k[3:] != o[3:] for o in out):
            out.append(k)
    return tuple(out)


def similar_keys(n: int, rng: random.Random) -> tuple[str, ...]:
    """`n` keys sharing one letter pair with consecutive numbers: 'KX-401', 'KX-402', ..."""
    letters = f"{rng.choice(LETTERS)}{rng.choice(LETTERS)}"
    base = rng.randint(100, 999 - n)
    return tuple(f"{letters}-{base + i}" for i in range(n))


def depths(n: int, rng: random.Random) -> tuple[float, ...]:
    """`n` relative positions in [0.05, 0.95), unsorted so planting order is random."""
    return tuple(0.05 + 0.9 * rng.random() for _ in range(n))


def fact_sentence(key: str, value: str) -> str:
    return f"The access code for locker {key} is {value}."


def update_sentence(key: str, value: str) -> str:
    return f"Update: the access code for locker {key} has been changed to {value}."


def question(key: str) -> str:
    return f"What is the access code for locker {key}?"


def needle(seed: int) -> TaskInstance:
    """Control: one random key, one static fact (the classic needle-in-a-haystack)."""
    rng = random.Random(seed)
    (key,), (value,) = random_keys(1, rng), distinct_codes(1, rng)
    return TaskInstance("needle", (Fact(fact_sentence(key, value), depths(1, rng)[0]),), question(key), value, ())


def many_keys(task: str, keys: tuple[str, ...], seed: int) -> TaskInstance:
    rng = random.Random(seed + 1)
    values = distinct_codes(len(keys), rng)
    facts = tuple(Fact(fact_sentence(k, v), d) for k, v, d in zip(keys, values, depths(len(keys), rng), strict=True))
    target = rng.randrange(len(keys))
    others = tuple(v for i, v in enumerate(values) if i != target)
    return TaskInstance(task, facts, question(keys[target]), values[target], others)


def many_random(seed: int) -> TaskInstance:
    """16 unrelated keys; query one. Isolates load from key geometry."""
    return many_keys("many_random", random_keys(MANY_KEYS, random.Random(seed)), seed)


def many_similar(seed: int) -> TaskInstance:
    """16 near-duplicate keys; query one. The geometry stressor: similar keys collide in a fixed-size memory."""
    return many_keys("many_similar", similar_keys(MANY_KEYS, random.Random(seed)), seed)


def updated(seed: int) -> TaskInstance:
    """8 keys, each assigned a code and later changed. The answer is the latest value; the old one is the distractor."""
    rng = random.Random(seed)
    keys = random_keys(UPDATED_KEYS, rng)
    old, new = distinct_codes(UPDATED_KEYS, rng), distinct_codes(UPDATED_KEYS, random.Random(seed + 2))
    facts: list[Fact] = []
    for k, v_old, v_new in zip(keys, old, new, strict=True):
        d_old, d_new = sorted(depths(2, rng))
        facts += [Fact(fact_sentence(k, v_old), d_old), Fact(update_sentence(k, v_new), d_new)]
    target = rng.randrange(UPDATED_KEYS)
    return TaskInstance("updated", tuple(facts), question(keys[target]), new[target], (old[target],))


def multihop(seed: int) -> TaskInstance:
    """8 two-hop chains locker -> person -> code; query one chain end-to-end."""
    rng = random.Random(seed)
    keys, codes = random_keys(CHAINS, rng), distinct_codes(CHAINS, rng)
    names = tuple(f"{f} {s}" for f, s in zip(rng.sample(FIRST_NAMES, CHAINS), rng.sample(LAST_NAMES, CHAINS), strict=True))
    ds = depths(2 * CHAINS, rng)
    facts = tuple(
        f
        for i, (k, n, c) in enumerate(zip(keys, names, codes, strict=True))
        for f in (Fact(f"Locker {k} is assigned to {n}.", ds[2 * i]), Fact(f"The access code for {n} is {c}.", ds[2 * i + 1]))
    )
    target = rng.randrange(CHAINS)
    q = f"What is the access code for the person assigned to locker {keys[target]}?"
    return TaskInstance("multihop", facts, q, codes[target], tuple(c for i, c in enumerate(codes) if i != target))


TASKS = {
    "needle": needle,
    "many_random": many_random,
    "many_similar": many_similar,
    "updated": updated,
    "multihop": multihop,
}

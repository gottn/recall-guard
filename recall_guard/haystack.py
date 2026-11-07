"""RULER-style needle cases over haystacks of controlled repetition (exp10). The template is NVIDIA RULER's niah
template as its generator writes it (exp03_robust/RULER-PROVENANCE.md): an instruction line, the haystack in lines of
five sentences, each needle on a line of its own, then the question with its answer prefix. Haystack kinds:
p1 / p5 / p50 repeat the first 1, 5 or 50 sentences of NOISE in a fixed order (p5 is RULER's noise haystack); r50
deals the same 50 in a fresh order every cycle (repeated, no period); filler is filler.py's office text (no repeats).
The k values share one key: k = 1 is RULER's single needle, k = 4 its multi-value task. Distractors hold the
haystack's sentences (for filler, its sentence subjects), so a missed answer that copies the haystack scores stale."""

import random
from collections.abc import Callable

from recall_guard.filler import SUBJECTS, filler_sentences
from recall_guard.suite import case_seed
from recall_guard.types import Case

NOISE = (  # RULER's five sentences first, then 45 more in their register; no digits
    "The grass is green.", "The sky is blue.", "The sun is yellow.", "Here we go.", "There and back again.",
    "The snow is white.", "The night is dark.", "The sea is deep.", "The road is long.", "The hill is steep.",
    "The bread is warm.", "The milk is cold.", "The door is open.", "The bell is loud.", "The lake is still.",
    "The wind is strong.", "The rain is soft.", "The stone is hard.", "The leaf is thin.", "The river is wide.",
    "The moon is round.", "The fire is hot.", "The ice is smooth.", "The forest is quiet.", "The path is narrow.",
    "The cat is asleep.", "The dog is awake.", "The bird is small.", "The fish is quick.", "The horse is tall.",
    "The apple is red.", "The lemon is sour.", "The honey is sweet.", "The salt is dry.", "The tea is ready.",
    "Off we go.", "Up and away.", "Round and round.", "Back to the start.", "On and on.",
    "Here it comes.", "There it goes.", "Now and then.", "Step by step.", "Bit by bit.",
    "The clock is ticking.", "The kettle is boiling.", "The garden is growing.", "The window is clean.", "The story is over.",
)
ADJECTIVES = (
    "ancient", "bitter", "clever", "dusty", "eager", "fancy", "gentle", "hollow", "icy", "jolly", "keen", "lucky",
    "merry", "noble", "odd", "proud", "rapid", "shy", "tidy", "upset", "vivid", "witty", "zany", "brave",
)
NOUNS = (
    "anchor", "basket", "candle", "dolphin", "engine", "falcon", "glacier", "harbor", "island", "jacket", "kitten",
    "ladder", "meadow", "orchard", "pebble", "quilt", "rocket", "saddle", "tunnel", "umbrella", "violin", "walrus",
    "yacht", "zebra",
)
KINDS = ("p1", "p5", "p50", "r50", "filler")
PER_LINE = 5
SIZING_ROUNDS = 4
NEEDLE = "One of the special magic numbers for {key} is: {value}."
TEMPLATE = {  # one value, several values: RULER's instruction and question with its answer prefix
    False: ("A special magic number is hidden within the following text. Make sure to memorize it. I will quiz you about "
            "the number afterwards.", "What is the special magic number for {key} mentioned in the provided text? The "
            "special magic number for {key} mentioned in the provided text is"),
    True: ("Some special magic numbers are hidden within the following text. Make sure to memorize it. I will quiz you "
           "about the numbers afterwards.", "What are all the special magic numbers for {key} mentioned in the provided "
           "text? The special magic numbers for {key} mentioned in the provided text are"),
}


def sentences(kind: str, n: int, seed: int) -> tuple[str, ...]:
    """The first `n` haystack sentences of `kind`, a prefix of the same call with a larger `n`."""
    if kind == "filler":
        return filler_sentences(n, seed)
    period, rng, out = int(kind[1:]), random.Random(seed), []
    while len(out) < n:
        out += NOISE[:period] if kind[0] == "p" else rng.sample(NOISE[:period], period)
    return tuple(out[:n])


def render(kind: str, key: str, values: tuple[str, ...], depths: tuple[float, ...], n_lines: int, seed: int) -> str:
    """Instruction, `n_lines` haystack lines with each needle inserted as a line at round(depth * n_lines), question."""
    hay = sentences(kind, n_lines * PER_LINE, seed)
    lines = [" ".join(hay[i : i + PER_LINE]) for i in range(0, len(hay), PER_LINE)]
    for depth, value in sorted(zip(depths, values, strict=True), reverse=True):  # from the back: earlier slots stay put
        lines.insert(round(depth * n_lines), NEEDLE.format(key=key, value=value))
    head, question = TEMPLATE[len(values) > 1]
    return "\n".join((head, *lines, question.format(key=key)))


def build_case(kind: str, k: int, length: int, i: int, seed: int, count_tokens: Callable[[str], int]) -> Case:
    """One case sized to `length` reference tokens; key, values and depths depend on `seed` only, not on the kind."""
    rng = random.Random(seed)
    key = f"{rng.choice(ADJECTIVES)}-{rng.choice(NOUNS)}"
    values: list[str] = []
    while len(values) < k:  # seven digits as in RULER, distinct first three digits: no partial-copy credit
        v = str(rng.randint(1_000_000, 9_999_999))
        if all(v[:3] != o[:3] for o in values):
            values.append(v)
    depths = tuple(rng.uniform(0.05, 0.95) for _ in range(k))
    hay_seed = 2 * seed + 1
    empty = count_tokens(render(kind, key, tuple(values), depths, 0, hay_seed))
    per_line = (count_tokens(render(kind, key, tuple(values), depths, 64, hay_seed)) - empty) / 64
    n = max(1, round((length - empty) / per_line))
    prompt, measured = "", 0
    for _ in range(SIZING_ROUNDS):
        prompt = render(kind, key, tuple(values), depths, n, hay_seed)
        measured = count_tokens(prompt)
        if abs(measured - length) <= per_line:
            break
        n = max(1, n + round((length - measured) / per_line))
    task = f"hay_{kind}_k{k}"
    distractors = SUBJECTS if kind == "filler" else NOISE[: int(kind[1:])]
    return Case(f"{task}-{length}-{i:03d}", task, length, seed, prompt, "|".join(values), distractors, measured, "contains")


def build_sweep(
    cells: tuple[tuple[str, int], ...], lengths: tuple[int, ...], cases: int, seed: int, count_tokens: Callable[[str], int]
) -> tuple[Case, ...]:
    """Every (kind, k) cell x length x case; cells with the same k share their needles case by case."""
    return tuple(
        build_case(kind, k, length, i, case_seed(seed, k, li, i), count_tokens)
        for kind, k in cells for li, length in enumerate(lengths) for i in range(cases)
    )

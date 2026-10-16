"""Plain frozen records shared by every module. No behaviour lives here."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Fact:
    """One planted sentence and where it goes: depth in [0, 1) is the relative position in the document."""

    sentence: str
    depth: float


@dataclass(frozen=True)
class TaskInstance:
    """What a task generator returns: sentences to plant, the question, the answer, and wrong-but-plausible values."""

    task: str
    facts: tuple[Fact, ...]
    question: str
    answer: str
    distractors: tuple[str, ...]


@dataclass(frozen=True)
class Case:
    """A fully rendered prompt. `ref_tokens` is the measured length under the suite's reference tokenizer."""

    id: str
    task: str
    length_bucket: int
    seed: int
    prompt: str
    answer: str
    distractors: tuple[str, ...]
    ref_tokens: int


@dataclass(frozen=True)
class Result:
    """One model's completion for one case, already scored."""

    case_id: str
    task: str
    length_bucket: int
    model: str
    output: str
    contains: bool
    exact: bool
    stale: bool
    wall_s: float

"""Build a suite: tasks x lengths x cases, each prompt sized to a target token count under a reference tokenizer.
The tokenizer enters only as a `count_tokens` function, so this module stays pure and testable without models."""

from collections.abc import Callable
from dataclasses import dataclass

from recall_guard.filler import filler_sentences
from recall_guard.tasks import TASKS
from recall_guard.types import Case, TaskInstance

INSTRUCTION = "Read the document and answer the question with only the requested value."
LENGTHS = (1024, 2048, 4096, 8192, 16384, 32768)
SENTENCES_PER_LINE = 8
SIZING_ROUNDS = 3


@dataclass(frozen=True)
class SuiteSpec:
    tasks: tuple[str, ...]
    lengths: tuple[int, ...]
    cases_per_cell: int


def render(instance: TaskInstance, filler: tuple[str, ...]) -> str:
    """Plant each fact at index round(depth * len(filler)), then wrap in the completion-style prompt."""
    slots = sorted(((round(f.depth * len(filler)), i) for i, f in enumerate(instance.facts)), reverse=True)
    sentences = list(filler)
    for index, i in slots:  # insert from the back so earlier indices stay valid
        sentences.insert(index, instance.facts[i].sentence)
    lines = (" ".join(sentences[i : i + SENTENCES_PER_LINE]) for i in range(0, len(sentences), SENTENCES_PER_LINE))
    doc = "\n".join(lines)
    return f"{INSTRUCTION}\n\nDocument:\n{doc}\n\nQuestion: {instance.question}\nAnswer:"


def tokens_per_sentence(count_tokens: Callable[[str], int], seed: int = 0, n: int = 256) -> float:
    """Mean reference tokens per filler sentence, measured on `n` sentences."""
    return count_tokens(" ".join(filler_sentences(n, seed))) / n


def size_prompt(
    instance: TaskInstance, target: int, seed: int, count_tokens: Callable[[str], int], tps: float
) -> tuple[str, int]:
    """Choose the filler count so the rendered prompt lands on `target` tokens; a few correction rounds."""
    n = max(0, round((target - count_tokens(render(instance, ()))) / tps))
    prompt, measured = render(instance, filler_sentences(n, seed)), 0
    for _ in range(SIZING_ROUNDS):
        prompt = render(instance, filler_sentences(n, seed))
        measured = count_tokens(prompt)
        if abs(measured - target) <= tps:
            break
        n = max(0, n + round((target - measured) / tps))
    return prompt, measured


def case_seed(base_seed: int, task_index: int, length_index: int, i: int) -> int:
    return base_seed * 1_000_003 + task_index * 10_007 + length_index * 1_009 + i


def build_case(
    task: str, task_index: int, length: int, length_index: int, i: int, base_seed: int,
    count_tokens: Callable[[str], int], tps: float,
) -> Case:
    seed = case_seed(base_seed, task_index, length_index, i)
    instance = TASKS[task](seed)
    prompt, measured = size_prompt(instance, length, seed, count_tokens, tps)
    return Case(f"{task}-{length}-{i:03d}", task, length, seed, prompt, instance.answer, instance.distractors, measured)


def build_suite(spec: SuiteSpec, base_seed: int, count_tokens: Callable[[str], int]) -> tuple[Case, ...]:
    tps = tokens_per_sentence(count_tokens)
    return tuple(
        build_case(task, ti, length, li, i, base_seed, count_tokens, tps)
        for ti, task in enumerate(spec.tasks)
        for li, length in enumerate(spec.lengths)
        for i in range(spec.cases_per_cell)
    )

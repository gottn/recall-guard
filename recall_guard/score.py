"""Score one completion against a case. Values are six-digit codes, so scoring is a digit-group match on the
first non-empty line of the completion (the same 'contains' rule RULER uses for needle tests)."""

import re

from recall_guard.types import Case, Result

CODE_RE = re.compile(r"\d{6}")


def first_line(output: str) -> str:
    return next((ln.strip() for ln in output.splitlines() if ln.strip()), "")


def codes_in(text: str) -> tuple[str, ...]:
    return tuple(CODE_RE.findall(text))


def score(answer: str, distractors: tuple[str, ...], output: str) -> tuple[bool, bool, bool]:
    """(contains, exact, stale): answer anywhere on the first line; answer is the first code; a distractor
    appears while the answer does not."""
    codes = codes_in(first_line(output))
    contains = answer in codes
    exact = bool(codes) and codes[0] == answer
    stale = not contains and any(d in codes for d in distractors)
    return contains, exact, stale


def to_result(case: Case, model: str, output: str, wall_s: float) -> Result:
    contains, exact, stale = score(case.answer, case.distractors, output)
    return Result(case.id, case.task, case.length_bucket, model, output, contains, exact, stale, wall_s)

"""Thinking loops on MATH-500 (exp10). The edit's benefit, as the post measures it: the share of answers that run to the
token limit, with thinking on and the post's sampling settings. Pure helpers: the problem subset, the prompt, and the
scoring of one generation (did it stop, its final boxed answer, an exact match after light normalisation)."""

import re

DATASET = "HuggingFaceH4/MATH-500"
SUFFIX = "\nPlease reason step by step, and put your final answer within \\boxed{}."
SAMPLING = {"temperature": 0.6, "top_p": 0.95, "top_k": 20, "presence_penalty": 1.5}  # the post's evaluation settings
TAIL_CHARS = 4000  # kept per answer: the final answer and enough of a loop to see it
STRIP = (("\\left", ""), ("\\right", ""), ("\\!", ""), ("\\,", ""), ("\\dfrac", "\\frac"), ("\\tfrac", "\\frac"),
         ("^\\circ", ""), ("^{\\circ}", ""), ("$", ""), (" ", ""))


def subset(rows: tuple[dict, ...], per_level: int) -> tuple[dict, ...]:
    """The first `per_level` problems of each difficulty level 1-5, in dataset order."""
    return tuple(r for level in range(1, 6) for r in [r for r in rows if r["level"] == level][:per_level])


def finished_at(ids: list[int], stop: tuple[int, ...]) -> int:
    """1 + the index of the first stop token, or 0 when the generation never stopped (it hit the token limit)."""
    return next((i + 1 for i, t in enumerate(ids) if t in stop), 0)


def last_boxed(text: str) -> str:
    """Contents of the last \\boxed{...} with balanced braces; '' when there is none or it is cut off."""
    start = text.rfind("\\boxed{")
    if start < 0:
        return ""
    depth = 0
    for i in range(start + len("\\boxed"), len(text)):
        depth += {"{": 1, "}": -1}.get(text[i], 0)
        if depth == 0:
            return text[start + len("\\boxed{") : i]
    return ""


def normalize(answer: str) -> str:
    """Exact-match form: \\text{} unwrapped; no spaces, $, \\left / \\right, thin spaces or degree marks; dfrac -> frac."""
    out = re.sub(r"\\text\{([^}]*)\}", r"\1", answer)
    for old, new in STRIP:
        out = out.replace(old, new)
    return out.rstrip(".")


def record(row: dict, text: str, stop_at: int, generated_tokens: int, model: str, wall_s: float) -> dict:
    """One scored answer. Only a finished answer is graded, on the last boxed value after its think block."""
    boxed = last_boxed(text.rsplit("</think>", 1)[-1]) if stop_at else ""
    return {"id": row["unique_id"], "level": row["level"], "model": model, "finished": bool(stop_at),
            "new_tokens": stop_at or generated_tokens, "boxed": boxed, "answer": row["answer"],
            "correct": bool(boxed) and normalize(boxed) == normalize(row["answer"]), "tail": text[-TAIL_CHARS:],
            "wall_s": wall_s}

"""Convert NVIDIA RULER's generated needle records into Cases, so the same runner and report serve both suites.
RULER record: {"index", "input", "outputs": [...], "length", "answer_prefix", ...}. The prompt the model completes is
input + answer_prefix. A template passed through a shell leaves literal backslash-n pairs; they become newlines here.
Needle tasks list every value to find (rule "contains"); the QA tasks (qa_1 SQuAD, qa_2 HotpotQA) list alternative
answers, of which one suffices (rule "any"), as RULER scores them."""

from recall_guard.types import Case

MULTI = "|"


def to_case(task: str, length_bucket: int, record: dict) -> Case:
    prompt = (record["input"] + record.get("answer_prefix", "")).replace("\\n", "\n")
    answer = MULTI.join(record["outputs"])
    return Case(f"ruler_{task}-{length_bucket}-{record['index']}", f"ruler_{task}", length_bucket, int(record["index"]),
                prompt, answer, (), int(record["length"]), "any" if task.startswith("qa") else "contains")

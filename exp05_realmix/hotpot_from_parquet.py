"""HotpotQA distractor parquet (HuggingFace hotpotqa/hotpot_qa) -> the original hotpot_*.json layout that
recall_guard.real_data.hotpot_pool reads; the fallback when curtis.ml.cmu.edu (RULER's source) does not answer.
Needs pyarrow (not a repo dependency; any venv): python hotpot_from_parquet.py out.json <parquet files...>"""

import json
import sys

import pyarrow.parquet as pq

rows = []
for f in sys.argv[2:]:
    for r in pq.read_table(f).to_pylist():
        rows.append({
            "_id": r["id"], "question": r["question"], "answer": r["answer"], "type": r["type"], "level": r["level"],
            "supporting_facts": [list(x) for x in zip(r["supporting_facts"]["title"], r["supporting_facts"]["sent_id"], strict=True)],
            "context": [list(x) for x in zip(r["context"]["title"], r["context"]["sentences"], strict=True)],
        })
with open(sys.argv[1], "w") as out:
    json.dump(rows, out)
print(f"wrote {len(rows)} questions to {sys.argv[1]}")

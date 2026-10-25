# exp04 case provenance

Generated 2026-10-25 on the Mac by `exp04_realdocs/make_cases.sh <RULER clone> exp04_realdocs/results/cases` (six generator runs,
then `recall_guard.cli import-ruler`), from NVIDIA/RULER commit c3f5e3b (2026-07-22), `scripts/data/synthetic/qa.py`: tokenizer
Qwen/Qwen2.5-1.5B (hf), max_seq_length 4096 / 16384 / 32768, tokens_to_generate 32, num_samples 100, random_seed 42, RULER's `qa`
template plus its answer prefix ` Answer:` (passed through the shell, so literal backslash-n pairs, which the importer turns into
newlines). Source files, fetched with the URLs in RULER's `download_qa_dataset.sh`:
- `squad.json` = SQuAD dev v2.0, 4,370,528 bytes, sha256 `80a5225e94905956a6446d296ca1093975c4d3b3260f1d6c8f68bc2ab77182d8`
  (35 articles, 5,928 answerable questions).
- `hotpotqa.json` = hotpot_dev_distractor_v1.json, 61,065,698 bytes, sha256 `e3da074df24e8369009918aa5cdbdd254dadcde4c63f7569d36afd6f2268caa8`
  (7,405 questions, all level "hard").

RULER takes questions in file order. `qa_1` is the first 100 answerable SQuAD questions: 96 from the article "Normans"
(39 paragraphs) and 4 from "Computational_complexity_theory" (48 paragraphs); the gold paragraph sits among the other paragraphs
of its own article first, then paragraphs of other articles, so at 4K (23 documents) every distractor is a same-article paragraph.
`qa_2` is the first 100 HotpotQA dev questions (topically mixed), their two gold paragraphs among paragraphs of other questions.
Distractor sets differ by length (RULER seeds once per run); the questions do not. When a sample overflows the length RULER
drops documents in steps of ten, hence the ref_tokens spread. 600 cases, 42 MB, kept git-ignored in
`exp04_realdocs/results/cases/` on the Mac and in `aau:~/data/rg/ruler-qa/` on the cluster.

## Audit (`.venv/bin/python exp04_realdocs/audit_cases.py exp04_realdocs/results/cases`)

| task | ref tokens | n | rule | ends with ' Answer:' | answer in prompt | ref_tokens min-max | docs/prompt |
|---|---:|---:|---|---:|---:|---|---:|
| ruler_qa_1 | 4096 | 100 | any | 100 | 100 | 2094-4084 | 23 |
| ruler_qa_1 | 16384 | 100 | any | 100 | 100 | 13886-16367 | 94 |
| ruler_qa_1 | 32768 | 100 | any | 100 | 100 | 29317-32761 | 187 |
| ruler_qa_2 | 4096 | 100 | any | 100 | 95 | 2285-4077 | 22 |
| ruler_qa_2 | 16384 | 100 | any | 100 | 97 | 12646-16336 | 111 |
| ruler_qa_2 | 32768 | 100 | any | 100 | 98 | 28255-32765 | 229 |
ruler_qa_1: same questions at every length: True
ruler_qa_2: same questions at every length: True

"answer in prompt" is the oracle: a model that reads the gold paragraph can produce a scored answer. The qa_2 shortfall is
yes/no questions (the first qa_2 answer is "yes"), whose answer is not a span of the text.

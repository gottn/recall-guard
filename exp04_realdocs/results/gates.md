### base-Qwen_Qwen2.5-1.5B -> base-jet-ai_Jet-Nemotron-2B
baseline ('Qwen/Qwen2.5-1.5B',) vs candidate ('jet-ai/Jet-Nemotron-2B',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.45 | 0.38 | 110 | 65 | 0.000415 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.69 | 0.70 | 15 | 16 | 0.64 |  |
| ruler_qa_1 | 16384 | 100 | 0.45 | 0.39 | 21 | 15 | 0.203 |  |
| ruler_qa_1 | 32768 | 100 | 0.36 | 0.12 | 26 | 2 | 1.52e-06 | FAIL |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.50 | 11 | 11 | 0.584 |  |
| ruler_qa_2 | 16384 | 100 | 0.39 | 0.28 | 24 | 13 | 0.0494 |  |
| ruler_qa_2 | 32768 | 100 | 0.32 | 0.27 | 13 | 8 | 0.192 |  |

FAIL: recall regression in all cases pooled, ruler_qa_1@32768


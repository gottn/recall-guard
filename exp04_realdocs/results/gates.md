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

### base-jet-ai_Jet-Nemotron-2B -> repair-seed1-jet-ai_Jet-Nemotron-2B
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.38 | 0.40 | 54 | 70 | 0.937 |  |
| ruler_qa_1 | 4096 | 100 | 0.70 | 0.67 | 14 | 11 | 0.345 |  |
| ruler_qa_1 | 16384 | 100 | 0.39 | 0.42 | 14 | 17 | 0.763 |  |
| ruler_qa_1 | 32768 | 100 | 0.12 | 0.26 | 2 | 16 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.46 | 9 | 5 | 0.212 |  |
| ruler_qa_2 | 16384 | 100 | 0.28 | 0.33 | 8 | 13 | 0.905 |  |
| ruler_qa_2 | 32768 | 100 | 0.27 | 0.28 | 7 | 8 | 0.696 |  |

PASS: no recall regression

### base-Qwen_Qwen2.5-1.5B -> repair-seed1-Qwen_Qwen2.5-1.5B
baseline ('Qwen/Qwen2.5-1.5B',) vs candidate ('Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.45 | 0.46 | 61 | 64 | 0.64 |  |
| ruler_qa_1 | 4096 | 100 | 0.69 | 0.70 | 13 | 14 | 0.649 |  |
| ruler_qa_1 | 16384 | 100 | 0.45 | 0.50 | 12 | 17 | 0.868 |  |
| ruler_qa_1 | 32768 | 100 | 0.36 | 0.38 | 11 | 13 | 0.729 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.44 | 8 | 2 | 0.0547 |  |
| ruler_qa_2 | 16384 | 100 | 0.39 | 0.34 | 12 | 7 | 0.18 |  |
| ruler_qa_2 | 32768 | 100 | 0.32 | 0.38 | 5 | 11 | 0.962 |  |

PASS: no recall regression


### real QA: base -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.38 | 0.56 | 33 | 141 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.70 | 0.79 | 6 | 15 | 0.987 |  |
| ruler_qa_1 | 16384 | 100 | 0.39 | 0.75 | 2 | 38 | 1 |  |
| ruler_qa_1 | 32768 | 100 | 0.12 | 0.44 | 2 | 34 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.54 | 8 | 12 | 0.868 |  |
| ruler_qa_2 | 16384 | 100 | 0.28 | 0.46 | 8 | 26 | 1 |  |
| ruler_qa_2 | 32768 | 100 | 0.27 | 0.36 | 7 | 16 | 0.983 |  |

PASS: no recall regression

### real QA: synthetic -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.40 | 0.56 | 32 | 124 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.67 | 0.79 | 5 | 17 | 0.998 |  |
| ruler_qa_1 | 16384 | 100 | 0.42 | 0.75 | 3 | 36 | 1 |  |
| ruler_qa_1 | 32768 | 100 | 0.26 | 0.44 | 5 | 23 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.46 | 0.54 | 7 | 15 | 0.974 |  |
| ruler_qa_2 | 16384 | 100 | 0.33 | 0.46 | 7 | 20 | 0.997 |  |
| ruler_qa_2 | 32768 | 100 | 0.28 | 0.36 | 5 | 13 | 0.985 |  |

PASS: no recall regression

### real QA: realmix -> synthetic (jet-ai_Jet-Nemotron-2B), FAIL cells are realmix gains
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.40 | 124 | 32 | 2.76e-14 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.79 | 0.67 | 17 | 5 | 0.00845 |  |
| ruler_qa_1 | 16384 | 100 | 0.75 | 0.42 | 36 | 3 | 1.8e-08 | FAIL |
| ruler_qa_1 | 32768 | 100 | 0.44 | 0.26 | 23 | 5 | 0.000456 | FAIL |
| ruler_qa_2 | 4096 | 100 | 0.54 | 0.46 | 15 | 7 | 0.0669 |  |
| ruler_qa_2 | 16384 | 100 | 0.46 | 0.33 | 20 | 7 | 0.00958 |  |
| ruler_qa_2 | 32768 | 100 | 0.36 | 0.28 | 13 | 5 | 0.0481 |  |

FAIL: recall regression in all cases pooled, ruler_qa_1@16384, ruler_qa_1@32768

### real QA: source -> realmix (jet-ai_Jet-Nemotron-2B), the remaining deficit
baseline ('Qwen/Qwen2.5-1.5B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.45 | 0.56 | 61 | 124 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.69 | 0.79 | 11 | 21 | 0.975 |  |
| ruler_qa_1 | 16384 | 100 | 0.45 | 0.75 | 8 | 38 | 1 |  |
| ruler_qa_1 | 32768 | 100 | 0.36 | 0.44 | 17 | 25 | 0.918 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.54 | 9 | 13 | 0.857 |  |
| ruler_qa_2 | 16384 | 100 | 0.39 | 0.46 | 7 | 14 | 0.961 |  |
| ruler_qa_2 | 32768 | 100 | 0.32 | 0.36 | 9 | 13 | 0.857 |  |

PASS: no recall regression

### suite-s1: base -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.91 | 6 | 214 | 1 |  |
| heldout_many | 16384 | 50 | 0.86 | 0.98 | 0 | 6 | 1 |  |
| heldout_many | 32768 | 50 | 0.40 | 0.96 | 1 | 29 | 1 |  |
| many_random | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_random | 32768 | 50 | 0.26 | 0.98 | 1 | 37 | 1 |  |
| many_similar | 16384 | 50 | 0.76 | 1.00 | 0 | 12 | 1 |  |
| many_similar | 32768 | 50 | 0.24 | 0.96 | 1 | 37 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 0.62 | 0 | 22 | 1 |  |
| multihop | 32768 | 50 | 0.06 | 0.40 | 2 | 19 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 32768 | 50 | 0.60 | 0.98 | 1 | 20 | 1 |  |

PASS: no recall regression

### suite-s1: synthetic -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.99 | 0.91 | 51 | 2 | 1.59e-13 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.96 | 2 | 1 | 0.5 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| multihop | 16384 | 50 | 1.00 | 0.62 | 19 | 0 | 1.91e-06 | FAIL |
| multihop | 32768 | 50 | 0.88 | 0.40 | 25 | 1 | 4.02e-07 | FAIL |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled, multihop@16384, multihop@32768

### suite-s2: base -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.93 | 4 | 225 | 1 |  |
| heldout_many | 16384 | 50 | 0.92 | 1.00 | 0 | 4 | 1 |  |
| heldout_many | 32768 | 50 | 0.50 | 0.98 | 1 | 25 | 1 |  |
| many_random | 16384 | 50 | 0.50 | 1.00 | 0 | 25 | 1 |  |
| many_random | 32768 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| many_similar | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_similar | 32768 | 50 | 0.20 | 0.98 | 0 | 39 | 1 |  |
| multihop | 16384 | 50 | 0.22 | 0.68 | 0 | 23 | 1 |  |
| multihop | 32768 | 50 | 0.16 | 0.50 | 2 | 19 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.78 | 1.00 | 0 | 11 | 1 |  |
| updated | 32768 | 50 | 0.56 | 0.98 | 1 | 22 | 1 |  |

PASS: no recall regression

### suite-s2: synthetic -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.98 | 0.93 | 37 | 2 | 1.42e-09 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 50 | 0.94 | 0.68 | 14 | 1 | 0.000488 | FAIL |
| multihop | 32768 | 50 | 0.90 | 0.50 | 20 | 0 | 9.54e-07 | FAIL |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled, multihop@16384, multihop@32768

### heldout: base -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 0.99 | 0 | 20 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 25 | 0.24 | 0.92 | 0 | 17 | 1 |  |

PASS: no recall regression

### heldout: synthetic -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.99 | 2 | 1 | 0.5 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 0.96 | 0.92 | 2 | 1 | 0.5 |  |

PASS: no recall regression

### multihop25: base -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.17 | 0.65 | 2 | 75 | 1 |  |
| multihop | 1024 | 25 | 0.24 | 0.68 | 1 | 12 | 1 |  |
| multihop | 2048 | 25 | 0.08 | 0.56 | 0 | 12 | 1 |  |
| multihop | 4096 | 25 | 0.20 | 0.72 | 0 | 13 | 1 |  |
| multihop | 8192 | 25 | 0.20 | 0.60 | 1 | 11 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 0.64 | 0 | 12 | 1 |  |
| multihop | 32768 | 25 | 0.12 | 0.72 | 0 | 15 | 1 |  |

PASS: no recall regression

### multihop25: synthetic -> realmix (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.95 | 0.65 | 47 | 3 | 1.85e-11 | FAIL |
| multihop | 1024 | 25 | 1.00 | 0.68 | 8 | 0 | 0.00391 | FAIL |
| multihop | 2048 | 25 | 0.96 | 0.56 | 10 | 0 | 0.000977 | FAIL |
| multihop | 4096 | 25 | 0.96 | 0.72 | 7 | 1 | 0.0352 |  |
| multihop | 8192 | 25 | 0.92 | 0.60 | 9 | 1 | 0.0107 |  |
| multihop | 16384 | 25 | 1.00 | 0.64 | 9 | 0 | 0.00195 | FAIL |
| multihop | 32768 | 25 | 0.84 | 0.72 | 4 | 1 | 0.188 |  |

FAIL: recall regression in all cases pooled, multihop@1024, multihop@2048, multihop@16384

### real QA: base -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.48 | 0.64 | 35 | 129 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.86 | 0.91 | 3 | 8 | 0.967 |  |
| ruler_qa_1 | 16384 | 100 | 0.65 | 0.80 | 8 | 23 | 0.998 |  |
| ruler_qa_1 | 32768 | 100 | 0.19 | 0.72 | 1 | 54 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.54 | 8 | 11 | 0.82 |  |
| ruler_qa_2 | 16384 | 100 | 0.34 | 0.47 | 7 | 20 | 0.997 |  |
| ruler_qa_2 | 32768 | 100 | 0.35 | 0.40 | 8 | 13 | 0.905 |  |

PASS: no recall regression

### real QA: synthetic -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.64 | 36 | 83 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.81 | 0.91 | 2 | 12 | 0.999 |  |
| ruler_qa_1 | 16384 | 100 | 0.76 | 0.80 | 8 | 12 | 0.868 |  |
| ruler_qa_1 | 32768 | 100 | 0.56 | 0.72 | 4 | 20 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.54 | 6 | 10 | 0.895 |  |
| ruler_qa_2 | 16384 | 100 | 0.38 | 0.47 | 5 | 14 | 0.99 |  |
| ruler_qa_2 | 32768 | 100 | 0.36 | 0.40 | 11 | 15 | 0.837 |  |

PASS: no recall regression

### real QA: realmix -> synthetic (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are realmix gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.64 | 0.56 | 83 | 36 | 9.81e-06 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.91 | 0.81 | 12 | 2 | 0.00647 | FAIL |
| ruler_qa_1 | 16384 | 100 | 0.80 | 0.76 | 12 | 8 | 0.252 |  |
| ruler_qa_1 | 32768 | 100 | 0.72 | 0.56 | 20 | 4 | 0.000772 | FAIL |
| ruler_qa_2 | 4096 | 100 | 0.54 | 0.50 | 10 | 6 | 0.227 |  |
| ruler_qa_2 | 16384 | 100 | 0.47 | 0.38 | 14 | 5 | 0.0318 |  |
| ruler_qa_2 | 32768 | 100 | 0.40 | 0.36 | 15 | 11 | 0.279 |  |

FAIL: recall regression in all cases pooled, ruler_qa_1@4096, ruler_qa_1@32768

### real QA: source -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo), the remaining deficit
baseline ('meta-llama/Llama-3.1-8B-Instruct',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.74 | 0.64 | 91 | 30 | 1.25e-08 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.92 | 0.91 | 5 | 4 | 0.5 |  |
| ruler_qa_1 | 16384 | 100 | 0.82 | 0.80 | 10 | 8 | 0.407 |  |
| ruler_qa_1 | 32768 | 100 | 0.83 | 0.72 | 17 | 6 | 0.0173 |  |
| ruler_qa_2 | 4096 | 100 | 0.67 | 0.54 | 15 | 2 | 0.00117 | FAIL |
| ruler_qa_2 | 16384 | 100 | 0.64 | 0.47 | 22 | 5 | 0.000757 | FAIL |
| ruler_qa_2 | 32768 | 100 | 0.57 | 0.40 | 22 | 5 | 0.000757 | FAIL |

FAIL: recall regression in all cases pooled, ruler_qa_2@4096, ruler_qa_2@16384, ruler_qa_2@32768

### suite-s1: base -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.32 | 0.98 | 2 | 398 | 1 |  |
| heldout_many | 16384 | 50 | 0.24 | 0.98 | 0 | 37 | 1 |  |
| heldout_many | 32768 | 50 | 0.10 | 0.98 | 0 | 44 | 1 |  |
| many_random | 16384 | 50 | 0.16 | 0.98 | 1 | 42 | 1 |  |
| many_random | 32768 | 50 | 0.28 | 1.00 | 0 | 36 | 1 |  |
| many_similar | 16384 | 50 | 0.12 | 0.96 | 0 | 42 | 1 |  |
| many_similar | 32768 | 50 | 0.12 | 0.96 | 0 | 42 | 1 |  |
| multihop | 16384 | 50 | 0.12 | 0.98 | 0 | 43 | 1 |  |
| multihop | 32768 | 50 | 0.08 | 0.96 | 1 | 45 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.48 | 1.00 | 0 | 26 | 1 |  |
| updated | 32768 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |

PASS: no recall regression

### suite-s1: synthetic -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 1.00 | 0.98 | 10 | 1 | 0.00586 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_random | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| multihop | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| multihop | 32768 | 50 | 0.98 | 0.96 | 2 | 1 | 0.5 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

FAIL: recall regression in all cases pooled

### suite-s2: base -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.34 | 0.99 | 1 | 391 | 1 |  |
| heldout_many | 16384 | 50 | 0.42 | 1.00 | 0 | 29 | 1 |  |
| heldout_many | 32768 | 50 | 0.24 | 0.98 | 1 | 38 | 1 |  |
| many_random | 16384 | 50 | 0.34 | 1.00 | 0 | 33 | 1 |  |
| many_random | 32768 | 50 | 0.22 | 1.00 | 0 | 39 | 1 |  |
| many_similar | 16384 | 50 | 0.10 | 0.96 | 0 | 43 | 1 |  |
| many_similar | 32768 | 50 | 0.06 | 0.98 | 0 | 46 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.04 | 0.98 | 0 | 47 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| updated | 32768 | 50 | 0.14 | 1.00 | 0 | 43 | 1 |  |

PASS: no recall regression

### suite-s2: synthetic -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 1.00 | 0.99 | 5 | 2 | 0.227 |  |
| heldout_many | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| multihop | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### heldout: base -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.61 | 0.99 | 0 | 56 | 1 |  |
| heldout_many | 1024 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| heldout_many | 2048 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 4096 | 25 | 0.76 | 1.00 | 0 | 6 | 1 |  |
| heldout_many | 8192 | 25 | 0.64 | 0.96 | 0 | 8 | 1 |  |
| heldout_many | 16384 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| heldout_many | 32768 | 25 | 0.16 | 0.96 | 0 | 20 | 1 |  |

PASS: no recall regression

### heldout: synthetic -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 1.00 | 0.99 | 2 | 0 | 0.25 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |

PASS: no recall regression

### multihop25: base -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.30 | 0.99 | 0 | 104 | 1 |  |
| multihop | 1024 | 25 | 0.52 | 1.00 | 0 | 12 | 1 |  |
| multihop | 2048 | 25 | 0.28 | 0.96 | 0 | 17 | 1 |  |
| multihop | 4096 | 25 | 0.40 | 1.00 | 0 | 15 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |

PASS: no recall regression

### multihop25: synthetic -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 1.00 | 0.99 | 1 | 0 | 0.5 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 32768 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression


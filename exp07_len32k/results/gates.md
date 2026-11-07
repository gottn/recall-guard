### real QA: base -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.48 | 0.70 | 26 | 157 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.86 | 0.92 | 2 | 8 | 0.989 |  |
| ruler_qa_1 | 16384 | 100 | 0.65 | 0.83 | 5 | 23 | 1 |  |
| ruler_qa_1 | 32768 | 100 | 0.19 | 0.80 | 0 | 61 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.61 | 6 | 16 | 0.992 |  |
| ruler_qa_2 | 16384 | 100 | 0.34 | 0.52 | 7 | 25 | 1 |  |
| ruler_qa_2 | 32768 | 100 | 0.35 | 0.53 | 6 | 24 | 1 |  |

PASS: no recall regression

### real QA: budget -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.69 | 0.70 | 25 | 34 | 0.904 |  |
| ruler_qa_1 | 4096 | 100 | 0.92 | 0.92 | 2 | 2 | 0.688 |  |
| ruler_qa_1 | 16384 | 100 | 0.81 | 0.83 | 5 | 7 | 0.806 |  |
| ruler_qa_1 | 32768 | 100 | 0.79 | 0.80 | 2 | 3 | 0.812 |  |
| ruler_qa_2 | 4096 | 100 | 0.64 | 0.61 | 7 | 4 | 0.274 |  |
| ruler_qa_2 | 16384 | 100 | 0.49 | 0.52 | 5 | 8 | 0.867 |  |
| ruler_qa_2 | 32768 | 100 | 0.47 | 0.53 | 4 | 10 | 0.971 |  |

PASS: no recall regression

### real QA: budget32k -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget32k gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.70 | 0.69 | 34 | 25 | 0.149 |  |
| ruler_qa_1 | 4096 | 100 | 0.92 | 0.92 | 2 | 2 | 0.688 |  |
| ruler_qa_1 | 16384 | 100 | 0.83 | 0.81 | 7 | 5 | 0.387 |  |
| ruler_qa_1 | 32768 | 100 | 0.80 | 0.79 | 3 | 2 | 0.5 |  |
| ruler_qa_2 | 4096 | 100 | 0.61 | 0.64 | 4 | 7 | 0.887 |  |
| ruler_qa_2 | 16384 | 100 | 0.52 | 0.49 | 8 | 5 | 0.291 |  |
| ruler_qa_2 | 32768 | 100 | 0.53 | 0.47 | 10 | 4 | 0.0898 |  |

PASS: no recall regression

### real QA: base -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.38 | 0.25 | 114 | 36 | 6.12e-11 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.70 | 0.44 | 33 | 7 | 2.11e-05 | FAIL |
| ruler_qa_1 | 16384 | 100 | 0.39 | 0.27 | 19 | 7 | 0.0145 |  |
| ruler_qa_1 | 32768 | 100 | 0.12 | 0.12 | 6 | 6 | 0.613 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.27 | 26 | 3 | 7.62e-06 | FAIL |
| ruler_qa_2 | 16384 | 100 | 0.28 | 0.20 | 18 | 10 | 0.0925 |  |
| ruler_qa_2 | 32768 | 100 | 0.27 | 0.18 | 12 | 3 | 0.0176 |  |

FAIL: recall regression in all cases pooled, ruler_qa_1@4096, ruler_qa_2@4096

### real QA: synthetic -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.40 | 0.25 | 107 | 13 | 7.48e-20 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.67 | 0.44 | 23 | 0 | 1.19e-07 | FAIL |
| ruler_qa_1 | 16384 | 100 | 0.42 | 0.27 | 17 | 2 | 0.000364 | FAIL |
| ruler_qa_1 | 32768 | 100 | 0.26 | 0.12 | 15 | 1 | 0.000259 | FAIL |
| ruler_qa_2 | 4096 | 100 | 0.46 | 0.27 | 20 | 1 | 1.05e-05 | FAIL |
| ruler_qa_2 | 16384 | 100 | 0.33 | 0.20 | 18 | 5 | 0.00531 | FAIL |
| ruler_qa_2 | 32768 | 100 | 0.28 | 0.18 | 14 | 4 | 0.0154 |  |

FAIL: recall regression in all cases pooled, ruler_qa_1@4096, ruler_qa_1@16384, ruler_qa_1@32768, ruler_qa_2@4096, ruler_qa_2@16384

### suite-s1: base -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.32 | 0.99 | 0 | 399 | 1 |  |
| heldout_many | 16384 | 50 | 0.24 | 0.98 | 0 | 37 | 1 |  |
| heldout_many | 32768 | 50 | 0.10 | 0.98 | 0 | 44 | 1 |  |
| many_random | 16384 | 50 | 0.16 | 1.00 | 0 | 42 | 1 |  |
| many_random | 32768 | 50 | 0.28 | 1.00 | 0 | 36 | 1 |  |
| many_similar | 16384 | 50 | 0.12 | 1.00 | 0 | 44 | 1 |  |
| many_similar | 32768 | 50 | 0.12 | 1.00 | 0 | 44 | 1 |  |
| multihop | 16384 | 50 | 0.12 | 0.96 | 0 | 42 | 1 |  |
| multihop | 32768 | 50 | 0.08 | 0.94 | 0 | 43 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.48 | 1.00 | 0 | 26 | 1 |  |
| updated | 32768 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |

PASS: no recall regression

### suite-s1: gentle -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 1.00 | 0.99 | 7 | 1 | 0.0352 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| multihop | 32768 | 50 | 0.98 | 0.94 | 3 | 1 | 0.312 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

FAIL: recall regression in all cases pooled

### suite-s1: budget -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.96 | 0.99 | 7 | 23 | 0.999 |  |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 0.96 | 0.98 | 1 | 2 | 0.875 |  |
| many_random | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| many_random | 32768 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| many_similar | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| many_similar | 32768 | 50 | 0.84 | 1.00 | 0 | 8 | 1 |  |
| multihop | 16384 | 50 | 0.94 | 0.96 | 2 | 3 | 0.812 |  |
| multihop | 32768 | 50 | 0.90 | 0.94 | 3 | 5 | 0.855 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### suite-s1: budget32k -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget32k gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.99 | 0.96 | 23 | 7 | 0.00261 | FAIL |
| heldout_many | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.96 | 2 | 1 | 0.5 |  |
| many_random | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_random | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 32768 | 50 | 1.00 | 0.84 | 8 | 0 | 0.00391 | FAIL |
| multihop | 16384 | 50 | 0.96 | 0.94 | 3 | 2 | 0.5 |  |
| multihop | 32768 | 50 | 0.94 | 0.90 | 5 | 3 | 0.363 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled, many_similar@32768

### suite-s1: base -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.98 | 4 | 258 | 1 |  |
| heldout_many | 16384 | 50 | 0.86 | 0.98 | 1 | 7 | 0.996 |  |
| heldout_many | 32768 | 50 | 0.40 | 0.92 | 2 | 28 | 1 |  |
| many_random | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_random | 32768 | 50 | 0.26 | 1.00 | 0 | 37 | 1 |  |
| many_similar | 16384 | 50 | 0.76 | 1.00 | 0 | 12 | 1 |  |
| many_similar | 32768 | 50 | 0.24 | 0.96 | 1 | 37 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.06 | 0.94 | 0 | 44 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 32768 | 50 | 0.60 | 1.00 | 0 | 20 | 1 |  |

PASS: no recall regression

### suite-s1: synthetic -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.99 | 0.98 | 9 | 6 | 0.304 |  |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.92 | 4 | 1 | 0.188 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| multihop | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 32768 | 50 | 0.88 | 0.94 | 2 | 5 | 0.938 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### suite-s1: budget -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.97 | 0.98 | 10 | 15 | 0.885 |  |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.92 | 4 | 0 | 0.0625 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 0.98 | 0.96 | 2 | 1 | 0.5 |  |
| multihop | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| multihop | 32768 | 50 | 0.86 | 0.94 | 3 | 7 | 0.945 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### suite-s2: base -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.34 | 0.98 | 4 | 388 | 1 |  |
| heldout_many | 16384 | 50 | 0.42 | 0.98 | 0 | 28 | 1 |  |
| heldout_many | 32768 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| many_random | 16384 | 50 | 0.34 | 1.00 | 0 | 33 | 1 |  |
| many_random | 32768 | 50 | 0.22 | 1.00 | 0 | 39 | 1 |  |
| many_similar | 16384 | 50 | 0.10 | 0.96 | 1 | 44 | 1 |  |
| many_similar | 32768 | 50 | 0.06 | 0.96 | 0 | 45 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 0.94 | 3 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.04 | 0.94 | 0 | 45 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| updated | 32768 | 50 | 0.14 | 1.00 | 0 | 43 | 1 |  |

PASS: no recall regression

### suite-s2: gentle -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 1.00 | 0.98 | 11 | 2 | 0.0112 | FAIL |
| heldout_many | 16384 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| heldout_many | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 32768 | 50 | 0.98 | 0.96 | 2 | 1 | 0.5 |  |
| multihop | 16384 | 50 | 1.00 | 0.94 | 3 | 0 | 0.125 |  |
| multihop | 32768 | 50 | 1.00 | 0.94 | 3 | 0 | 0.125 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

FAIL: recall regression in all cases pooled

### suite-s2: budget -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.96 | 0.98 | 5 | 17 | 0.998 |  |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| many_random | 16384 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| many_random | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| many_similar | 16384 | 50 | 0.96 | 0.96 | 2 | 2 | 0.688 |  |
| many_similar | 32768 | 50 | 0.86 | 0.96 | 0 | 5 | 1 |  |
| multihop | 16384 | 50 | 0.96 | 0.94 | 2 | 1 | 0.5 |  |
| multihop | 32768 | 50 | 0.88 | 0.94 | 0 | 3 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### suite-s2: budget32k -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget32k gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.98 | 0.96 | 17 | 5 | 0.00845 | FAIL |
| heldout_many | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 16384 | 50 | 0.96 | 0.96 | 2 | 2 | 0.688 |  |
| many_similar | 32768 | 50 | 0.96 | 0.86 | 5 | 0 | 0.0312 |  |
| multihop | 16384 | 50 | 0.94 | 0.96 | 1 | 2 | 0.875 |  |
| multihop | 32768 | 50 | 0.94 | 0.88 | 3 | 0 | 0.125 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled

### suite-s2: base -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 1.00 | 0 | 263 | 1 |  |
| heldout_many | 16384 | 50 | 0.92 | 1.00 | 0 | 4 | 1 |  |
| heldout_many | 32768 | 50 | 0.50 | 0.98 | 0 | 24 | 1 |  |
| many_random | 16384 | 50 | 0.50 | 1.00 | 0 | 25 | 1 |  |
| many_random | 32768 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| many_similar | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_similar | 32768 | 50 | 0.20 | 1.00 | 0 | 40 | 1 |  |
| multihop | 16384 | 50 | 0.22 | 1.00 | 0 | 39 | 1 |  |
| multihop | 32768 | 50 | 0.16 | 0.98 | 0 | 41 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.78 | 1.00 | 0 | 11 | 1 |  |
| updated | 32768 | 50 | 0.56 | 1.00 | 0 | 22 | 1 |  |

PASS: no recall regression

### suite-s2: synthetic -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.98 | 1.00 | 2 | 9 | 0.994 |  |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 16384 | 50 | 0.94 | 1.00 | 0 | 3 | 1 |  |
| multihop | 32768 | 50 | 0.90 | 0.98 | 1 | 5 | 0.984 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### suite-s2: budget -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.97 | 1.00 | 2 | 17 | 1 |  |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 16384 | 50 | 0.82 | 1.00 | 0 | 9 | 1 |  |
| multihop | 32768 | 50 | 0.88 | 0.98 | 1 | 6 | 0.992 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### heldout: base -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.61 | 1.00 | 0 | 58 | 1 |  |
| heldout_many | 1024 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| heldout_many | 2048 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 4096 | 25 | 0.76 | 1.00 | 0 | 6 | 1 |  |
| heldout_many | 8192 | 25 | 0.64 | 1.00 | 0 | 9 | 1 |  |
| heldout_many | 16384 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| heldout_many | 32768 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |

PASS: no recall regression

### heldout: gentle -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### heldout: budget -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### heldout: budget32k -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget32k gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 1.00 | 0.99 | 1 | 0 | 0.5 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |

PASS: no recall regression

### heldout: base -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 0.97 | 1 | 19 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| heldout_many | 32768 | 25 | 0.24 | 0.88 | 0 | 16 | 1 |  |

PASS: no recall regression

### heldout: synthetic -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.97 | 3 | 0 | 0.125 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 25 | 0.96 | 0.88 | 2 | 0 | 0.25 |  |

PASS: no recall regression

### heldout: budget -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.97 | 3 | 1 | 0.312 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| heldout_many | 32768 | 25 | 0.96 | 0.88 | 2 | 0 | 0.25 |  |

PASS: no recall regression

### multihop25: base -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.30 | 0.98 | 0 | 102 | 1 |  |
| multihop | 1024 | 25 | 0.52 | 1.00 | 0 | 12 | 1 |  |
| multihop | 2048 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 4096 | 25 | 0.40 | 1.00 | 0 | 15 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 0.92 | 0 | 19 | 1 |  |
| multihop | 32768 | 25 | 0.16 | 0.96 | 0 | 20 | 1 |  |

PASS: no recall regression

### multihop25: gentle -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 1.00 | 0.98 | 3 | 0 | 0.125 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 16384 | 25 | 1.00 | 0.92 | 2 | 0 | 0.25 |  |
| multihop | 32768 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |

PASS: no recall regression

### multihop25: budget -> budget32k (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.95 | 0.98 | 3 | 7 | 0.945 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| multihop | 16384 | 25 | 1.00 | 0.92 | 2 | 0 | 0.25 |  |
| multihop | 32768 | 25 | 0.80 | 0.96 | 1 | 5 | 0.984 |  |

PASS: no recall regression

### multihop25: budget32k -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget32k gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget32k',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.98 | 0.95 | 7 | 3 | 0.172 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| multihop | 32768 | 25 | 0.96 | 0.80 | 5 | 1 | 0.109 |  |

PASS: no recall regression

### multihop25: base -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.17 | 0.99 | 0 | 123 | 1 |  |
| multihop | 1024 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| multihop | 2048 | 25 | 0.08 | 1.00 | 0 | 23 | 1 |  |
| multihop | 4096 | 25 | 0.20 | 1.00 | 0 | 20 | 1 |  |
| multihop | 8192 | 25 | 0.20 | 1.00 | 0 | 20 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 0.96 | 0 | 20 | 1 |  |
| multihop | 32768 | 25 | 0.12 | 0.96 | 0 | 21 | 1 |  |

PASS: no recall regression

### multihop25: synthetic -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.95 | 0.99 | 1 | 7 | 0.996 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| multihop | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| multihop | 8192 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| multihop | 16384 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 32768 | 25 | 0.84 | 0.96 | 0 | 3 | 1 |  |

PASS: no recall regression

### multihop25: budget -> syn1200 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 0.99 | 2 | 23 | 1 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 0.68 | 1.00 | 0 | 8 | 1 |  |
| multihop | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| multihop | 8192 | 25 | 0.84 | 1.00 | 0 | 4 | 1 |  |
| multihop | 16384 | 25 | 0.88 | 0.96 | 1 | 3 | 0.938 |  |
| multihop | 32768 | 25 | 0.72 | 0.96 | 1 | 7 | 0.996 |  |

PASS: no recall regression


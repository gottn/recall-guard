### suite-s1: base -> repair-seed1 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.99 | 0 | 257 | 1 |  |
| heldout_many | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| heldout_many | 32768 | 50 | 0.40 | 0.98 | 0 | 29 | 1 |  |
| many_random | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_random | 32768 | 50 | 0.26 | 1.00 | 0 | 37 | 1 |  |
| many_similar | 16384 | 50 | 0.76 | 1.00 | 0 | 12 | 1 |  |
| many_similar | 32768 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.06 | 0.88 | 0 | 41 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 32768 | 50 | 0.60 | 1.00 | 0 | 20 | 1 |  |

PASS: no recall regression

### suite-s2: base -> repair-seed1 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.98 | 0 | 256 | 1 |  |
| heldout_many | 16384 | 50 | 0.92 | 1.00 | 0 | 4 | 1 |  |
| heldout_many | 32768 | 50 | 0.50 | 0.98 | 0 | 24 | 1 |  |
| many_random | 16384 | 50 | 0.50 | 1.00 | 0 | 25 | 1 |  |
| many_random | 32768 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| many_similar | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_similar | 32768 | 50 | 0.20 | 1.00 | 0 | 40 | 1 |  |
| multihop | 16384 | 50 | 0.22 | 0.94 | 0 | 36 | 1 |  |
| multihop | 32768 | 50 | 0.16 | 0.90 | 0 | 37 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.78 | 1.00 | 0 | 11 | 1 |  |
| updated | 32768 | 50 | 0.56 | 1.00 | 0 | 22 | 1 |  |

PASS: no recall regression

### heldout: base -> repair-seed1 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 0.99 | 0 | 21 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 25 | 0.24 | 0.96 | 0 | 18 | 1 |  |

PASS: no recall regression

### multihop25: base -> repair-seed1 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.17 | 0.95 | 0 | 117 | 1 |  |
| multihop | 1024 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| multihop | 2048 | 25 | 0.08 | 0.96 | 0 | 22 | 1 |  |
| multihop | 4096 | 25 | 0.20 | 0.96 | 0 | 19 | 1 |  |
| multihop | 8192 | 25 | 0.20 | 0.92 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.12 | 0.84 | 0 | 18 | 1 |  |

PASS: no recall regression

### real QA: base -> repair-seed1 (jet-ai_Jet-Nemotron-2B)
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

### suite-s1: base -> repair-seed2 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.97 | 1 | 250 | 1 |  |
| heldout_many | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| heldout_many | 32768 | 50 | 0.40 | 0.94 | 0 | 27 | 1 |  |
| many_random | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_random | 32768 | 50 | 0.26 | 0.98 | 0 | 36 | 1 |  |
| many_similar | 16384 | 50 | 0.76 | 1.00 | 0 | 12 | 1 |  |
| many_similar | 32768 | 50 | 0.24 | 0.96 | 1 | 37 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 0.94 | 0 | 38 | 1 |  |
| multihop | 32768 | 50 | 0.06 | 0.88 | 0 | 41 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 32768 | 50 | 0.60 | 1.00 | 0 | 20 | 1 |  |

PASS: no recall regression

### suite-s2: base -> repair-seed2 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.98 | 2 | 256 | 1 |  |
| heldout_many | 16384 | 50 | 0.92 | 1.00 | 0 | 4 | 1 |  |
| heldout_many | 32768 | 50 | 0.50 | 0.98 | 0 | 24 | 1 |  |
| many_random | 16384 | 50 | 0.50 | 1.00 | 0 | 25 | 1 |  |
| many_random | 32768 | 50 | 0.36 | 0.98 | 0 | 31 | 1 |  |
| many_similar | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_similar | 32768 | 50 | 0.20 | 1.00 | 0 | 40 | 1 |  |
| multihop | 16384 | 50 | 0.22 | 0.94 | 2 | 38 | 1 |  |
| multihop | 32768 | 50 | 0.16 | 0.88 | 0 | 36 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.78 | 1.00 | 0 | 11 | 1 |  |
| updated | 32768 | 50 | 0.56 | 1.00 | 0 | 22 | 1 |  |

PASS: no recall regression

### heldout: base -> repair-seed2 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 1.00 | 0 | 22 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |

PASS: no recall regression

### multihop25: base -> repair-seed2 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.17 | 0.96 | 0 | 119 | 1 |  |
| multihop | 1024 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| multihop | 2048 | 25 | 0.08 | 0.96 | 0 | 22 | 1 |  |
| multihop | 4096 | 25 | 0.20 | 1.00 | 0 | 20 | 1 |  |
| multihop | 8192 | 25 | 0.20 | 0.88 | 0 | 17 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.12 | 0.92 | 0 | 20 | 1 |  |

PASS: no recall regression

### real QA: base -> repair-seed2 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.38 | 0.21 | 134 | 34 | 1.53e-15 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.70 | 0.37 | 41 | 8 | 9.82e-07 | FAIL |
| ruler_qa_1 | 16384 | 100 | 0.39 | 0.26 | 21 | 8 | 0.0121 |  |
| ruler_qa_1 | 32768 | 100 | 0.12 | 0.11 | 6 | 5 | 0.5 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.20 | 32 | 2 | 3.47e-08 | FAIL |
| ruler_qa_2 | 16384 | 100 | 0.28 | 0.17 | 18 | 7 | 0.0216 |  |
| ruler_qa_2 | 32768 | 100 | 0.27 | 0.15 | 16 | 4 | 0.00591 | FAIL |

FAIL: recall regression in all cases pooled, ruler_qa_1@4096, ruler_qa_2@4096, ruler_qa_2@32768

### suite-s1: base -> repair-seed3 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.97 | 2 | 246 | 1 |  |
| heldout_many | 16384 | 50 | 0.86 | 0.98 | 0 | 6 | 1 |  |
| heldout_many | 32768 | 50 | 0.40 | 0.90 | 1 | 26 | 1 |  |
| many_random | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_random | 32768 | 50 | 0.26 | 1.00 | 0 | 37 | 1 |  |
| many_similar | 16384 | 50 | 0.76 | 0.96 | 1 | 11 | 1 |  |
| many_similar | 32768 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 0.92 | 0 | 37 | 1 |  |
| multihop | 32768 | 50 | 0.06 | 0.84 | 0 | 39 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 32768 | 50 | 0.60 | 1.00 | 0 | 20 | 1 |  |

PASS: no recall regression

### suite-s2: base -> repair-seed3 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.98 | 1 | 252 | 1 |  |
| heldout_many | 16384 | 50 | 0.92 | 1.00 | 0 | 4 | 1 |  |
| heldout_many | 32768 | 50 | 0.50 | 0.96 | 1 | 24 | 1 |  |
| many_random | 16384 | 50 | 0.50 | 1.00 | 0 | 25 | 1 |  |
| many_random | 32768 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| many_similar | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_similar | 32768 | 50 | 0.20 | 1.00 | 0 | 40 | 1 |  |
| multihop | 16384 | 50 | 0.22 | 0.98 | 0 | 38 | 1 |  |
| multihop | 32768 | 50 | 0.16 | 0.78 | 0 | 31 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.78 | 1.00 | 0 | 11 | 1 |  |
| updated | 32768 | 50 | 0.56 | 1.00 | 0 | 22 | 1 |  |

PASS: no recall regression

### heldout: base -> repair-seed3 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3',): 150 shared cases, alpha 0.05

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

### multihop25: base -> repair-seed3 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.17 | 0.95 | 0 | 118 | 1 |  |
| multihop | 1024 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| multihop | 2048 | 25 | 0.08 | 0.96 | 0 | 22 | 1 |  |
| multihop | 4096 | 25 | 0.20 | 1.00 | 0 | 20 | 1 |  |
| multihop | 8192 | 25 | 0.20 | 0.92 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.12 | 0.84 | 0 | 18 | 1 |  |

PASS: no recall regression

### real QA: base -> repair-seed3 (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.38 | 0.47 | 25 | 81 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.70 | 0.80 | 4 | 14 | 0.996 |  |
| ruler_qa_1 | 16384 | 100 | 0.39 | 0.51 | 6 | 18 | 0.997 |  |
| ruler_qa_1 | 32768 | 100 | 0.12 | 0.22 | 3 | 13 | 0.998 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.56 | 6 | 12 | 0.952 |  |
| ruler_qa_2 | 16384 | 100 | 0.28 | 0.39 | 3 | 14 | 0.999 |  |
| ruler_qa_2 | 32768 | 100 | 0.27 | 0.34 | 3 | 10 | 0.989 |  |

PASS: no recall regression

### suite-s1: base -> repair-seed1-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.32 | 1.00 | 0 | 405 | 1 |  |
| heldout_many | 16384 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| heldout_many | 32768 | 50 | 0.10 | 1.00 | 0 | 45 | 1 |  |
| many_random | 16384 | 50 | 0.16 | 1.00 | 0 | 42 | 1 |  |
| many_random | 32768 | 50 | 0.28 | 1.00 | 0 | 36 | 1 |  |
| many_similar | 16384 | 50 | 0.12 | 1.00 | 0 | 44 | 1 |  |
| many_similar | 32768 | 50 | 0.12 | 1.00 | 0 | 44 | 1 |  |
| multihop | 16384 | 50 | 0.12 | 1.00 | 0 | 44 | 1 |  |
| multihop | 32768 | 50 | 0.08 | 0.98 | 0 | 45 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.48 | 1.00 | 0 | 26 | 1 |  |
| updated | 32768 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |

PASS: no recall regression

### suite-s2: base -> repair-seed1-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.34 | 1.00 | 0 | 393 | 1 |  |
| heldout_many | 16384 | 50 | 0.42 | 0.98 | 0 | 28 | 1 |  |
| heldout_many | 32768 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| many_random | 16384 | 50 | 0.34 | 1.00 | 0 | 33 | 1 |  |
| many_random | 32768 | 50 | 0.22 | 1.00 | 0 | 39 | 1 |  |
| many_similar | 16384 | 50 | 0.10 | 1.00 | 0 | 45 | 1 |  |
| many_similar | 32768 | 50 | 0.06 | 0.98 | 0 | 46 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.04 | 1.00 | 0 | 48 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| updated | 32768 | 50 | 0.14 | 1.00 | 0 | 43 | 1 |  |

PASS: no recall regression

### heldout: base -> repair-seed1-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',): 150 shared cases, alpha 0.05

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

### multihop25: base -> repair-seed1-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.30 | 1.00 | 0 | 105 | 1 |  |
| multihop | 1024 | 25 | 0.52 | 1.00 | 0 | 12 | 1 |  |
| multihop | 2048 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 4096 | 25 | 0.40 | 1.00 | 0 | 15 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |

PASS: no recall regression

### real QA: base -> repair-seed1-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.48 | 0.56 | 50 | 97 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.86 | 0.81 | 7 | 2 | 0.0898 |  |
| ruler_qa_1 | 16384 | 100 | 0.65 | 0.76 | 7 | 18 | 0.993 |  |
| ruler_qa_1 | 32768 | 100 | 0.19 | 0.56 | 3 | 40 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.50 | 12 | 11 | 0.5 |  |
| ruler_qa_2 | 16384 | 100 | 0.34 | 0.38 | 12 | 16 | 0.828 |  |
| ruler_qa_2 | 32768 | 100 | 0.35 | 0.36 | 9 | 10 | 0.676 |  |

PASS: no recall regression

### suite-s1: base -> repair-seed2-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.32 | 0.99 | 3 | 404 | 1 |  |
| heldout_many | 16384 | 50 | 0.24 | 0.98 | 1 | 38 | 1 |  |
| heldout_many | 32768 | 50 | 0.10 | 1.00 | 0 | 45 | 1 |  |
| many_random | 16384 | 50 | 0.16 | 1.00 | 0 | 42 | 1 |  |
| many_random | 32768 | 50 | 0.28 | 1.00 | 0 | 36 | 1 |  |
| many_similar | 16384 | 50 | 0.12 | 0.98 | 0 | 43 | 1 |  |
| many_similar | 32768 | 50 | 0.12 | 1.00 | 0 | 44 | 1 |  |
| multihop | 16384 | 50 | 0.12 | 0.98 | 1 | 44 | 1 |  |
| multihop | 32768 | 50 | 0.08 | 1.00 | 0 | 46 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.48 | 0.98 | 1 | 26 | 1 |  |
| updated | 32768 | 50 | 0.18 | 0.98 | 0 | 40 | 1 |  |

PASS: no recall regression

### suite-s2: base -> repair-seed2-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.34 | 1.00 | 0 | 393 | 1 |  |
| heldout_many | 16384 | 50 | 0.42 | 0.98 | 0 | 28 | 1 |  |
| heldout_many | 32768 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| many_random | 16384 | 50 | 0.34 | 1.00 | 0 | 33 | 1 |  |
| many_random | 32768 | 50 | 0.22 | 1.00 | 0 | 39 | 1 |  |
| many_similar | 16384 | 50 | 0.10 | 1.00 | 0 | 45 | 1 |  |
| many_similar | 32768 | 50 | 0.06 | 1.00 | 0 | 47 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.04 | 0.98 | 0 | 47 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| updated | 32768 | 50 | 0.14 | 1.00 | 0 | 43 | 1 |  |

PASS: no recall regression

### heldout: base -> repair-seed2-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle',): 150 shared cases, alpha 0.05

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

### multihop25: base -> repair-seed2-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.30 | 0.99 | 0 | 103 | 1 |  |
| multihop | 1024 | 25 | 0.52 | 1.00 | 0 | 12 | 1 |  |
| multihop | 2048 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 4096 | 25 | 0.40 | 1.00 | 0 | 15 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.16 | 0.92 | 0 | 19 | 1 |  |

PASS: no recall regression

### real QA: base -> repair-seed2-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.48 | 0.57 | 47 | 102 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.86 | 0.81 | 8 | 3 | 0.113 |  |
| ruler_qa_1 | 16384 | 100 | 0.65 | 0.68 | 11 | 14 | 0.788 |  |
| ruler_qa_1 | 32768 | 100 | 0.19 | 0.64 | 4 | 49 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.49 | 12 | 10 | 0.416 |  |
| ruler_qa_2 | 16384 | 100 | 0.34 | 0.45 | 6 | 17 | 0.995 |  |
| ruler_qa_2 | 32768 | 100 | 0.35 | 0.38 | 6 | 9 | 0.849 |  |

PASS: no recall regression

### suite-s1: base -> repair-seed3-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.32 | 0.99 | 0 | 401 | 1 |  |
| heldout_many | 16384 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| heldout_many | 32768 | 50 | 0.10 | 0.98 | 0 | 44 | 1 |  |
| many_random | 16384 | 50 | 0.16 | 1.00 | 0 | 42 | 1 |  |
| many_random | 32768 | 50 | 0.28 | 1.00 | 0 | 36 | 1 |  |
| many_similar | 16384 | 50 | 0.12 | 0.98 | 0 | 43 | 1 |  |
| many_similar | 32768 | 50 | 0.12 | 0.98 | 0 | 43 | 1 |  |
| multihop | 16384 | 50 | 0.12 | 0.98 | 0 | 43 | 1 |  |
| multihop | 32768 | 50 | 0.08 | 0.98 | 0 | 45 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.48 | 1.00 | 0 | 26 | 1 |  |
| updated | 32768 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |

PASS: no recall regression

### suite-s2: base -> repair-seed3-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.34 | 0.99 | 1 | 391 | 1 |  |
| heldout_many | 16384 | 50 | 0.42 | 0.98 | 0 | 28 | 1 |  |
| heldout_many | 32768 | 50 | 0.24 | 0.98 | 0 | 37 | 1 |  |
| many_random | 16384 | 50 | 0.34 | 0.98 | 1 | 33 | 1 |  |
| many_random | 32768 | 50 | 0.22 | 0.98 | 0 | 38 | 1 |  |
| many_similar | 16384 | 50 | 0.10 | 1.00 | 0 | 45 | 1 |  |
| many_similar | 32768 | 50 | 0.06 | 1.00 | 0 | 47 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 1.00 | 0 | 41 | 1 |  |
| multihop | 32768 | 50 | 0.04 | 0.98 | 0 | 47 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| updated | 32768 | 50 | 0.14 | 1.00 | 0 | 43 | 1 |  |

PASS: no recall regression

### heldout: base -> repair-seed3-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.61 | 0.99 | 1 | 57 | 1 |  |
| heldout_many | 1024 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| heldout_many | 2048 | 25 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| heldout_many | 4096 | 25 | 0.76 | 1.00 | 0 | 6 | 1 |  |
| heldout_many | 8192 | 25 | 0.64 | 1.00 | 0 | 9 | 1 |  |
| heldout_many | 16384 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| heldout_many | 32768 | 25 | 0.16 | 0.96 | 0 | 20 | 1 |  |

PASS: no recall regression

### multihop25: base -> repair-seed3-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.30 | 0.98 | 0 | 102 | 1 |  |
| multihop | 1024 | 25 | 0.52 | 0.96 | 0 | 11 | 1 |  |
| multihop | 2048 | 25 | 0.28 | 0.96 | 0 | 17 | 1 |  |
| multihop | 4096 | 25 | 0.40 | 1.00 | 0 | 15 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 1.00 | 0 | 18 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.16 | 0.96 | 0 | 20 | 1 |  |

PASS: no recall regression

### real QA: base -> repair-seed3-gentle (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.48 | 0.55 | 58 | 99 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.86 | 0.79 | 10 | 3 | 0.0461 |  |
| ruler_qa_1 | 16384 | 100 | 0.65 | 0.72 | 11 | 18 | 0.932 |  |
| ruler_qa_1 | 32768 | 100 | 0.19 | 0.56 | 5 | 42 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.51 | 13 | 13 | 0.577 |  |
| ruler_qa_2 | 16384 | 100 | 0.34 | 0.37 | 11 | 14 | 0.788 |  |
| ruler_qa_2 | 32768 | 100 | 0.35 | 0.36 | 8 | 9 | 0.685 |  |

PASS: no recall regression


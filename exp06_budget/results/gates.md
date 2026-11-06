### real QA: base -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.38 | 0.56 | 41 | 152 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.70 | 0.82 | 7 | 19 | 0.995 |  |
| ruler_qa_1 | 16384 | 100 | 0.39 | 0.72 | 3 | 36 | 1 |  |
| ruler_qa_1 | 32768 | 100 | 0.12 | 0.45 | 2 | 35 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.51 | 12 | 13 | 0.655 |  |
| ruler_qa_2 | 16384 | 100 | 0.28 | 0.44 | 9 | 25 | 0.999 |  |
| ruler_qa_2 | 32768 | 100 | 0.27 | 0.43 | 8 | 24 | 0.999 |  |

PASS: no recall regression

### real QA: synthetic -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.40 | 0.56 | 34 | 129 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.67 | 0.82 | 4 | 19 | 1 |  |
| ruler_qa_1 | 16384 | 100 | 0.42 | 0.72 | 1 | 31 | 1 |  |
| ruler_qa_1 | 32768 | 100 | 0.26 | 0.45 | 4 | 23 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.46 | 0.51 | 10 | 15 | 0.885 |  |
| ruler_qa_2 | 16384 | 100 | 0.33 | 0.44 | 9 | 20 | 0.988 |  |
| ruler_qa_2 | 32768 | 100 | 0.28 | 0.43 | 6 | 21 | 0.999 |  |

PASS: no recall regression

### real QA: realmix -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.56 | 36 | 39 | 0.678 |  |
| ruler_qa_1 | 4096 | 100 | 0.79 | 0.82 | 3 | 6 | 0.91 |  |
| ruler_qa_1 | 16384 | 100 | 0.75 | 0.72 | 7 | 4 | 0.274 |  |
| ruler_qa_1 | 32768 | 100 | 0.44 | 0.45 | 8 | 9 | 0.685 |  |
| ruler_qa_2 | 4096 | 100 | 0.54 | 0.51 | 8 | 5 | 0.291 |  |
| ruler_qa_2 | 16384 | 100 | 0.46 | 0.44 | 6 | 4 | 0.377 |  |
| ruler_qa_2 | 32768 | 100 | 0.36 | 0.43 | 4 | 11 | 0.982 |  |

PASS: no recall regression

### real QA: budget -> realmix (jet-ai_Jet-Nemotron-2B), FAIL cells are budget gains
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.56 | 39 | 36 | 0.409 |  |
| ruler_qa_1 | 4096 | 100 | 0.82 | 0.79 | 6 | 3 | 0.254 |  |
| ruler_qa_1 | 16384 | 100 | 0.72 | 0.75 | 4 | 7 | 0.887 |  |
| ruler_qa_1 | 32768 | 100 | 0.45 | 0.44 | 9 | 8 | 0.5 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.54 | 5 | 8 | 0.867 |  |
| ruler_qa_2 | 16384 | 100 | 0.44 | 0.46 | 4 | 6 | 0.828 |  |
| ruler_qa_2 | 32768 | 100 | 0.43 | 0.36 | 11 | 4 | 0.0592 |  |

PASS: no recall regression

### suite-s1: base -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.97 | 3 | 252 | 1 |  |
| heldout_many | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| heldout_many | 32768 | 50 | 0.40 | 1.00 | 0 | 30 | 1 |  |
| many_random | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_random | 32768 | 50 | 0.26 | 1.00 | 0 | 37 | 1 |  |
| many_similar | 16384 | 50 | 0.76 | 1.00 | 0 | 12 | 1 |  |
| many_similar | 32768 | 50 | 0.24 | 0.98 | 0 | 37 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 0.86 | 1 | 35 | 1 |  |
| multihop | 32768 | 50 | 0.06 | 0.86 | 2 | 42 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 32768 | 50 | 0.60 | 1.00 | 0 | 20 | 1 |  |

PASS: no recall regression

### suite-s1: synthetic -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.99 | 0.97 | 13 | 5 | 0.0481 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 50 | 1.00 | 0.86 | 7 | 0 | 0.00781 |  |
| multihop | 32768 | 50 | 0.88 | 0.86 | 5 | 4 | 0.5 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |

FAIL: recall regression in all cases pooled

### suite-s1: realmix -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.91 | 0.97 | 2 | 43 | 1 |  |
| heldout_many | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 0.96 | 0.98 | 0 | 1 | 1 |  |
| multihop | 16384 | 50 | 0.62 | 0.86 | 1 | 13 | 1 |  |
| multihop | 32768 | 50 | 0.40 | 0.86 | 1 | 24 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### suite-s1: budget -> realmix (jet-ai_Jet-Nemotron-2B), FAIL cells are budget gains
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.97 | 0.91 | 43 | 2 | 2.94e-11 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 0.98 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 50 | 0.86 | 0.62 | 13 | 1 | 0.000916 | FAIL |
| multihop | 32768 | 50 | 0.86 | 0.40 | 24 | 1 | 7.75e-07 | FAIL |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled, multihop@16384, multihop@32768

### suite-s2: base -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.97 | 3 | 251 | 1 |  |
| heldout_many | 16384 | 50 | 0.92 | 1.00 | 0 | 4 | 1 |  |
| heldout_many | 32768 | 50 | 0.50 | 0.98 | 1 | 25 | 1 |  |
| many_random | 16384 | 50 | 0.50 | 1.00 | 0 | 25 | 1 |  |
| many_random | 32768 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| many_similar | 16384 | 50 | 0.64 | 1.00 | 0 | 18 | 1 |  |
| many_similar | 32768 | 50 | 0.20 | 1.00 | 0 | 40 | 1 |  |
| multihop | 16384 | 50 | 0.22 | 0.82 | 1 | 31 | 1 |  |
| multihop | 32768 | 50 | 0.16 | 0.88 | 0 | 36 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 0.86 | 1.00 | 0 | 7 | 1 |  |
| updated | 16384 | 50 | 0.78 | 1.00 | 0 | 11 | 1 |  |
| updated | 32768 | 50 | 0.56 | 0.98 | 1 | 22 | 1 |  |

PASS: no recall regression

### suite-s2: synthetic -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.98 | 0.97 | 14 | 6 | 0.0577 |  |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 16384 | 50 | 0.94 | 0.82 | 8 | 2 | 0.0547 |  |
| multihop | 32768 | 50 | 0.90 | 0.88 | 4 | 3 | 0.5 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

PASS: no recall regression

### suite-s2: realmix -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.93 | 0.97 | 7 | 34 | 1 |  |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| multihop | 16384 | 50 | 0.68 | 0.82 | 4 | 11 | 0.982 |  |
| multihop | 32768 | 50 | 0.50 | 0.88 | 1 | 20 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |

PASS: no recall regression

### suite-s2: budget -> realmix (jet-ai_Jet-Nemotron-2B), FAIL cells are budget gains
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.97 | 0.93 | 34 | 7 | 1.27e-05 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_similar | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 50 | 0.82 | 0.68 | 11 | 4 | 0.0592 |  |
| multihop | 32768 | 50 | 0.88 | 0.50 | 20 | 1 | 1.05e-05 | FAIL |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |

FAIL: recall regression in all cases pooled, multihop@32768

### heldout: base -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 0.99 | 1 | 21 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| heldout_many | 32768 | 25 | 0.24 | 0.96 | 0 | 18 | 1 |  |

PASS: no recall regression

### heldout: synthetic -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.99 | 2 | 1 | 0.5 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 25 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |

PASS: no recall regression

### heldout: realmix -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.99 | 1 | 1 | 0.75 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 25 | 0.92 | 0.96 | 0 | 1 | 1 |  |

PASS: no recall regression

### heldout: budget -> realmix (jet-ai_Jet-Nemotron-2B), FAIL cells are budget gains
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.99 | 1 | 1 | 0.75 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 25 | 0.96 | 0.92 | 1 | 0 | 0.5 |  |

PASS: no recall regression

### multihop25: base -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.17 | 0.85 | 0 | 102 | 1 |  |
| multihop | 1024 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| multihop | 2048 | 25 | 0.08 | 0.68 | 0 | 15 | 1 |  |
| multihop | 4096 | 25 | 0.20 | 0.96 | 0 | 19 | 1 |  |
| multihop | 8192 | 25 | 0.20 | 0.84 | 0 | 16 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 0.88 | 0 | 18 | 1 |  |
| multihop | 32768 | 25 | 0.12 | 0.72 | 0 | 15 | 1 |  |

PASS: no recall regression

### multihop25: synthetic -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.95 | 0.85 | 18 | 3 | 0.000745 | FAIL |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 0.96 | 0.68 | 8 | 1 | 0.0195 |  |
| multihop | 4096 | 25 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| multihop | 8192 | 25 | 0.92 | 0.84 | 2 | 0 | 0.25 |  |
| multihop | 16384 | 25 | 1.00 | 0.88 | 3 | 0 | 0.125 |  |
| multihop | 32768 | 25 | 0.84 | 0.72 | 4 | 1 | 0.188 |  |

FAIL: recall regression in all cases pooled

### multihop25: realmix -> budget (jet-ai_Jet-Nemotron-2B)
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.65 | 0.85 | 7 | 36 | 1 |  |
| multihop | 1024 | 25 | 0.68 | 1.00 | 0 | 8 | 1 |  |
| multihop | 2048 | 25 | 0.56 | 0.68 | 2 | 5 | 0.938 |  |
| multihop | 4096 | 25 | 0.72 | 0.96 | 0 | 6 | 1 |  |
| multihop | 8192 | 25 | 0.60 | 0.84 | 1 | 7 | 0.996 |  |
| multihop | 16384 | 25 | 0.64 | 0.88 | 2 | 8 | 0.989 |  |
| multihop | 32768 | 25 | 0.72 | 0.72 | 2 | 2 | 0.688 |  |

PASS: no recall regression

### multihop25: budget -> realmix (jet-ai_Jet-Nemotron-2B), FAIL cells are budget gains
baseline ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget',) vs candidate ('jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.85 | 0.65 | 36 | 7 | 4.48e-06 | FAIL |
| multihop | 1024 | 25 | 1.00 | 0.68 | 8 | 0 | 0.00391 | FAIL |
| multihop | 2048 | 25 | 0.68 | 0.56 | 5 | 2 | 0.227 |  |
| multihop | 4096 | 25 | 0.96 | 0.72 | 6 | 0 | 0.0156 |  |
| multihop | 8192 | 25 | 0.84 | 0.60 | 7 | 1 | 0.0352 |  |
| multihop | 16384 | 25 | 0.88 | 0.64 | 8 | 2 | 0.0547 |  |
| multihop | 32768 | 25 | 0.72 | 0.72 | 2 | 2 | 0.688 |  |

FAIL: recall regression in all cases pooled, multihop@1024

### real QA: base -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.48 | 0.69 | 34 | 156 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.86 | 0.92 | 3 | 9 | 0.981 |  |
| ruler_qa_1 | 16384 | 100 | 0.65 | 0.81 | 7 | 23 | 0.999 |  |
| ruler_qa_1 | 32768 | 100 | 0.19 | 0.79 | 0 | 60 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.51 | 0.64 | 6 | 19 | 0.998 |  |
| ruler_qa_2 | 16384 | 100 | 0.34 | 0.49 | 9 | 24 | 0.998 |  |
| ruler_qa_2 | 32768 | 100 | 0.35 | 0.47 | 9 | 21 | 0.992 |  |

PASS: no recall regression

### real QA: synthetic -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.69 | 30 | 105 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.81 | 0.92 | 0 | 11 | 1 |  |
| ruler_qa_1 | 16384 | 100 | 0.76 | 0.81 | 7 | 12 | 0.916 |  |
| ruler_qa_1 | 32768 | 100 | 0.56 | 0.79 | 2 | 25 | 1 |  |
| ruler_qa_2 | 4096 | 100 | 0.50 | 0.64 | 5 | 19 | 0.999 |  |
| ruler_qa_2 | 16384 | 100 | 0.38 | 0.49 | 7 | 18 | 0.993 |  |
| ruler_qa_2 | 32768 | 100 | 0.36 | 0.47 | 9 | 20 | 0.988 |  |

PASS: no recall regression

### real QA: realmix -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.64 | 0.69 | 19 | 47 | 1 |  |
| ruler_qa_1 | 4096 | 100 | 0.91 | 0.92 | 2 | 3 | 0.812 |  |
| ruler_qa_1 | 16384 | 100 | 0.80 | 0.81 | 4 | 5 | 0.746 |  |
| ruler_qa_1 | 32768 | 100 | 0.72 | 0.79 | 2 | 9 | 0.994 |  |
| ruler_qa_2 | 4096 | 100 | 0.54 | 0.64 | 3 | 13 | 0.998 |  |
| ruler_qa_2 | 16384 | 100 | 0.47 | 0.49 | 5 | 7 | 0.806 |  |
| ruler_qa_2 | 32768 | 100 | 0.40 | 0.47 | 3 | 10 | 0.989 |  |

PASS: no recall regression

### real QA: budget -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.69 | 0.64 | 47 | 19 | 0.000378 | FAIL |
| ruler_qa_1 | 4096 | 100 | 0.92 | 0.91 | 3 | 2 | 0.5 |  |
| ruler_qa_1 | 16384 | 100 | 0.81 | 0.80 | 5 | 4 | 0.5 |  |
| ruler_qa_1 | 32768 | 100 | 0.79 | 0.72 | 9 | 2 | 0.0327 |  |
| ruler_qa_2 | 4096 | 100 | 0.64 | 0.54 | 13 | 3 | 0.0106 |  |
| ruler_qa_2 | 16384 | 100 | 0.49 | 0.47 | 7 | 5 | 0.387 |  |
| ruler_qa_2 | 32768 | 100 | 0.47 | 0.40 | 10 | 3 | 0.0461 |  |

FAIL: recall regression in all cases pooled

### suite-s1: base -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.32 | 0.96 | 4 | 387 | 1 |  |
| heldout_many | 16384 | 50 | 0.24 | 1.00 | 0 | 38 | 1 |  |
| heldout_many | 32768 | 50 | 0.10 | 0.96 | 1 | 44 | 1 |  |
| many_random | 16384 | 50 | 0.16 | 0.98 | 0 | 41 | 1 |  |
| many_random | 32768 | 50 | 0.28 | 0.96 | 1 | 35 | 1 |  |
| many_similar | 16384 | 50 | 0.12 | 0.98 | 0 | 43 | 1 |  |
| many_similar | 32768 | 50 | 0.12 | 0.84 | 0 | 36 | 1 |  |
| multihop | 16384 | 50 | 0.12 | 0.94 | 1 | 42 | 1 |  |
| multihop | 32768 | 50 | 0.08 | 0.90 | 1 | 42 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.48 | 1.00 | 0 | 26 | 1 |  |
| updated | 32768 | 50 | 0.18 | 0.98 | 0 | 40 | 1 |  |

PASS: no recall regression

### suite-s1: synthetic -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 1.00 | 0.96 | 23 | 1 | 1.49e-06 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_random | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 32768 | 50 | 1.00 | 0.84 | 8 | 0 | 0.00391 | FAIL |
| multihop | 16384 | 50 | 1.00 | 0.94 | 3 | 0 | 0.125 |  |
| multihop | 32768 | 50 | 0.98 | 0.90 | 5 | 1 | 0.109 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled, many_similar@32768

### suite-s1: realmix -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.98 | 0.96 | 20 | 7 | 0.00958 | FAIL |
| heldout_many | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.96 | 2 | 1 | 0.5 |  |
| many_random | 16384 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 16384 | 50 | 0.96 | 0.98 | 0 | 1 | 1 |  |
| many_similar | 32768 | 50 | 0.96 | 0.84 | 7 | 1 | 0.0352 |  |
| multihop | 16384 | 50 | 0.98 | 0.94 | 3 | 1 | 0.312 |  |
| multihop | 32768 | 50 | 0.96 | 0.90 | 4 | 1 | 0.188 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled

### suite-s1: budget -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.96 | 0.98 | 7 | 20 | 0.997 |  |
| heldout_many | 16384 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 50 | 0.96 | 0.98 | 1 | 2 | 0.875 |  |
| many_random | 16384 | 50 | 0.98 | 0.98 | 1 | 1 | 0.75 |  |
| many_random | 32768 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| many_similar | 16384 | 50 | 0.98 | 0.96 | 1 | 0 | 0.5 |  |
| many_similar | 32768 | 50 | 0.84 | 0.96 | 1 | 7 | 0.996 |  |
| multihop | 16384 | 50 | 0.94 | 0.98 | 1 | 3 | 0.938 |  |
| multihop | 32768 | 50 | 0.90 | 0.96 | 1 | 4 | 0.969 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### suite-s2: base -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.34 | 0.96 | 2 | 374 | 1 |  |
| heldout_many | 16384 | 50 | 0.42 | 1.00 | 0 | 29 | 1 |  |
| heldout_many | 32768 | 50 | 0.24 | 0.96 | 1 | 37 | 1 |  |
| many_random | 16384 | 50 | 0.34 | 0.96 | 0 | 31 | 1 |  |
| many_random | 32768 | 50 | 0.22 | 0.98 | 0 | 38 | 1 |  |
| many_similar | 16384 | 50 | 0.10 | 0.96 | 0 | 43 | 1 |  |
| many_similar | 32768 | 50 | 0.06 | 0.86 | 0 | 40 | 1 |  |
| multihop | 16384 | 50 | 0.18 | 0.96 | 1 | 40 | 1 |  |
| multihop | 32768 | 50 | 0.04 | 0.88 | 0 | 42 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.36 | 1.00 | 0 | 32 | 1 |  |
| updated | 32768 | 50 | 0.14 | 0.98 | 0 | 42 | 1 |  |

PASS: no recall regression

### suite-s2: synthetic -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 1.00 | 0.96 | 23 | 2 | 9.72e-06 | FAIL |
| heldout_many | 16384 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_similar | 32768 | 50 | 0.98 | 0.86 | 7 | 1 | 0.0352 |  |
| multihop | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| multihop | 32768 | 50 | 1.00 | 0.88 | 6 | 0 | 0.0156 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled

### suite-s2: realmix -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.99 | 0.96 | 19 | 1 | 2e-05 | FAIL |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.98 | 0.96 | 1 | 0 | 0.5 |  |
| many_random | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| many_random | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |
| many_similar | 16384 | 50 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| many_similar | 32768 | 50 | 0.98 | 0.86 | 6 | 0 | 0.0156 |  |
| multihop | 16384 | 50 | 1.00 | 0.96 | 2 | 0 | 0.25 |  |
| multihop | 32768 | 50 | 0.98 | 0.88 | 5 | 0 | 0.0312 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 1.00 | 0.98 | 1 | 0 | 0.5 |  |

FAIL: recall regression in all cases pooled

### suite-s2: budget -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.96 | 0.99 | 1 | 19 | 1 |  |
| heldout_many | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 50 | 0.96 | 0.98 | 0 | 1 | 1 |  |
| many_random | 16384 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| many_random | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |
| many_similar | 16384 | 50 | 0.96 | 0.96 | 1 | 1 | 0.75 |  |
| many_similar | 32768 | 50 | 0.86 | 0.98 | 0 | 6 | 1 |  |
| multihop | 16384 | 50 | 0.96 | 1.00 | 0 | 2 | 1 |  |
| multihop | 32768 | 50 | 0.88 | 0.98 | 0 | 5 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 32768 | 50 | 0.98 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### heldout: base -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.61 | 0.99 | 0 | 57 | 1 |  |
| heldout_many | 1024 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| heldout_many | 2048 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 4096 | 25 | 0.76 | 1.00 | 0 | 6 | 1 |  |
| heldout_many | 8192 | 25 | 0.64 | 0.96 | 0 | 8 | 1 |  |
| heldout_many | 16384 | 25 | 0.24 | 1.00 | 0 | 19 | 1 |  |
| heldout_many | 32768 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |

PASS: no recall regression

### heldout: synthetic -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

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

### heldout: realmix -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.99 | 0 | 1 | 1 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 0.96 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |

PASS: no recall regression

### heldout: budget -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.99 | 1 | 0 | 0.5 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 8192 | 25 | 0.96 | 0.96 | 0 | 0 | 1 |  |
| heldout_many | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 32768 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |

PASS: no recall regression

### multihop25: base -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.30 | 0.95 | 0 | 98 | 1 |  |
| multihop | 1024 | 25 | 0.52 | 1.00 | 0 | 12 | 1 |  |
| multihop | 2048 | 25 | 0.28 | 0.96 | 0 | 17 | 1 |  |
| multihop | 4096 | 25 | 0.40 | 1.00 | 0 | 15 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 0.96 | 0 | 17 | 1 |  |
| multihop | 16384 | 25 | 0.16 | 1.00 | 0 | 21 | 1 |  |
| multihop | 32768 | 25 | 0.16 | 0.80 | 0 | 16 | 1 |  |

PASS: no recall regression

### multihop25: synthetic -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 1.00 | 0.95 | 7 | 0 | 0.00781 | FAIL |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 32768 | 25 | 1.00 | 0.80 | 5 | 0 | 0.0312 |  |

FAIL: recall regression in all cases pooled

### multihop25: realmix -> budget (JunxiongWang_Llama3.1-Mamba2-8B-dpo)
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.99 | 0.95 | 6 | 0 | 0.0156 | FAIL |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 0.96 | 0.96 | 0 | 0 | 1 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| multihop | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 32768 | 25 | 1.00 | 0.80 | 5 | 0 | 0.0312 |  |

FAIL: recall regression in all cases pooled

### multihop25: budget -> realmix (JunxiongWang_Llama3.1-Mamba2-8B-dpo), FAIL cells are budget gains
baseline ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget',) vs candidate ('JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.95 | 0.99 | 0 | 6 | 1 |  |
| multihop | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 2048 | 25 | 0.96 | 0.96 | 0 | 0 | 1 |  |
| multihop | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 8192 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| multihop | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| multihop | 32768 | 25 | 0.80 | 1.00 | 0 | 5 | 1 |  |

PASS: no recall regression


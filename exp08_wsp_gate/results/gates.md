### suite-s1: base -> edited
baseline ('Qwen/Qwen3.5-0.8B',) vs candidate ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.75 | 0.73 | 23 | 12 | 0.0448 | FAIL |
| heldout_many | 16384 | 50 | 0.94 | 0.88 | 3 | 0 | 0.125 |  |
| heldout_many | 32768 | 50 | 0.84 | 0.84 | 2 | 2 | 0.688 |  |
| many_random | 16384 | 50 | 0.88 | 0.86 | 1 | 0 | 0.5 |  |
| many_random | 32768 | 50 | 0.82 | 0.84 | 1 | 2 | 0.875 |  |
| many_similar | 16384 | 50 | 0.64 | 0.60 | 4 | 2 | 0.344 |  |
| many_similar | 32768 | 50 | 0.62 | 0.58 | 5 | 3 | 0.363 |  |
| multihop | 16384 | 50 | 0.48 | 0.48 | 1 | 1 | 0.75 |  |
| multihop | 32768 | 50 | 0.22 | 0.16 | 3 | 0 | 0.125 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.82 | 0.84 | 0 | 1 | 1 |  |
| updated | 32768 | 50 | 0.74 | 0.70 | 3 | 1 | 0.312 |  |

FAIL: recall regression in all cases pooled

### suite-s2: base -> edited
baseline ('Qwen/Qwen3.5-0.8B',) vs candidate ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.73 | 0.71 | 21 | 12 | 0.0814 |  |
| heldout_many | 16384 | 50 | 0.92 | 0.88 | 3 | 1 | 0.312 |  |
| heldout_many | 32768 | 50 | 0.82 | 0.80 | 1 | 0 | 0.5 |  |
| many_random | 16384 | 50 | 0.90 | 0.90 | 1 | 1 | 0.75 |  |
| many_random | 32768 | 50 | 0.84 | 0.88 | 1 | 3 | 0.938 |  |
| many_similar | 16384 | 50 | 0.70 | 0.60 | 5 | 0 | 0.0312 |  |
| many_similar | 32768 | 50 | 0.50 | 0.46 | 3 | 1 | 0.312 |  |
| multihop | 16384 | 50 | 0.32 | 0.32 | 1 | 1 | 0.75 |  |
| multihop | 32768 | 50 | 0.32 | 0.32 | 2 | 2 | 0.688 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.68 | 0.68 | 3 | 3 | 0.656 |  |
| updated | 32768 | 50 | 0.74 | 0.72 | 1 | 0 | 0.5 |  |

PASS: no recall regression

### heldout: base -> edited
baseline ('Qwen/Qwen3.5-0.8B',) vs candidate ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.97 | 0.93 | 6 | 1 | 0.0625 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 4096 | 25 | 1.00 | 0.96 | 1 | 0 | 0.5 |  |
| heldout_many | 8192 | 25 | 0.96 | 0.88 | 2 | 0 | 0.25 |  |
| heldout_many | 16384 | 25 | 0.96 | 0.92 | 1 | 0 | 0.5 |  |
| heldout_many | 32768 | 25 | 0.88 | 0.88 | 1 | 1 | 0.75 |  |

PASS: no recall regression

### multihop25: base -> edited
baseline ('Qwen/Qwen3.5-0.8B',) vs candidate ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.45 | 0.41 | 10 | 4 | 0.0898 |  |
| multihop | 1024 | 25 | 0.56 | 0.48 | 2 | 0 | 0.25 |  |
| multihop | 2048 | 25 | 0.44 | 0.44 | 0 | 0 | 1 |  |
| multihop | 4096 | 25 | 0.56 | 0.44 | 3 | 0 | 0.125 |  |
| multihop | 8192 | 25 | 0.24 | 0.28 | 2 | 3 | 0.812 |  |
| multihop | 16384 | 25 | 0.36 | 0.36 | 0 | 0 | 1 |  |
| multihop | 32768 | 25 | 0.52 | 0.44 | 3 | 1 | 0.312 |  |

PASS: no recall regression

### step1: base -> edited
baseline ('Qwen/Qwen3.5-0.8B',) vs candidate ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',): 750 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 750 | 0.80 | 0.77 | 32 | 10 | 0.00047 | FAIL |
| many_random | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 2048 | 25 | 1.00 | 0.92 | 2 | 0 | 0.25 |  |
| many_random | 4096 | 25 | 0.92 | 0.88 | 1 | 0 | 0.5 |  |
| many_random | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 16384 | 25 | 0.92 | 0.92 | 0 | 0 | 1 |  |
| many_random | 32768 | 25 | 0.84 | 0.76 | 3 | 1 | 0.312 |  |
| many_similar | 1024 | 25 | 0.96 | 0.92 | 1 | 0 | 0.5 |  |
| many_similar | 2048 | 25 | 0.88 | 0.88 | 0 | 0 | 1 |  |
| many_similar | 4096 | 25 | 0.76 | 0.80 | 0 | 1 | 1 |  |
| many_similar | 8192 | 25 | 0.68 | 0.64 | 1 | 0 | 0.5 |  |
| many_similar | 16384 | 25 | 0.84 | 0.76 | 2 | 0 | 0.25 |  |
| many_similar | 32768 | 25 | 0.72 | 0.64 | 2 | 0 | 0.25 |  |
| multihop | 1024 | 25 | 0.44 | 0.40 | 1 | 0 | 0.5 |  |
| multihop | 2048 | 25 | 0.40 | 0.44 | 0 | 1 | 1 |  |
| multihop | 4096 | 25 | 0.28 | 0.32 | 1 | 2 | 0.875 |  |
| multihop | 8192 | 25 | 0.36 | 0.24 | 4 | 1 | 0.188 |  |
| multihop | 16384 | 25 | 0.40 | 0.40 | 1 | 1 | 0.75 |  |
| multihop | 32768 | 25 | 0.36 | 0.36 | 1 | 1 | 0.75 |  |
| needle | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 1024 | 25 | 1.00 | 0.92 | 2 | 0 | 0.25 |  |
| updated | 2048 | 25 | 0.92 | 0.80 | 3 | 0 | 0.125 |  |
| updated | 4096 | 25 | 0.84 | 0.72 | 3 | 0 | 0.125 |  |
| updated | 8192 | 25 | 0.88 | 0.80 | 2 | 0 | 0.25 |  |
| updated | 16384 | 25 | 0.84 | 0.84 | 0 | 0 | 1 |  |
| updated | 32768 | 25 | 0.68 | 0.68 | 2 | 2 | 0.688 |  |

FAIL: recall regression in all cases pooled

### real QA: base -> edited
baseline ('Qwen/Qwen3.5-0.8B',) vs candidate ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.56 | 0.55 | 30 | 20 | 0.101 |  |
| ruler_qa_1 | 4096 | 100 | 0.71 | 0.71 | 3 | 3 | 0.656 |  |
| ruler_qa_1 | 16384 | 100 | 0.61 | 0.58 | 5 | 2 | 0.227 |  |
| ruler_qa_1 | 32768 | 100 | 0.62 | 0.62 | 6 | 6 | 0.613 |  |
| ruler_qa_2 | 4096 | 100 | 0.54 | 0.49 | 6 | 1 | 0.0625 |  |
| ruler_qa_2 | 16384 | 100 | 0.44 | 0.44 | 5 | 5 | 0.623 |  |
| ruler_qa_2 | 32768 | 100 | 0.46 | 0.44 | 5 | 3 | 0.363 |  |

PASS: no recall regression

### suite-s1: edited -> base, FAIL cells are edited gains
baseline ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',) vs candidate ('Qwen/Qwen3.5-0.8B',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.73 | 0.75 | 12 | 23 | 0.98 |  |
| heldout_many | 16384 | 50 | 0.88 | 0.94 | 0 | 3 | 1 |  |
| heldout_many | 32768 | 50 | 0.84 | 0.84 | 2 | 2 | 0.688 |  |
| many_random | 16384 | 50 | 0.86 | 0.88 | 0 | 1 | 1 |  |
| many_random | 32768 | 50 | 0.84 | 0.82 | 2 | 1 | 0.5 |  |
| many_similar | 16384 | 50 | 0.60 | 0.64 | 2 | 4 | 0.891 |  |
| many_similar | 32768 | 50 | 0.58 | 0.62 | 3 | 5 | 0.855 |  |
| multihop | 16384 | 50 | 0.48 | 0.48 | 1 | 1 | 0.75 |  |
| multihop | 32768 | 50 | 0.16 | 0.22 | 0 | 3 | 1 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.84 | 0.82 | 1 | 0 | 0.5 |  |
| updated | 32768 | 50 | 0.70 | 0.74 | 1 | 3 | 0.938 |  |

PASS: no recall regression

### suite-s2: edited -> base, FAIL cells are edited gains
baseline ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',) vs candidate ('Qwen/Qwen3.5-0.8B',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.71 | 0.73 | 12 | 21 | 0.96 |  |
| heldout_many | 16384 | 50 | 0.88 | 0.92 | 1 | 3 | 0.938 |  |
| heldout_many | 32768 | 50 | 0.80 | 0.82 | 0 | 1 | 1 |  |
| many_random | 16384 | 50 | 0.90 | 0.90 | 1 | 1 | 0.75 |  |
| many_random | 32768 | 50 | 0.88 | 0.84 | 3 | 1 | 0.312 |  |
| many_similar | 16384 | 50 | 0.60 | 0.70 | 0 | 5 | 1 |  |
| many_similar | 32768 | 50 | 0.46 | 0.50 | 1 | 3 | 0.938 |  |
| multihop | 16384 | 50 | 0.32 | 0.32 | 1 | 1 | 0.75 |  |
| multihop | 32768 | 50 | 0.32 | 0.32 | 2 | 2 | 0.688 |  |
| needle | 16384 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 50 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 16384 | 50 | 0.68 | 0.68 | 3 | 3 | 0.656 |  |
| updated | 32768 | 50 | 0.72 | 0.74 | 0 | 1 | 1 |  |

PASS: no recall regression

### heldout: edited -> base, FAIL cells are edited gains
baseline ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',) vs candidate ('Qwen/Qwen3.5-0.8B',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.93 | 0.97 | 1 | 6 | 0.992 |  |
| heldout_many | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| heldout_many | 2048 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 4096 | 25 | 0.96 | 1.00 | 0 | 1 | 1 |  |
| heldout_many | 8192 | 25 | 0.88 | 0.96 | 0 | 2 | 1 |  |
| heldout_many | 16384 | 25 | 0.92 | 0.96 | 0 | 1 | 1 |  |
| heldout_many | 32768 | 25 | 0.88 | 0.88 | 1 | 1 | 0.75 |  |

PASS: no recall regression

### multihop25: edited -> base, FAIL cells are edited gains
baseline ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',) vs candidate ('Qwen/Qwen3.5-0.8B',): 150 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 150 | 0.41 | 0.45 | 4 | 10 | 0.971 |  |
| multihop | 1024 | 25 | 0.48 | 0.56 | 0 | 2 | 1 |  |
| multihop | 2048 | 25 | 0.44 | 0.44 | 0 | 0 | 1 |  |
| multihop | 4096 | 25 | 0.44 | 0.56 | 0 | 3 | 1 |  |
| multihop | 8192 | 25 | 0.28 | 0.24 | 3 | 2 | 0.5 |  |
| multihop | 16384 | 25 | 0.36 | 0.36 | 0 | 0 | 1 |  |
| multihop | 32768 | 25 | 0.44 | 0.52 | 1 | 3 | 0.938 |  |

PASS: no recall regression

### step1: edited -> base, FAIL cells are edited gains
baseline ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',) vs candidate ('Qwen/Qwen3.5-0.8B',): 750 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 750 | 0.77 | 0.80 | 10 | 32 | 1 |  |
| many_random | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 2048 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| many_random | 4096 | 25 | 0.88 | 0.92 | 0 | 1 | 1 |  |
| many_random | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| many_random | 16384 | 25 | 0.92 | 0.92 | 0 | 0 | 1 |  |
| many_random | 32768 | 25 | 0.76 | 0.84 | 1 | 3 | 0.938 |  |
| many_similar | 1024 | 25 | 0.92 | 0.96 | 0 | 1 | 1 |  |
| many_similar | 2048 | 25 | 0.88 | 0.88 | 0 | 0 | 1 |  |
| many_similar | 4096 | 25 | 0.80 | 0.76 | 1 | 0 | 0.5 |  |
| many_similar | 8192 | 25 | 0.64 | 0.68 | 0 | 1 | 1 |  |
| many_similar | 16384 | 25 | 0.76 | 0.84 | 0 | 2 | 1 |  |
| many_similar | 32768 | 25 | 0.64 | 0.72 | 0 | 2 | 1 |  |
| multihop | 1024 | 25 | 0.40 | 0.44 | 0 | 1 | 1 |  |
| multihop | 2048 | 25 | 0.44 | 0.40 | 1 | 0 | 0.5 |  |
| multihop | 4096 | 25 | 0.32 | 0.28 | 2 | 1 | 0.5 |  |
| multihop | 8192 | 25 | 0.24 | 0.36 | 1 | 4 | 0.969 |  |
| multihop | 16384 | 25 | 0.40 | 0.40 | 1 | 1 | 0.75 |  |
| multihop | 32768 | 25 | 0.36 | 0.36 | 1 | 1 | 0.75 |  |
| needle | 1024 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 2048 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 4096 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 8192 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 16384 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| needle | 32768 | 25 | 1.00 | 1.00 | 0 | 0 | 1 |  |
| updated | 1024 | 25 | 0.92 | 1.00 | 0 | 2 | 1 |  |
| updated | 2048 | 25 | 0.80 | 0.92 | 0 | 3 | 1 |  |
| updated | 4096 | 25 | 0.72 | 0.84 | 0 | 3 | 1 |  |
| updated | 8192 | 25 | 0.80 | 0.88 | 0 | 2 | 1 |  |
| updated | 16384 | 25 | 0.84 | 0.84 | 0 | 0 | 1 |  |
| updated | 32768 | 25 | 0.68 | 0.68 | 2 | 2 | 0.688 |  |

PASS: no recall regression

### real QA: edited -> base, FAIL cells are edited gains
baseline ('RikiyaT/Qwen3.5-0.8B-weight-space-programming',) vs candidate ('Qwen/Qwen3.5-0.8B',): 600 shared cases, alpha 0.05

| task | ref tokens | n | baseline | candidate | lost | gained | p | |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all |  | 600 | 0.55 | 0.56 | 20 | 30 | 0.941 |  |
| ruler_qa_1 | 4096 | 100 | 0.71 | 0.71 | 3 | 3 | 0.656 |  |
| ruler_qa_1 | 16384 | 100 | 0.58 | 0.61 | 2 | 5 | 0.938 |  |
| ruler_qa_1 | 32768 | 100 | 0.62 | 0.62 | 6 | 6 | 0.613 |  |
| ruler_qa_2 | 4096 | 100 | 0.49 | 0.54 | 1 | 6 | 0.992 |  |
| ruler_qa_2 | 16384 | 100 | 0.44 | 0.44 | 5 | 5 | 0.623 |  |
| ruler_qa_2 | 32768 | 100 | 0.44 | 0.46 | 3 | 5 | 0.855 |  |

PASS: no recall regression


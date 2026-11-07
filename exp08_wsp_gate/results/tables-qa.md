## Recall (contains) by reference length

| model | task | 4096 | 16384 | 32768 |
|---|---|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | ruler_qa_1 | 0.71 | 0.61 | 0.62 |
| Qwen/Qwen3.5-0.8B | ruler_qa_2 | 0.54 | 0.44 | 0.46 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_1 | 0.71 | 0.58 | 0.62 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_2 | 0.49 | 0.44 | 0.44 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | ruler_qa_1 | 4096 | 100 | 0.71 | 0.00 | 0.00 | 0.4 |
| Qwen/Qwen3.5-0.8B | ruler_qa_1 | 16384 | 100 | 0.61 | 0.00 | 0.00 | 0.9 |
| Qwen/Qwen3.5-0.8B | ruler_qa_1 | 32768 | 100 | 0.62 | 0.00 | 0.00 | 1.7 |
| Qwen/Qwen3.5-0.8B | ruler_qa_2 | 4096 | 100 | 0.54 | 0.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-0.8B | ruler_qa_2 | 16384 | 100 | 0.44 | 0.00 | 0.00 | 1.1 |
| Qwen/Qwen3.5-0.8B | ruler_qa_2 | 32768 | 100 | 0.46 | 0.00 | 0.00 | 2.1 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_1 | 4096 | 100 | 0.71 | 0.00 | 0.00 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_1 | 16384 | 100 | 0.58 | 0.00 | 0.00 | 0.9 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_1 | 32768 | 100 | 0.62 | 0.00 | 0.00 | 1.7 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_2 | 4096 | 100 | 0.49 | 0.00 | 0.00 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_2 | 16384 | 100 | 0.44 | 0.00 | 0.00 | 1.1 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_qa_2 | 32768 | 100 | 0.44 | 0.00 | 0.00 | 1.9 |

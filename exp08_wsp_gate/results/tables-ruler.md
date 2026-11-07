## Recall (contains) by reference length

| model | task | 16384 | 32768 |
|---|---|---:|---:|
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_1 | 1.00 | 1.00 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_2 | 1.00 | 0.94 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_3 | 0.20 | 0.36 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multiquery | 0.00 | 0.00 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multivalue | 0.40 | 0.36 |
| Qwen/Qwen3.5-0.8B | ruler_niah_single_1 | 1.00 | 1.00 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_1 | 0.98 | 1.00 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_2 | 0.96 | 0.94 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_3 | 0.28 | 0.40 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multiquery | 0.00 | 0.00 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multivalue | 0.18 | 0.16 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_single_1 | 0.00 | 0.00 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_1 | 16384 | 50 | 1.00 | 0.00 | 0.00 | 1.0 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_1 | 32768 | 50 | 1.00 | 0.00 | 0.00 | 1.9 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_2 | 16384 | 50 | 1.00 | 0.00 | 0.00 | 1.2 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_2 | 32768 | 50 | 0.94 | 0.00 | 0.00 | 2.0 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_3 | 16384 | 50 | 0.20 | 0.00 | 0.00 | 2.8 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multikey_3 | 32768 | 50 | 0.36 | 0.00 | 0.00 | 3.5 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multiquery | 16384 | 50 | 0.00 | 0.00 | 0.00 | 2.7 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multiquery | 32768 | 50 | 0.00 | 0.00 | 0.00 | 3.4 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multivalue | 16384 | 50 | 0.40 | 0.00 | 0.00 | 2.6 |
| Qwen/Qwen3.5-0.8B | ruler_niah_multivalue | 32768 | 50 | 0.36 | 0.00 | 0.00 | 3.4 |
| Qwen/Qwen3.5-0.8B | ruler_niah_single_1 | 16384 | 50 | 1.00 | 0.00 | 0.00 | 1.4 |
| Qwen/Qwen3.5-0.8B | ruler_niah_single_1 | 32768 | 50 | 1.00 | 0.00 | 0.00 | 2.2 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_1 | 16384 | 50 | 0.98 | 0.00 | 0.00 | 1.0 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_1 | 32768 | 50 | 1.00 | 0.00 | 0.00 | 1.9 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_2 | 16384 | 50 | 0.96 | 0.00 | 0.00 | 1.2 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_2 | 32768 | 50 | 0.94 | 0.00 | 0.00 | 2.0 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_3 | 16384 | 50 | 0.28 | 0.00 | 0.00 | 2.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multikey_3 | 32768 | 50 | 0.40 | 0.00 | 0.00 | 3.1 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multiquery | 16384 | 50 | 0.00 | 0.00 | 0.00 | 2.7 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multiquery | 32768 | 50 | 0.00 | 0.00 | 0.00 | 3.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multivalue | 16384 | 50 | 0.18 | 0.00 | 0.00 | 2.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_multivalue | 32768 | 50 | 0.16 | 0.00 | 0.00 | 3.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_single_1 | 16384 | 50 | 0.00 | 0.00 | 0.00 | 2.7 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | ruler_niah_single_1 | 32768 | 50 | 0.00 | 0.00 | 0.00 | 3.5 |

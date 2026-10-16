## Recall (contains) by reference length

| model | task | 16384 | 32768 |
|---|---|---:|---:|
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_1 | 0.98 | 0.94 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_2 | 0.86 | 0.72 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_3 | 0.40 | 0.40 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multiquery | 0.64 | 0.48 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multivalue | 0.74 | 0.46 |
| Qwen/Qwen2.5-1.5B | ruler_niah_single_1 | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_1 | 0.72 | 0.56 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_2 | 0.60 | 0.26 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_3 | 0.64 | 0.16 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multiquery | 0.08 | 0.00 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multivalue | 0.24 | 0.02 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_single_1 | 1.00 | 1.00 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_1 | 16384 | 50 | 0.98 | 0.00 | 0.00 | 0.7 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_1 | 32768 | 50 | 0.94 | 0.00 | 0.00 | 1.3 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_2 | 16384 | 50 | 0.86 | 0.00 | 0.00 | 0.6 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_2 | 32768 | 50 | 0.72 | 0.00 | 0.00 | 1.2 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_3 | 16384 | 50 | 0.40 | 0.00 | 0.00 | 1.2 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multikey_3 | 32768 | 50 | 0.40 | 0.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multiquery | 16384 | 50 | 0.64 | 0.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multiquery | 32768 | 50 | 0.48 | 0.00 | 0.00 | 2.5 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multivalue | 16384 | 50 | 0.74 | 0.00 | 0.00 | 1.7 |
| Qwen/Qwen2.5-1.5B | ruler_niah_multivalue | 32768 | 50 | 0.46 | 0.00 | 0.00 | 2.4 |
| Qwen/Qwen2.5-1.5B | ruler_niah_single_1 | 16384 | 50 | 1.00 | 0.00 | 0.00 | 0.6 |
| Qwen/Qwen2.5-1.5B | ruler_niah_single_1 | 32768 | 50 | 1.00 | 0.00 | 0.00 | 1.2 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_1 | 16384 | 50 | 0.72 | 0.00 | 0.00 | 2.3 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_1 | 32768 | 50 | 0.56 | 0.00 | 0.00 | 3.5 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_2 | 16384 | 50 | 0.60 | 0.00 | 0.00 | 0.9 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_2 | 32768 | 50 | 0.26 | 0.00 | 0.00 | 1.6 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_3 | 16384 | 50 | 0.64 | 0.00 | 0.00 | 2.3 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multikey_3 | 32768 | 50 | 0.16 | 0.00 | 0.00 | 3.0 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multiquery | 16384 | 50 | 0.08 | 0.00 | 0.00 | 2.9 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multiquery | 32768 | 50 | 0.00 | 0.00 | 0.00 | 3.6 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multivalue | 16384 | 50 | 0.24 | 0.00 | 0.00 | 3.0 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multivalue | 32768 | 50 | 0.02 | 0.00 | 0.00 | 3.5 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_single_1 | 16384 | 50 | 1.00 | 0.00 | 0.00 | 0.9 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_single_1 | 32768 | 50 | 1.00 | 0.00 | 0.00 | 1.7 |

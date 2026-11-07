## Recall (contains) by reference length

| model | task | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | many_random | 1.00 | 1.00 | 0.92 | 1.00 | 0.92 | 0.84 |
| Qwen/Qwen3.5-0.8B | many_similar | 0.96 | 0.88 | 0.76 | 0.68 | 0.84 | 0.72 |
| Qwen/Qwen3.5-0.8B | multihop | 0.44 | 0.40 | 0.28 | 0.36 | 0.40 | 0.36 |
| Qwen/Qwen3.5-0.8B | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen3.5-0.8B | updated | 1.00 | 0.92 | 0.84 | 0.88 | 0.84 | 0.68 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 1.00 | 0.92 | 0.88 | 1.00 | 0.92 | 0.76 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 0.92 | 0.88 | 0.80 | 0.64 | 0.76 | 0.64 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 0.40 | 0.44 | 0.32 | 0.24 | 0.40 | 0.36 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 0.92 | 0.80 | 0.72 | 0.80 | 0.84 | 0.68 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | many_random | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-0.8B | many_random | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-0.8B | many_random | 4096 | 25 | 0.92 | 0.92 | 0.08 | 0.4 |
| Qwen/Qwen3.5-0.8B | many_random | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-0.8B | many_random | 16384 | 25 | 0.92 | 0.92 | 0.08 | 0.8 |
| Qwen/Qwen3.5-0.8B | many_random | 32768 | 25 | 0.84 | 0.84 | 0.12 | 1.6 |
| Qwen/Qwen3.5-0.8B | many_similar | 1024 | 25 | 0.96 | 0.96 | 0.04 | 0.3 |
| Qwen/Qwen3.5-0.8B | many_similar | 2048 | 25 | 0.88 | 0.88 | 0.12 | 0.3 |
| Qwen/Qwen3.5-0.8B | many_similar | 4096 | 25 | 0.76 | 0.76 | 0.24 | 0.4 |
| Qwen/Qwen3.5-0.8B | many_similar | 8192 | 25 | 0.68 | 0.68 | 0.32 | 0.5 |
| Qwen/Qwen3.5-0.8B | many_similar | 16384 | 25 | 0.84 | 0.84 | 0.12 | 0.8 |
| Qwen/Qwen3.5-0.8B | many_similar | 32768 | 25 | 0.72 | 0.72 | 0.28 | 1.6 |
| Qwen/Qwen3.5-0.8B | multihop | 1024 | 25 | 0.44 | 0.44 | 0.56 | 0.3 |
| Qwen/Qwen3.5-0.8B | multihop | 2048 | 25 | 0.40 | 0.40 | 0.60 | 0.3 |
| Qwen/Qwen3.5-0.8B | multihop | 4096 | 25 | 0.28 | 0.28 | 0.72 | 0.4 |
| Qwen/Qwen3.5-0.8B | multihop | 8192 | 25 | 0.36 | 0.36 | 0.64 | 0.5 |
| Qwen/Qwen3.5-0.8B | multihop | 16384 | 25 | 0.40 | 0.40 | 0.60 | 0.8 |
| Qwen/Qwen3.5-0.8B | multihop | 32768 | 25 | 0.36 | 0.36 | 0.60 | 1.6 |
| Qwen/Qwen3.5-0.8B | needle | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-0.8B | needle | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-0.8B | needle | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen3.5-0.8B | needle | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-0.8B | needle | 16384 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen3.5-0.8B | needle | 32768 | 25 | 1.00 | 1.00 | 0.00 | 1.6 |
| Qwen/Qwen3.5-0.8B | updated | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-0.8B | updated | 2048 | 25 | 0.92 | 0.92 | 0.08 | 0.3 |
| Qwen/Qwen3.5-0.8B | updated | 4096 | 25 | 0.84 | 0.84 | 0.16 | 0.4 |
| Qwen/Qwen3.5-0.8B | updated | 8192 | 25 | 0.88 | 0.88 | 0.08 | 0.5 |
| Qwen/Qwen3.5-0.8B | updated | 16384 | 25 | 0.84 | 0.84 | 0.12 | 0.8 |
| Qwen/Qwen3.5-0.8B | updated | 32768 | 25 | 0.68 | 0.68 | 0.12 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 2048 | 25 | 0.92 | 0.92 | 0.08 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 4096 | 25 | 0.88 | 0.88 | 0.12 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 16384 | 25 | 0.92 | 0.92 | 0.08 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 32768 | 25 | 0.76 | 0.76 | 0.20 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 1024 | 25 | 0.92 | 0.92 | 0.08 | 0.2 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 2048 | 25 | 0.88 | 0.88 | 0.12 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 4096 | 25 | 0.80 | 0.80 | 0.16 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 8192 | 25 | 0.64 | 0.64 | 0.36 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 16384 | 25 | 0.76 | 0.76 | 0.20 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 32768 | 25 | 0.64 | 0.64 | 0.36 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 1024 | 25 | 0.40 | 0.40 | 0.60 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 2048 | 25 | 0.44 | 0.44 | 0.52 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 4096 | 25 | 0.32 | 0.32 | 0.68 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 8192 | 25 | 0.24 | 0.24 | 0.76 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 16384 | 25 | 0.40 | 0.40 | 0.60 | 0.9 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 32768 | 25 | 0.36 | 0.36 | 0.64 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 16384 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 32768 | 25 | 1.00 | 1.00 | 0.00 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 1024 | 25 | 0.92 | 0.92 | 0.08 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 2048 | 25 | 0.80 | 0.80 | 0.20 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 4096 | 25 | 0.72 | 0.72 | 0.24 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 8192 | 25 | 0.80 | 0.80 | 0.12 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 16384 | 25 | 0.84 | 0.84 | 0.16 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 32768 | 25 | 0.68 | 0.68 | 0.16 | 1.6 |

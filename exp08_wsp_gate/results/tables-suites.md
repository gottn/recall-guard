## Recall (contains) by reference length

| model | task | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | heldout_many | 1.00 | 1.00 | 1.00 | 0.96 | 0.94 | 0.84 |
| Qwen/Qwen3.5-0.8B | many_random |  |  |  |  | 0.89 | 0.83 |
| Qwen/Qwen3.5-0.8B | many_similar |  |  |  |  | 0.67 | 0.56 |
| Qwen/Qwen3.5-0.8B | multihop |  |  |  |  | 0.40 | 0.27 |
| Qwen/Qwen3.5-0.8B | needle |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen3.5-0.8B | updated |  |  |  |  | 0.75 | 0.74 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 1.00 | 0.96 | 0.96 | 0.88 | 0.89 | 0.83 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random |  |  |  |  | 0.88 | 0.86 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar |  |  |  |  | 0.60 | 0.52 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop |  |  |  |  | 0.40 | 0.24 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle |  |  |  |  | 1.00 | 1.00 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated |  |  |  |  | 0.76 | 0.71 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen3.5-0.8B | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-0.8B | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.0 |
| Qwen/Qwen3.5-0.8B | heldout_many | 8192 | 25 | 0.96 | 0.96 | 0.04 | 1.1 |
| Qwen/Qwen3.5-0.8B | heldout_many | 16384 | 125 | 0.94 | 0.94 | 0.06 | 1.4 |
| Qwen/Qwen3.5-0.8B | heldout_many | 32768 | 125 | 0.84 | 0.84 | 0.14 | 1.6 |
| Qwen/Qwen3.5-0.8B | many_random | 16384 | 100 | 0.89 | 0.89 | 0.08 | 0.8 |
| Qwen/Qwen3.5-0.8B | many_random | 32768 | 100 | 0.83 | 0.83 | 0.17 | 1.8 |
| Qwen/Qwen3.5-0.8B | many_similar | 16384 | 100 | 0.67 | 0.67 | 0.33 | 0.8 |
| Qwen/Qwen3.5-0.8B | many_similar | 32768 | 100 | 0.56 | 0.56 | 0.43 | 1.6 |
| Qwen/Qwen3.5-0.8B | multihop | 16384 | 100 | 0.40 | 0.40 | 0.60 | 0.8 |
| Qwen/Qwen3.5-0.8B | multihop | 32768 | 100 | 0.27 | 0.27 | 0.72 | 1.6 |
| Qwen/Qwen3.5-0.8B | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen3.5-0.8B | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.6 |
| Qwen/Qwen3.5-0.8B | updated | 16384 | 100 | 0.75 | 0.75 | 0.20 | 0.8 |
| Qwen/Qwen3.5-0.8B | updated | 32768 | 100 | 0.74 | 0.74 | 0.17 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 2048 | 25 | 0.96 | 0.96 | 0.04 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 4096 | 25 | 0.96 | 0.96 | 0.04 | 0.4 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 8192 | 25 | 0.88 | 0.88 | 0.12 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 16384 | 125 | 0.89 | 0.89 | 0.09 | 0.9 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | heldout_many | 32768 | 125 | 0.83 | 0.83 | 0.14 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 16384 | 100 | 0.88 | 0.88 | 0.11 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_random | 32768 | 100 | 0.86 | 0.86 | 0.13 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 16384 | 100 | 0.60 | 0.60 | 0.39 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | many_similar | 32768 | 100 | 0.52 | 0.52 | 0.47 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 16384 | 100 | 0.40 | 0.40 | 0.60 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 32768 | 100 | 0.24 | 0.24 | 0.75 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 16384 | 100 | 0.76 | 0.76 | 0.20 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | updated | 32768 | 100 | 0.71 | 0.71 | 0.21 | 1.6 |

## Recall (contains) by reference length

| model | task | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | multihop | 0.56 | 0.44 | 0.56 | 0.24 | 0.36 | 0.52 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 0.48 | 0.44 | 0.44 | 0.28 | 0.36 | 0.44 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen3.5-0.8B | multihop | 1024 | 25 | 0.56 | 0.56 | 0.44 | 0.3 |
| Qwen/Qwen3.5-0.8B | multihop | 2048 | 25 | 0.44 | 0.44 | 0.56 | 0.3 |
| Qwen/Qwen3.5-0.8B | multihop | 4096 | 25 | 0.56 | 0.56 | 0.44 | 0.3 |
| Qwen/Qwen3.5-0.8B | multihop | 8192 | 25 | 0.24 | 0.24 | 0.76 | 0.5 |
| Qwen/Qwen3.5-0.8B | multihop | 16384 | 25 | 0.36 | 0.36 | 0.64 | 0.8 |
| Qwen/Qwen3.5-0.8B | multihop | 32768 | 25 | 0.52 | 0.52 | 0.48 | 1.6 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 1024 | 25 | 0.48 | 0.48 | 0.52 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 2048 | 25 | 0.44 | 0.44 | 0.56 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 4096 | 25 | 0.44 | 0.44 | 0.56 | 0.3 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 8192 | 25 | 0.28 | 0.28 | 0.72 | 0.5 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 16384 | 25 | 0.36 | 0.36 | 0.64 | 0.8 |
| RikiyaT/Qwen3.5-0.8B-weight-space-programming | multihop | 32768 | 25 | 0.44 | 0.44 | 0.56 | 1.6 |

## Recall (contains) by reference length

| model | task | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen2.5-1.5B | many_random | 0.96 | 0.92 | 0.88 | 0.92 | 0.96 | 0.72 |
| Qwen/Qwen2.5-1.5B | many_similar | 0.96 | 0.88 | 0.92 | 0.96 | 0.76 | 0.68 |
| Qwen/Qwen2.5-1.5B | multihop | 0.28 | 0.16 | 0.08 | 0.08 | 0.20 | 0.16 |
| Qwen/Qwen2.5-1.5B | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B | updated | 0.64 | 0.48 | 0.56 | 0.32 | 0.36 | 0.44 |
| Qwen/Qwen3-4B | many_random | 0.96 | 1.00 | 1.00 | 1.00 | 1.00 | 0.84 |
| Qwen/Qwen3-4B | many_similar | 1.00 | 0.96 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen3-4B | multihop | 0.80 | 0.64 | 0.52 | 0.68 | 0.68 | 0.44 |
| Qwen/Qwen3-4B | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen3-4B | updated | 0.96 | 0.68 | 0.56 | 0.72 | 0.64 | 0.92 |
| Qwen/Qwen3.5-4B | many_random | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen3.5-4B | many_similar | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen3.5-4B | multihop | 0.76 | 0.52 | 0.36 | 0.44 | 0.40 | 0.36 |
| Qwen/Qwen3.5-4B | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen3.5-4B | updated | 1.00 | 1.00 | 0.92 | 0.88 | 0.88 | 0.76 |
| jet-ai/Jet-Nemotron-2B | many_random | 1.00 | 0.92 | 0.88 | 0.80 | 0.72 | 0.16 |
| jet-ai/Jet-Nemotron-2B | many_similar | 1.00 | 1.00 | 0.92 | 0.76 | 0.76 | 0.20 |
| jet-ai/Jet-Nemotron-2B | multihop | 0.20 | 0.08 | 0.12 | 0.20 | 0.24 | 0.20 |
| jet-ai/Jet-Nemotron-2B | needle | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B | updated | 0.92 | 0.56 | 0.68 | 0.84 | 0.84 | 0.60 |

## Verdict rule: first length where a stressor separates the pair and the needle does not

| hybrid | full | task | first length with gap | full - hybrid | needle gap |
|---|---|---|---:|---:|---:|
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 8192 | +0.24 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 16384 | +0.24 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 32768 | +0.48 | +0.00 |

## Hybrid minus full attention

| hybrid | full | task | ref tokens | hybrid | full | gap |
|---|---|---|---:|---:|---:|---:|
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_random | 1024 | 1.00 | 0.96 | +0.04 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_random | 2048 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_random | 4096 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_random | 8192 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_random | 16384 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_random | 32768 | 1.00 | 0.84 | +0.16 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_similar | 1024 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_similar | 2048 | 1.00 | 0.96 | +0.04 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_similar | 4096 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_similar | 8192 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_similar | 16384 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | many_similar | 32768 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 1024 | 0.76 | 0.80 | -0.04 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 2048 | 0.52 | 0.64 | -0.12 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 4096 | 0.36 | 0.52 | -0.16 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 8192 | 0.44 | 0.68 | -0.24 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 16384 | 0.40 | 0.68 | -0.28 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | multihop | 32768 | 0.36 | 0.44 | -0.08 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | needle | 1024 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | needle | 2048 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | needle | 4096 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | needle | 8192 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | needle | 16384 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | needle | 32768 | 1.00 | 1.00 | +0.00 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | updated | 1024 | 1.00 | 0.96 | +0.04 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | updated | 2048 | 1.00 | 0.68 | +0.32 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | updated | 4096 | 0.92 | 0.56 | +0.36 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | updated | 8192 | 0.88 | 0.72 | +0.16 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | updated | 16384 | 0.88 | 0.64 | +0.24 |
| Qwen/Qwen3.5-4B | Qwen/Qwen3-4B | updated | 32768 | 0.76 | 0.92 | -0.16 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 1024 | 1.00 | 0.96 | +0.04 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 2048 | 0.92 | 0.92 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 4096 | 0.88 | 0.88 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 8192 | 0.80 | 0.92 | -0.12 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 16384 | 0.72 | 0.96 | -0.24 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_random | 32768 | 0.16 | 0.72 | -0.56 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 1024 | 1.00 | 0.96 | +0.04 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 2048 | 1.00 | 0.88 | +0.12 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 4096 | 0.92 | 0.92 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 8192 | 0.76 | 0.96 | -0.20 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 16384 | 0.76 | 0.76 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | many_similar | 32768 | 0.20 | 0.68 | -0.48 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | multihop | 1024 | 0.20 | 0.28 | -0.08 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | multihop | 2048 | 0.08 | 0.16 | -0.08 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | multihop | 4096 | 0.12 | 0.08 | +0.04 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | multihop | 8192 | 0.20 | 0.08 | +0.12 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | multihop | 16384 | 0.24 | 0.20 | +0.04 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | multihop | 32768 | 0.20 | 0.16 | +0.04 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | needle | 1024 | 1.00 | 1.00 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | needle | 2048 | 1.00 | 1.00 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | needle | 4096 | 1.00 | 1.00 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | needle | 8192 | 1.00 | 1.00 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | needle | 16384 | 1.00 | 1.00 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | needle | 32768 | 1.00 | 1.00 | +0.00 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | updated | 1024 | 0.92 | 0.64 | +0.28 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | updated | 2048 | 0.56 | 0.48 | +0.08 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | updated | 4096 | 0.68 | 0.56 | +0.12 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | updated | 8192 | 0.84 | 0.32 | +0.52 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | updated | 16384 | 0.84 | 0.36 | +0.48 |
| jet-ai/Jet-Nemotron-2B | Qwen/Qwen2.5-1.5B | updated | 32768 | 0.60 | 0.44 | +0.16 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen2.5-1.5B | many_random | 1024 | 25 | 0.96 | 0.96 | 0.04 | 0.2 |
| Qwen/Qwen2.5-1.5B | many_random | 2048 | 25 | 0.92 | 0.92 | 0.08 | 0.3 |
| Qwen/Qwen2.5-1.5B | many_random | 4096 | 25 | 0.88 | 0.88 | 0.12 | 0.4 |
| Qwen/Qwen2.5-1.5B | many_random | 8192 | 25 | 0.92 | 0.92 | 0.08 | 0.5 |
| Qwen/Qwen2.5-1.5B | many_random | 16384 | 25 | 0.96 | 0.96 | 0.04 | 1.0 |
| Qwen/Qwen2.5-1.5B | many_random | 32768 | 25 | 0.72 | 0.72 | 0.28 | 1.7 |
| Qwen/Qwen2.5-1.5B | many_similar | 1024 | 25 | 0.96 | 0.96 | 0.04 | 0.2 |
| Qwen/Qwen2.5-1.5B | many_similar | 2048 | 25 | 0.88 | 0.88 | 0.12 | 0.2 |
| Qwen/Qwen2.5-1.5B | many_similar | 4096 | 25 | 0.92 | 0.92 | 0.08 | 0.3 |
| Qwen/Qwen2.5-1.5B | many_similar | 8192 | 25 | 0.96 | 0.96 | 0.04 | 0.5 |
| Qwen/Qwen2.5-1.5B | many_similar | 16384 | 25 | 0.76 | 0.76 | 0.20 | 0.9 |
| Qwen/Qwen2.5-1.5B | many_similar | 32768 | 25 | 0.68 | 0.68 | 0.28 | 1.7 |
| Qwen/Qwen2.5-1.5B | multihop | 1024 | 25 | 0.28 | 0.28 | 0.68 | 0.3 |
| Qwen/Qwen2.5-1.5B | multihop | 2048 | 25 | 0.16 | 0.16 | 0.84 | 0.5 |
| Qwen/Qwen2.5-1.5B | multihop | 4096 | 25 | 0.08 | 0.08 | 0.88 | 0.6 |
| Qwen/Qwen2.5-1.5B | multihop | 8192 | 25 | 0.08 | 0.08 | 0.88 | 0.7 |
| Qwen/Qwen2.5-1.5B | multihop | 16384 | 25 | 0.20 | 0.20 | 0.68 | 1.1 |
| Qwen/Qwen2.5-1.5B | multihop | 32768 | 25 | 0.16 | 0.16 | 0.80 | 1.7 |
| Qwen/Qwen2.5-1.5B | needle | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.6 |
| Qwen/Qwen2.5-1.5B | needle | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen2.5-1.5B | needle | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen2.5-1.5B | needle | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen2.5-1.5B | needle | 16384 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B | needle | 32768 | 25 | 1.00 | 1.00 | 0.00 | 1.7 |
| Qwen/Qwen2.5-1.5B | updated | 1024 | 25 | 0.64 | 0.64 | 0.36 | 0.3 |
| Qwen/Qwen2.5-1.5B | updated | 2048 | 25 | 0.48 | 0.48 | 0.52 | 0.5 |
| Qwen/Qwen2.5-1.5B | updated | 4096 | 25 | 0.56 | 0.56 | 0.36 | 0.5 |
| Qwen/Qwen2.5-1.5B | updated | 8192 | 25 | 0.32 | 0.32 | 0.56 | 0.6 |
| Qwen/Qwen2.5-1.5B | updated | 16384 | 25 | 0.36 | 0.36 | 0.40 | 1.0 |
| Qwen/Qwen2.5-1.5B | updated | 32768 | 25 | 0.44 | 0.44 | 0.40 | 1.7 |
| Qwen/Qwen3-4B | many_random | 1024 | 25 | 0.96 | 0.96 | 0.04 | 0.3 |
| Qwen/Qwen3-4B | many_random | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen3-4B | many_random | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3-4B | many_random | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.7 |
| Qwen/Qwen3-4B | many_random | 16384 | 25 | 1.00 | 1.00 | 0.00 | 1.5 |
| Qwen/Qwen3-4B | many_random | 32768 | 25 | 0.84 | 0.84 | 0.16 | 3.6 |
| Qwen/Qwen3-4B | many_similar | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3-4B | many_similar | 2048 | 25 | 0.96 | 0.96 | 0.00 | 0.4 |
| Qwen/Qwen3-4B | many_similar | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3-4B | many_similar | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen3-4B | many_similar | 16384 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| Qwen/Qwen3-4B | many_similar | 32768 | 25 | 1.00 | 1.00 | 0.00 | 3.7 |
| Qwen/Qwen3-4B | multihop | 1024 | 25 | 0.80 | 0.80 | 0.20 | 0.3 |
| Qwen/Qwen3-4B | multihop | 2048 | 25 | 0.64 | 0.64 | 0.36 | 0.4 |
| Qwen/Qwen3-4B | multihop | 4096 | 25 | 0.52 | 0.52 | 0.48 | 0.5 |
| Qwen/Qwen3-4B | multihop | 8192 | 25 | 0.68 | 0.68 | 0.32 | 0.8 |
| Qwen/Qwen3-4B | multihop | 16384 | 25 | 0.68 | 0.68 | 0.32 | 1.5 |
| Qwen/Qwen3-4B | multihop | 32768 | 25 | 0.44 | 0.44 | 0.56 | 3.7 |
| Qwen/Qwen3-4B | needle | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3-4B | needle | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3-4B | needle | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3-4B | needle | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.7 |
| Qwen/Qwen3-4B | needle | 16384 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| Qwen/Qwen3-4B | needle | 32768 | 25 | 1.00 | 1.00 | 0.00 | 3.4 |
| Qwen/Qwen3-4B | updated | 1024 | 25 | 0.96 | 0.96 | 0.00 | 0.3 |
| Qwen/Qwen3-4B | updated | 2048 | 25 | 0.68 | 0.68 | 0.12 | 0.4 |
| Qwen/Qwen3-4B | updated | 4096 | 25 | 0.56 | 0.56 | 0.28 | 0.5 |
| Qwen/Qwen3-4B | updated | 8192 | 25 | 0.72 | 0.72 | 0.08 | 0.8 |
| Qwen/Qwen3-4B | updated | 16384 | 25 | 0.64 | 0.64 | 0.00 | 1.4 |
| Qwen/Qwen3-4B | updated | 32768 | 25 | 0.92 | 0.92 | 0.00 | 3.7 |
| Qwen/Qwen3.5-4B | many_random | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-4B | many_random | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen3.5-4B | many_random | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.7 |
| Qwen/Qwen3.5-4B | many_random | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen3.5-4B | many_random | 16384 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| Qwen/Qwen3.5-4B | many_random | 32768 | 25 | 1.00 | 1.00 | 0.00 | 2.5 |
| Qwen/Qwen3.5-4B | many_similar | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-4B | many_similar | 2048 | 25 | 1.00 | 1.00 | 0.00 | 1.7 |
| Qwen/Qwen3.5-4B | many_similar | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-4B | many_similar | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen3.5-4B | many_similar | 16384 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| Qwen/Qwen3.5-4B | many_similar | 32768 | 25 | 1.00 | 1.00 | 0.00 | 2.5 |
| Qwen/Qwen3.5-4B | multihop | 1024 | 25 | 0.76 | 0.76 | 0.24 | 0.3 |
| Qwen/Qwen3.5-4B | multihop | 2048 | 25 | 0.52 | 0.52 | 0.48 | 0.4 |
| Qwen/Qwen3.5-4B | multihop | 4096 | 25 | 0.36 | 0.36 | 0.56 | 0.8 |
| Qwen/Qwen3.5-4B | multihop | 8192 | 25 | 0.44 | 0.44 | 0.36 | 1.0 |
| Qwen/Qwen3.5-4B | multihop | 16384 | 25 | 0.40 | 0.40 | 0.32 | 2.8 |
| Qwen/Qwen3.5-4B | multihop | 32768 | 25 | 0.36 | 0.36 | 0.32 | 2.8 |
| Qwen/Qwen3.5-4B | needle | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-4B | needle | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen3.5-4B | needle | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| Qwen/Qwen3.5-4B | needle | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen3.5-4B | needle | 16384 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| Qwen/Qwen3.5-4B | needle | 32768 | 25 | 1.00 | 1.00 | 0.00 | 4.1 |
| Qwen/Qwen3.5-4B | updated | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen3.5-4B | updated | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| Qwen/Qwen3.5-4B | updated | 4096 | 25 | 0.92 | 0.92 | 0.08 | 0.5 |
| Qwen/Qwen3.5-4B | updated | 8192 | 25 | 0.88 | 0.88 | 0.12 | 2.4 |
| Qwen/Qwen3.5-4B | updated | 16384 | 25 | 0.88 | 0.88 | 0.12 | 1.3 |
| Qwen/Qwen3.5-4B | updated | 32768 | 25 | 0.76 | 0.76 | 0.24 | 2.5 |
| jet-ai/Jet-Nemotron-2B | many_random | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.6 |
| jet-ai/Jet-Nemotron-2B | many_random | 2048 | 25 | 0.92 | 0.92 | 0.08 | 0.5 |
| jet-ai/Jet-Nemotron-2B | many_random | 4096 | 25 | 0.88 | 0.88 | 0.12 | 0.5 |
| jet-ai/Jet-Nemotron-2B | many_random | 8192 | 25 | 0.80 | 0.80 | 0.20 | 0.5 |
| jet-ai/Jet-Nemotron-2B | many_random | 16384 | 25 | 0.72 | 0.72 | 0.20 | 0.9 |
| jet-ai/Jet-Nemotron-2B | many_random | 32768 | 25 | 0.16 | 0.16 | 0.68 | 2.3 |
| jet-ai/Jet-Nemotron-2B | many_similar | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.6 |
| jet-ai/Jet-Nemotron-2B | many_similar | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| jet-ai/Jet-Nemotron-2B | many_similar | 4096 | 25 | 0.92 | 0.92 | 0.08 | 0.4 |
| jet-ai/Jet-Nemotron-2B | many_similar | 8192 | 25 | 0.76 | 0.76 | 0.24 | 0.5 |
| jet-ai/Jet-Nemotron-2B | many_similar | 16384 | 25 | 0.76 | 0.76 | 0.24 | 0.8 |
| jet-ai/Jet-Nemotron-2B | many_similar | 32768 | 25 | 0.20 | 0.20 | 0.80 | 2.3 |
| jet-ai/Jet-Nemotron-2B | multihop | 1024 | 25 | 0.20 | 0.20 | 0.36 | 0.9 |
| jet-ai/Jet-Nemotron-2B | multihop | 2048 | 25 | 0.08 | 0.08 | 0.52 | 0.8 |
| jet-ai/Jet-Nemotron-2B | multihop | 4096 | 25 | 0.12 | 0.12 | 0.48 | 0.5 |
| jet-ai/Jet-Nemotron-2B | multihop | 8192 | 25 | 0.20 | 0.20 | 0.60 | 0.6 |
| jet-ai/Jet-Nemotron-2B | multihop | 16384 | 25 | 0.24 | 0.24 | 0.76 | 0.8 |
| jet-ai/Jet-Nemotron-2B | multihop | 32768 | 25 | 0.20 | 0.20 | 0.76 | 2.1 |
| jet-ai/Jet-Nemotron-2B | needle | 1024 | 25 | 1.00 | 1.00 | 0.00 | 11.8 |
| jet-ai/Jet-Nemotron-2B | needle | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| jet-ai/Jet-Nemotron-2B | needle | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| jet-ai/Jet-Nemotron-2B | needle | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.5 |
| jet-ai/Jet-Nemotron-2B | needle | 16384 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| jet-ai/Jet-Nemotron-2B | needle | 32768 | 25 | 1.00 | 1.00 | 0.00 | 1.6 |
| jet-ai/Jet-Nemotron-2B | updated | 1024 | 25 | 0.92 | 0.92 | 0.04 | 0.9 |
| jet-ai/Jet-Nemotron-2B | updated | 2048 | 25 | 0.56 | 0.56 | 0.28 | 0.7 |
| jet-ai/Jet-Nemotron-2B | updated | 4096 | 25 | 0.68 | 0.68 | 0.20 | 0.4 |
| jet-ai/Jet-Nemotron-2B | updated | 8192 | 25 | 0.84 | 0.84 | 0.04 | 0.6 |
| jet-ai/Jet-Nemotron-2B | updated | 16384 | 25 | 0.84 | 0.84 | 0.00 | 1.2 |
| jet-ai/Jet-Nemotron-2B | updated | 32768 | 25 | 0.60 | 0.60 | 0.00 | 2.5 |

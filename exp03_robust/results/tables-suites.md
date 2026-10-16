## Recall (contains) by reference length

| model | task | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen2.5-1.5B | heldout_many | 0.96 | 1.00 | 1.00 | 0.92 | 0.91 | 0.93 |
| Qwen/Qwen2.5-1.5B | many_random |  |  |  |  | 0.90 | 0.90 |
| Qwen/Qwen2.5-1.5B | many_similar |  |  |  |  | 0.88 | 0.75 |
| Qwen/Qwen2.5-1.5B | multihop | 0.12 | 0.24 | 0.16 | 0.20 | 0.22 | 0.14 |
| Qwen/Qwen2.5-1.5B | needle |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B | updated |  |  |  |  | 0.42 | 0.34 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 1.00 | 1.00 | 0.96 | 0.96 | 0.90 | 0.41 |
| jet-ai/Jet-Nemotron-2B | many_random |  |  |  |  | 0.57 | 0.31 |
| jet-ai/Jet-Nemotron-2B | many_similar |  |  |  |  | 0.70 | 0.22 |
| jet-ai/Jet-Nemotron-2B | multihop | 0.24 | 0.08 | 0.20 | 0.20 | 0.19 | 0.11 |
| jet-ai/Jet-Nemotron-2B | needle |  |  |  |  | 1.00 | 0.86 |
| jet-ai/Jet-Nemotron-2B | updated |  |  |  |  | 0.82 | 0.58 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_random |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_similar |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 1.00 | 0.96 | 0.96 | 0.92 | 0.98 | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | needle |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | updated |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.95 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random |  |  |  |  | 1.00 | 0.97 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar |  |  |  |  | 1.00 | 0.97 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 1.00 | 0.96 | 1.00 | 0.88 | 0.95 | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated |  |  |  |  | 1.00 | 1.00 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen/Qwen2.5-1.5B | heldout_many | 1024 | 25 | 0.96 | 0.96 | 0.04 | 0.2 |
| Qwen/Qwen2.5-1.5B | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.2 |
| Qwen/Qwen2.5-1.5B | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.3 |
| Qwen/Qwen2.5-1.5B | heldout_many | 8192 | 25 | 0.92 | 0.92 | 0.04 | 0.5 |
| Qwen/Qwen2.5-1.5B | heldout_many | 16384 | 125 | 0.91 | 0.91 | 0.06 | 1.1 |
| Qwen/Qwen2.5-1.5B | heldout_many | 32768 | 125 | 0.93 | 0.93 | 0.06 | 1.7 |
| Qwen/Qwen2.5-1.5B | many_random | 16384 | 100 | 0.90 | 0.90 | 0.10 | 1.0 |
| Qwen/Qwen2.5-1.5B | many_random | 32768 | 100 | 0.90 | 0.90 | 0.09 | 1.7 |
| Qwen/Qwen2.5-1.5B | many_similar | 16384 | 100 | 0.88 | 0.88 | 0.12 | 0.9 |
| Qwen/Qwen2.5-1.5B | many_similar | 32768 | 100 | 0.75 | 0.75 | 0.24 | 1.7 |
| Qwen/Qwen2.5-1.5B | multihop | 1024 | 25 | 0.12 | 0.12 | 0.84 | 0.4 |
| Qwen/Qwen2.5-1.5B | multihop | 2048 | 25 | 0.24 | 0.24 | 0.76 | 0.6 |
| Qwen/Qwen2.5-1.5B | multihop | 4096 | 25 | 0.16 | 0.16 | 0.84 | 0.6 |
| Qwen/Qwen2.5-1.5B | multihop | 8192 | 25 | 0.20 | 0.20 | 0.76 | 0.7 |
| Qwen/Qwen2.5-1.5B | multihop | 16384 | 125 | 0.22 | 0.22 | 0.72 | 1.1 |
| Qwen/Qwen2.5-1.5B | multihop | 32768 | 125 | 0.14 | 0.14 | 0.81 | 1.7 |
| Qwen/Qwen2.5-1.5B | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.7 |
| Qwen/Qwen2.5-1.5B | updated | 16384 | 100 | 0.42 | 0.42 | 0.47 | 1.1 |
| Qwen/Qwen2.5-1.5B | updated | 32768 | 100 | 0.34 | 0.34 | 0.45 | 1.7 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 4096 | 25 | 0.96 | 0.96 | 0.04 | 0.4 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 8192 | 25 | 0.96 | 0.96 | 0.04 | 0.6 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 16384 | 125 | 0.90 | 0.90 | 0.10 | 1.4 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 32768 | 125 | 0.41 | 0.41 | 0.54 | 2.2 |
| jet-ai/Jet-Nemotron-2B | many_random | 16384 | 100 | 0.57 | 0.57 | 0.39 | 1.4 |
| jet-ai/Jet-Nemotron-2B | many_random | 32768 | 100 | 0.31 | 0.31 | 0.60 | 2.3 |
| jet-ai/Jet-Nemotron-2B | many_similar | 16384 | 100 | 0.70 | 0.70 | 0.30 | 0.9 |
| jet-ai/Jet-Nemotron-2B | many_similar | 32768 | 100 | 0.22 | 0.22 | 0.72 | 2.4 |
| jet-ai/Jet-Nemotron-2B | multihop | 1024 | 25 | 0.24 | 0.24 | 0.40 | 1.7 |
| jet-ai/Jet-Nemotron-2B | multihop | 2048 | 25 | 0.08 | 0.08 | 0.40 | 0.7 |
| jet-ai/Jet-Nemotron-2B | multihop | 4096 | 25 | 0.20 | 0.20 | 0.32 | 0.6 |
| jet-ai/Jet-Nemotron-2B | multihop | 8192 | 25 | 0.20 | 0.20 | 0.52 | 0.6 |
| jet-ai/Jet-Nemotron-2B | multihop | 16384 | 125 | 0.19 | 0.19 | 0.77 | 0.8 |
| jet-ai/Jet-Nemotron-2B | multihop | 32768 | 125 | 0.11 | 0.11 | 0.86 | 2.1 |
| jet-ai/Jet-Nemotron-2B | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 0.8 |
| jet-ai/Jet-Nemotron-2B | needle | 32768 | 100 | 0.86 | 0.86 | 0.00 | 1.7 |
| jet-ai/Jet-Nemotron-2B | updated | 16384 | 100 | 0.82 | 0.82 | 0.02 | 1.2 |
| jet-ai/Jet-Nemotron-2B | updated | 32768 | 100 | 0.58 | 0.58 | 0.02 | 2.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 16384 | 125 | 1.00 | 1.00 | 0.00 | 1.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 32768 | 125 | 0.98 | 0.98 | 0.02 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 2048 | 25 | 0.96 | 0.96 | 0.04 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 4096 | 25 | 0.96 | 0.96 | 0.04 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 8192 | 25 | 0.92 | 0.92 | 0.08 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 16384 | 125 | 0.98 | 0.98 | 0.02 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 32768 | 125 | 0.88 | 0.88 | 0.12 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 16384 | 125 | 1.00 | 1.00 | 0.00 | 1.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 32768 | 88 | 0.95 | 0.95 | 0.05 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 32768 | 63 | 0.97 | 0.97 | 0.03 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 32768 | 64 | 0.97 | 0.97 | 0.03 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 2048 | 25 | 0.96 | 0.96 | 0.04 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 8192 | 25 | 0.88 | 0.88 | 0.08 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 16384 | 125 | 0.95 | 0.95 | 0.05 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 32768 | 94 | 0.88 | 0.88 | 0.11 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 32768 | 64 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 32768 | 63 | 1.00 | 1.00 | 0.00 | 2.5 |

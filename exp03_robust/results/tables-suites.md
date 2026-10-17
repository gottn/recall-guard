## Recall (contains) by reference length

| model | task | 1024 | 2048 | 4096 | 8192 | 16384 | 32768 |
|---|---|---:|---:|---:|---:|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 0.92 | 0.96 | 0.76 | 0.64 | 0.31 | 0.17 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random |  |  |  |  | 0.25 | 0.25 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar |  |  |  |  | 0.11 | 0.09 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 0.52 | 0.28 | 0.40 | 0.28 | 0.15 | 0.08 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle |  |  |  |  | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated |  |  |  |  | 0.42 | 0.16 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | heldout_many |  |  |  |  | 0.94 | 0.91 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_random |  |  |  |  | 1.00 | 0.95 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_similar |  |  |  |  | 1.00 | 0.87 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | multihop |  |  |  |  | 0.90 | 0.88 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | needle |  |  |  |  | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | updated |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B | heldout_many | 0.96 | 1.00 | 1.00 | 0.92 | 0.91 | 0.93 |
| Qwen/Qwen2.5-1.5B | many_random |  |  |  |  | 0.90 | 0.90 |
| Qwen/Qwen2.5-1.5B | many_similar |  |  |  |  | 0.88 | 0.75 |
| Qwen/Qwen2.5-1.5B | multihop | 0.12 | 0.24 | 0.16 | 0.20 | 0.22 | 0.14 |
| Qwen/Qwen2.5-1.5B | needle |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B | updated |  |  |  |  | 0.42 | 0.34 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_random |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_similar |  |  |  |  | 0.99 | 0.95 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 1.00 | 0.96 | 1.00 | 1.00 | 0.98 | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | needle |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | updated |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | heldout_many |  |  |  |  |  | 0.20 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | many_random |  |  |  |  |  | 0.38 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | many_similar |  |  |  |  |  | 0.44 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | multihop |  |  |  |  |  | 0.50 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | needle |  |  |  |  |  | 0.90 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | updated |  |  |  |  |  | 0.52 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | heldout_many |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | many_random |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | many_similar |  |  |  |  |  | 0.96 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | multihop |  |  |  |  |  | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | needle |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | updated |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_random |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_similar |  |  |  |  | 1.00 | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | needle |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | updated |  |  |  |  | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | heldout_many |  |  |  |  |  | 0.96 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | many_random |  |  |  |  |  | 0.94 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | many_similar |  |  |  |  |  | 0.90 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | multihop |  |  |  |  |  | 0.94 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | needle |  |  |  |  |  | 0.86 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | updated |  |  |  |  |  | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | heldout_many |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | many_random |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | many_similar |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | multihop |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | needle |  |  |  |  |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | updated |  |  |  |  |  | 1.00 |
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
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | heldout_many |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | many_random |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | many_similar |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | multihop |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | needle |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | updated |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | heldout_many |  |  |  |  |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | many_random |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | many_similar |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | multihop |  |  |  |  |  | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | needle |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | updated |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.97 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random |  |  |  |  | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar |  |  |  |  | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 1.00 | 0.96 | 1.00 | 0.88 | 0.95 | 0.89 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | heldout_many |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | many_random |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | many_similar |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | multihop |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | needle |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | updated |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | heldout_many |  |  |  |  |  | 0.94 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | many_random |  |  |  |  |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | many_similar |  |  |  |  |  | 0.96 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | multihop |  |  |  |  |  | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | needle |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | updated |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 | 0.93 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar |  |  |  |  | 0.98 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 1.00 | 0.96 | 1.00 | 0.92 | 0.96 | 0.82 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated |  |  |  |  | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | heldout_many |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | many_random |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | many_similar |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | multihop |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | needle |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | updated |  |  |  |  |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | heldout_many |  |  |  |  |  | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | many_random |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | many_similar |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | multihop |  |  |  |  |  | 0.86 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | needle |  |  |  |  |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | updated |  |  |  |  |  | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | many_random |  |  |  |  | 0.99 | 0.99 |
| meta-llama/Llama-3.1-8B-Instruct | many_similar |  |  |  |  | 0.95 | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 0.76 | 0.72 | 0.76 | 0.52 | 0.63 | 0.49 |
| meta-llama/Llama-3.1-8B-Instruct | needle |  |  |  |  | 1.00 | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | updated |  |  |  |  | 0.87 | 0.74 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 1024 | 25 | 0.92 | 0.92 | 0.08 | 0.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 2048 | 25 | 0.96 | 0.96 | 0.04 | 0.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 4096 | 25 | 0.76 | 0.76 | 0.24 | 0.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 8192 | 25 | 0.64 | 0.64 | 0.36 | 0.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 16384 | 125 | 0.31 | 0.31 | 0.63 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 32768 | 125 | 0.17 | 0.17 | 0.77 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random | 16384 | 100 | 0.25 | 0.25 | 0.72 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random | 32768 | 100 | 0.25 | 0.25 | 0.61 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar | 16384 | 100 | 0.11 | 0.11 | 0.85 | 1.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar | 32768 | 100 | 0.09 | 0.09 | 0.77 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 1024 | 25 | 0.52 | 0.52 | 0.40 | 0.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 2048 | 25 | 0.28 | 0.28 | 0.44 | 0.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 4096 | 25 | 0.40 | 0.32 | 0.56 | 0.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 8192 | 25 | 0.28 | 0.28 | 0.64 | 0.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 16384 | 125 | 0.15 | 0.14 | 0.82 | 1.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 32768 | 125 | 0.08 | 0.08 | 0.81 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated | 16384 | 100 | 0.42 | 0.42 | 0.03 | 1.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated | 32768 | 100 | 0.16 | 0.16 | 0.01 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | heldout_many | 16384 | 50 | 0.94 | 0.94 | 0.04 | 2.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | heldout_many | 32768 | 22 | 0.91 | 0.91 | 0.09 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_random | 16384 | 50 | 1.00 | 1.00 | 0.00 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_random | 32768 | 19 | 0.95 | 0.95 | 0.05 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_similar | 16384 | 50 | 1.00 | 1.00 | 0.00 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_similar | 32768 | 15 | 0.87 | 0.87 | 0.13 | 4.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | multihop | 16384 | 50 | 0.90 | 0.90 | 0.10 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | multihop | 32768 | 26 | 0.88 | 0.88 | 0.12 | 4.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | needle | 16384 | 50 | 1.00 | 1.00 | 0.00 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | needle | 32768 | 21 | 1.00 | 1.00 | 0.00 | 4.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | updated | 16384 | 50 | 1.00 | 1.00 | 0.00 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | updated | 32768 | 18 | 1.00 | 1.00 | 0.00 | 4.2 |
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
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.9 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 16384 | 125 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 32768 | 125 | 1.00 | 1.00 | 0.00 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.2 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_similar | 16384 | 100 | 0.99 | 0.99 | 0.01 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_similar | 32768 | 100 | 0.95 | 0.95 | 0.02 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 2048 | 25 | 0.96 | 0.96 | 0.04 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.9 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 16384 | 125 | 0.98 | 0.98 | 0.02 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 32768 | 125 | 0.98 | 0.98 | 0.02 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | heldout_many | 32768 | 50 | 0.20 | 0.20 | 0.38 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | many_random | 32768 | 50 | 0.38 | 0.38 | 0.42 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | many_similar | 32768 | 50 | 0.44 | 0.44 | 0.44 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | multihop | 32768 | 50 | 0.50 | 0.50 | 0.32 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | needle | 32768 | 50 | 0.90 | 0.90 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | updated | 32768 | 50 | 0.52 | 0.52 | 0.02 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | many_similar | 32768 | 50 | 0.96 | 0.96 | 0.02 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | multihop | 32768 | 50 | 0.98 | 0.98 | 0.02 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.9 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 16384 | 125 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 32768 | 125 | 0.99 | 0.99 | 0.01 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_similar | 32768 | 100 | 0.98 | 0.98 | 0.02 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 4096 | 25 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 8192 | 25 | 1.00 | 1.00 | 0.00 | 0.9 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 16384 | 125 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 32768 | 125 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | heldout_many | 32768 | 50 | 0.96 | 0.96 | 0.02 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | many_random | 32768 | 50 | 0.94 | 0.94 | 0.06 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | many_similar | 32768 | 50 | 0.90 | 0.90 | 0.08 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | multihop | 32768 | 50 | 0.94 | 0.94 | 0.04 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | needle | 32768 | 50 | 0.86 | 0.86 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | updated | 32768 | 50 | 0.98 | 0.98 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | multihop | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 2.3 |
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
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | heldout_many | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | many_random | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | many_similar | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | multihop | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | needle | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | updated | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.02 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 4.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | multihop | 32768 | 50 | 0.88 | 0.88 | 0.12 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 16384 | 125 | 1.00 | 1.00 | 0.00 | 1.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 32768 | 125 | 0.97 | 0.97 | 0.03 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 32768 | 100 | 0.98 | 0.98 | 0.02 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 32768 | 100 | 0.98 | 0.98 | 0.02 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 2048 | 25 | 0.96 | 0.96 | 0.04 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 8192 | 25 | 0.88 | 0.88 | 0.08 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 16384 | 125 | 0.95 | 0.95 | 0.05 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 32768 | 125 | 0.89 | 0.89 | 0.10 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | heldout_many | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | many_random | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | many_similar | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | multihop | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | needle | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | updated | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | heldout_many | 32768 | 50 | 0.94 | 0.94 | 0.06 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | many_random | 32768 | 50 | 0.98 | 0.98 | 0.02 | 4.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | many_similar | 32768 | 50 | 0.96 | 0.96 | 0.04 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | multihop | 32768 | 50 | 0.88 | 0.88 | 0.12 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 16384 | 125 | 0.99 | 0.99 | 0.01 | 1.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 32768 | 125 | 0.93 | 0.93 | 0.07 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar | 16384 | 100 | 0.98 | 0.98 | 0.02 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 1024 | 25 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 2048 | 25 | 0.96 | 0.96 | 0.04 | 1.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 8192 | 25 | 0.92 | 0.92 | 0.08 | 1.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 16384 | 125 | 0.96 | 0.96 | 0.04 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 32768 | 125 | 0.82 | 0.82 | 0.18 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | heldout_many | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | many_random | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | many_similar | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | multihop | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | needle | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | updated | 32768 | 50 | 0.00 | 0.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | heldout_many | 32768 | 50 | 0.88 | 0.88 | 0.12 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 4.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | multihop | 32768 | 50 | 0.86 | 0.86 | 0.14 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 3.8 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 1024 | 25 | 1.00 | 1.00 | 0.00 | 0.4 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 2048 | 25 | 1.00 | 1.00 | 0.00 | 0.9 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 4096 | 25 | 1.00 | 1.00 | 0.00 | 1.1 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 8192 | 25 | 1.00 | 1.00 | 0.00 | 1.5 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 16384 | 125 | 1.00 | 1.00 | 0.00 | 2.0 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 32768 | 125 | 1.00 | 1.00 | 0.00 | 4.0 |
| meta-llama/Llama-3.1-8B-Instruct | many_random | 16384 | 100 | 0.99 | 0.99 | 0.01 | 1.8 |
| meta-llama/Llama-3.1-8B-Instruct | many_random | 32768 | 100 | 0.99 | 0.99 | 0.01 | 4.4 |
| meta-llama/Llama-3.1-8B-Instruct | many_similar | 16384 | 100 | 0.95 | 0.95 | 0.04 | 2.1 |
| meta-llama/Llama-3.1-8B-Instruct | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.5 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 1024 | 25 | 0.76 | 0.76 | 0.24 | 0.9 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 2048 | 25 | 0.72 | 0.72 | 0.28 | 1.0 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 4096 | 25 | 0.76 | 0.72 | 0.16 | 1.1 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 8192 | 25 | 0.52 | 0.52 | 0.44 | 1.5 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 16384 | 125 | 0.63 | 0.62 | 0.32 | 2.3 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 32768 | 125 | 0.49 | 0.46 | 0.50 | 4.6 |
| meta-llama/Llama-3.1-8B-Instruct | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| meta-llama/Llama-3.1-8B-Instruct | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.5 |
| meta-llama/Llama-3.1-8B-Instruct | updated | 16384 | 100 | 0.87 | 0.82 | 0.13 | 2.3 |
| meta-llama/Llama-3.1-8B-Instruct | updated | 32768 | 100 | 0.74 | 0.72 | 0.25 | 4.6 |

## Recall (contains) by reference length

| model | task | 16384 | 32768 |
|---|---|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 0.33 | 0.17 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random | 0.25 | 0.25 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar | 0.11 | 0.09 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 0.15 | 0.06 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated | 0.42 | 0.16 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | heldout_many | 1.00 | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | many_random | 0.97 | 0.97 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | many_similar | 0.97 | 0.85 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | multihop | 0.95 | 0.89 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | updated | 1.00 | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | heldout_many |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | many_random |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | many_similar |  | 0.82 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | multihop |  | 0.86 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | updated |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | heldout_many |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | many_random |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | many_similar |  | 0.84 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | multihop |  | 0.88 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | updated |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | heldout_many | 0.99 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_similar | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | multihop | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | heldout_many | 0.99 | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | many_random | 0.99 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | many_similar | 0.96 | 0.97 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | multihop | 0.99 | 0.97 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | heldout_many | 0.98 | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | many_similar | 0.98 | 0.94 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | multihop | 0.96 | 0.94 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | updated | 0.99 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | heldout_many |  | 0.88 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | many_similar |  | 0.94 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | multihop |  | 0.82 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | heldout_many |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | many_similar |  | 0.94 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | multihop |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | heldout_many | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | many_similar | 0.98 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | multihop | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | heldout_many |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | many_similar |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | multihop |  | 0.92 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | heldout_many |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | many_similar |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | multihop |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | updated |  | 1.00 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 0.89 | 0.45 |
| jet-ai/Jet-Nemotron-2B | many_random | 0.57 | 0.31 |
| jet-ai/Jet-Nemotron-2B | many_similar | 0.70 | 0.22 |
| jet-ai/Jet-Nemotron-2B | multihop | 0.20 | 0.11 |
| jet-ai/Jet-Nemotron-2B | needle | 1.00 | 0.86 |
| jet-ai/Jet-Nemotron-2B | updated | 0.82 | 0.58 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_random | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_similar | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 0.97 | 0.89 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | updated | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | heldout_many | 1.00 | 0.99 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | many_random | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | many_similar | 1.00 | 0.99 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | multihop | 0.84 | 0.87 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | updated | 1.00 | 0.99 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | heldout_many |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | many_random |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | many_similar |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | multihop |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | needle |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | updated |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | heldout_many |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | many_random |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | many_similar |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | multihop |  | 0.84 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | needle |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | updated |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | heldout_many | 0.99 | 0.97 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | many_random | 1.00 | 0.99 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | many_similar | 1.00 | 0.97 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | multihop | 0.65 | 0.45 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | updated | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 1.00 | 0.96 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 0.94 | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | heldout_many | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | many_random | 1.00 | 0.99 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | many_similar | 0.99 | 0.99 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | multihop | 0.62 | 0.49 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | updated | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | heldout_many |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | many_random |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | many_similar |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | multihop |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | needle |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | updated |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | heldout_many |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | many_random |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | many_similar |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | multihop |  | 0.44 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | needle |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | updated |  | 0.96 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 0.99 | 0.93 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar | 0.98 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 0.95 | 0.81 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | heldout_many | 0.99 | 0.94 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | many_random | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | many_similar | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | multihop | 0.68 | 0.61 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | updated | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | heldout_many |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | many_random |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | many_similar |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | multihop |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | needle |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | updated |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | heldout_many |  | 0.90 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | many_random |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | many_similar |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | multihop |  | 0.58 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | needle |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | updated |  | 1.00 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 16384 | 100 | 0.33 | 0.33 | 0.60 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 32768 | 100 | 0.17 | 0.17 | 0.79 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random | 16384 | 100 | 0.25 | 0.25 | 0.72 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random | 32768 | 100 | 0.25 | 0.25 | 0.61 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar | 16384 | 100 | 0.11 | 0.11 | 0.85 | 1.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar | 32768 | 100 | 0.09 | 0.09 | 0.77 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 16384 | 100 | 0.15 | 0.14 | 0.82 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 32768 | 100 | 0.06 | 0.06 | 0.81 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated | 16384 | 100 | 0.42 | 0.42 | 0.03 | 1.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated | 32768 | 100 | 0.16 | 0.16 | 0.01 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | heldout_many | 32768 | 100 | 0.96 | 0.96 | 0.04 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | many_random | 16384 | 100 | 0.97 | 0.97 | 0.03 | 4.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | many_random | 32768 | 100 | 0.97 | 0.97 | 0.03 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | many_similar | 16384 | 100 | 0.97 | 0.97 | 0.03 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | many_similar | 32768 | 100 | 0.85 | 0.85 | 0.15 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | multihop | 16384 | 100 | 0.95 | 0.95 | 0.05 | 4.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | multihop | 32768 | 100 | 0.89 | 0.89 | 0.11 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget | updated | 32768 | 100 | 0.98 | 0.98 | 0.00 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | heldout_many | 32768 | 50 | 0.96 | 0.96 | 0.04 | 8.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | many_random | 32768 | 50 | 0.96 | 0.96 | 0.04 | 7.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | many_similar | 32768 | 50 | 0.82 | 0.82 | 0.18 | 7.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | multihop | 32768 | 50 | 0.86 | 0.86 | 0.10 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+chat | updated | 32768 | 50 | 0.96 | 0.96 | 0.04 | 7.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | heldout_many | 32768 | 50 | 0.96 | 0.96 | 0.04 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | many_random | 32768 | 50 | 0.96 | 0.96 | 0.04 | 9.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | many_similar | 32768 | 50 | 0.84 | 0.84 | 0.16 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | multihop | 32768 | 50 | 0.88 | 0.88 | 0.12 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-budget+unmerged | updated | 32768 | 50 | 0.98 | 0.98 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | heldout_many | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | heldout_many | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_similar | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | multihop | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | multihop | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | heldout_many | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | heldout_many | 32768 | 100 | 0.98 | 0.98 | 0.02 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | many_random | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | many_similar | 16384 | 100 | 0.96 | 0.96 | 0.04 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | many_similar | 32768 | 100 | 0.97 | 0.97 | 0.03 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | multihop | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | multihop | 32768 | 100 | 0.97 | 0.97 | 0.03 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-realmix | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | heldout_many | 16384 | 100 | 0.98 | 0.98 | 0.02 | 5.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | heldout_many | 32768 | 100 | 0.96 | 0.96 | 0.04 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | many_similar | 16384 | 100 | 0.98 | 0.98 | 0.02 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | many_similar | 32768 | 100 | 0.94 | 0.94 | 0.06 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | multihop | 16384 | 100 | 0.96 | 0.96 | 0.04 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | multihop | 32768 | 100 | 0.94 | 0.94 | 0.06 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | updated | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | heldout_many | 32768 | 50 | 0.88 | 0.88 | 0.12 | 8.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | many_similar | 32768 | 50 | 0.94 | 0.94 | 0.06 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | multihop | 32768 | 50 | 0.82 | 0.82 | 0.06 | 8.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 11.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | many_similar | 32768 | 50 | 0.94 | 0.94 | 0.06 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | multihop | 32768 | 50 | 0.96 | 0.96 | 0.04 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-budget+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | heldout_many | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | many_similar | 16384 | 100 | 0.98 | 0.98 | 0.02 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | many_similar | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | multihop | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | multihop | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | multihop | 32768 | 50 | 0.92 | 0.92 | 0.02 | 8.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | many_similar | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | multihop | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-budget+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 16384 | 100 | 0.89 | 0.89 | 0.11 | 1.5 |
| jet-ai/Jet-Nemotron-2B | heldout_many | 32768 | 100 | 0.45 | 0.45 | 0.51 | 2.1 |
| jet-ai/Jet-Nemotron-2B | many_random | 16384 | 100 | 0.57 | 0.57 | 0.39 | 1.4 |
| jet-ai/Jet-Nemotron-2B | many_random | 32768 | 100 | 0.31 | 0.31 | 0.60 | 2.3 |
| jet-ai/Jet-Nemotron-2B | many_similar | 16384 | 100 | 0.70 | 0.70 | 0.30 | 0.9 |
| jet-ai/Jet-Nemotron-2B | many_similar | 32768 | 100 | 0.22 | 0.22 | 0.72 | 2.4 |
| jet-ai/Jet-Nemotron-2B | multihop | 16384 | 100 | 0.20 | 0.20 | 0.76 | 0.9 |
| jet-ai/Jet-Nemotron-2B | multihop | 32768 | 100 | 0.11 | 0.11 | 0.86 | 2.1 |
| jet-ai/Jet-Nemotron-2B | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 0.8 |
| jet-ai/Jet-Nemotron-2B | needle | 32768 | 100 | 0.86 | 0.86 | 0.00 | 1.7 |
| jet-ai/Jet-Nemotron-2B | updated | 16384 | 100 | 0.82 | 0.82 | 0.02 | 1.2 |
| jet-ai/Jet-Nemotron-2B | updated | 32768 | 100 | 0.58 | 0.58 | 0.02 | 2.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | heldout_many | 32768 | 100 | 0.98 | 0.98 | 0.02 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 16384 | 100 | 0.97 | 0.97 | 0.03 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | multihop | 32768 | 100 | 0.89 | 0.89 | 0.11 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | heldout_many | 32768 | 100 | 0.99 | 0.99 | 0.01 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | many_similar | 32768 | 100 | 0.99 | 0.99 | 0.01 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | multihop | 16384 | 100 | 0.84 | 0.84 | 0.16 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | multihop | 32768 | 100 | 0.87 | 0.87 | 0.13 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | updated | 32768 | 100 | 0.99 | 0.99 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | heldout_many | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | many_random | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | many_similar | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | multihop | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | needle | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+chat | updated | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | many_similar | 32768 | 50 | 0.98 | 0.98 | 0.02 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | multihop | 32768 | 50 | 0.84 | 0.84 | 0.16 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | heldout_many | 16384 | 100 | 0.99 | 0.99 | 0.01 | 2.7 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | heldout_many | 32768 | 100 | 0.97 | 0.97 | 0.03 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.7 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | many_random | 32768 | 100 | 0.99 | 0.99 | 0.01 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | many_similar | 32768 | 100 | 0.97 | 0.97 | 0.03 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | multihop | 16384 | 100 | 0.65 | 0.65 | 0.35 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | multihop | 32768 | 100 | 0.45 | 0.45 | 0.55 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | updated | 32768 | 100 | 0.98 | 0.98 | 0.01 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 32768 | 100 | 0.96 | 0.96 | 0.04 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 32768 | 100 | 0.98 | 0.98 | 0.02 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 32768 | 100 | 0.98 | 0.98 | 0.02 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 16384 | 100 | 0.94 | 0.94 | 0.06 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 32768 | 100 | 0.88 | 0.88 | 0.12 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | heldout_many | 32768 | 100 | 0.98 | 0.98 | 0.02 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | many_random | 32768 | 100 | 0.99 | 0.99 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | many_similar | 16384 | 100 | 0.99 | 0.99 | 0.01 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | many_similar | 32768 | 100 | 0.99 | 0.99 | 0.01 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | multihop | 16384 | 100 | 0.62 | 0.62 | 0.38 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | multihop | 32768 | 100 | 0.49 | 0.49 | 0.51 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | updated | 32768 | 100 | 0.98 | 0.98 | 0.02 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | heldout_many | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | many_random | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.7 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | many_similar | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | multihop | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | needle | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+chat | updated | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.02 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | many_random | 32768 | 50 | 0.98 | 0.98 | 0.00 | 8.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | multihop | 32768 | 50 | 0.44 | 0.44 | 0.56 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget+unmerged | updated | 32768 | 50 | 0.96 | 0.96 | 0.04 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 16384 | 100 | 0.99 | 0.99 | 0.01 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 32768 | 100 | 0.93 | 0.93 | 0.07 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar | 16384 | 100 | 0.98 | 0.98 | 0.02 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 16384 | 100 | 0.95 | 0.95 | 0.05 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 32768 | 100 | 0.81 | 0.81 | 0.19 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | heldout_many | 16384 | 100 | 0.99 | 0.99 | 0.01 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | heldout_many | 32768 | 100 | 0.94 | 0.94 | 0.06 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | multihop | 16384 | 100 | 0.68 | 0.68 | 0.32 | 3.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | multihop | 32768 | 100 | 0.61 | 0.61 | 0.38 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 3.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | heldout_many | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | many_random | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | many_similar | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | multihop | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | needle | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+chat | updated | 32768 | 50 | 0.00 | 0.00 | 0.00 | 5.3 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | heldout_many | 32768 | 50 | 0.90 | 0.90 | 0.10 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | multihop | 32768 | 50 | 0.58 | 0.58 | 0.40 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.2 |

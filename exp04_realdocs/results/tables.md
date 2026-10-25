## Recall (contains) by reference length

| model | task | 4096 | 16384 | 32768 |
|---|---|---:|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_1 | 0.86 | 0.65 | 0.19 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_2 | 0.51 | 0.34 | 0.35 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_1 | 0.81 | 0.76 | 0.56 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_2 | 0.50 | 0.38 | 0.36 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_1 | 0.84 | 0.76 | 0.35 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_2 | 0.59 | 0.41 | 0.42 |
| Qwen/Qwen2.5-1.5B | ruler_qa_1 | 0.69 | 0.45 | 0.36 |
| Qwen/Qwen2.5-1.5B | ruler_qa_2 | 0.50 | 0.39 | 0.32 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_1 | 0.70 | 0.50 | 0.38 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_2 | 0.44 | 0.34 | 0.38 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_1 | 0.70 | 0.39 | 0.12 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_2 | 0.50 | 0.28 | 0.27 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_1 | 0.67 | 0.42 | 0.26 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_2 | 0.46 | 0.33 | 0.28 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_1 | 0.92 | 0.82 | 0.83 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_2 | 0.67 | 0.64 | 0.57 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_1 | 4096 | 100 | 0.86 | 0.00 | 0.00 | 1.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_1 | 16384 | 100 | 0.65 | 0.00 | 0.00 | 3.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_1 | 32768 | 100 | 0.19 | 0.00 | 0.00 | 6.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_2 | 4096 | 100 | 0.51 | 0.00 | 0.00 | 1.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_2 | 16384 | 100 | 0.34 | 0.00 | 0.00 | 3.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | ruler_qa_2 | 32768 | 100 | 0.35 | 0.00 | 0.00 | 6.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_1 | 4096 | 100 | 0.81 | 0.00 | 0.00 | 1.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_1 | 16384 | 100 | 0.76 | 0.00 | 0.00 | 3.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_1 | 32768 | 100 | 0.56 | 0.00 | 0.00 | 7.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_2 | 4096 | 100 | 0.50 | 0.00 | 0.00 | 1.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_2 | 16384 | 100 | 0.38 | 0.00 | 0.00 | 4.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | ruler_qa_2 | 32768 | 100 | 0.36 | 0.00 | 0.00 | 7.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_1 | 4096 | 100 | 0.84 | 0.00 | 0.00 | 3.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_1 | 16384 | 100 | 0.76 | 0.00 | 0.00 | 5.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_1 | 32768 | 100 | 0.35 | 0.00 | 0.00 | 8.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_2 | 4096 | 100 | 0.59 | 0.00 | 0.00 | 2.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_2 | 16384 | 100 | 0.41 | 0.00 | 0.00 | 5.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | ruler_qa_2 | 32768 | 100 | 0.42 | 0.00 | 0.00 | 8.4 |
| Qwen/Qwen2.5-1.5B | ruler_qa_1 | 4096 | 100 | 0.69 | 0.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B | ruler_qa_1 | 16384 | 100 | 0.45 | 0.00 | 0.00 | 2.3 |
| Qwen/Qwen2.5-1.5B | ruler_qa_1 | 32768 | 100 | 0.36 | 0.00 | 0.00 | 3.7 |
| Qwen/Qwen2.5-1.5B | ruler_qa_2 | 4096 | 100 | 0.50 | 0.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B | ruler_qa_2 | 16384 | 100 | 0.39 | 0.00 | 0.00 | 2.4 |
| Qwen/Qwen2.5-1.5B | ruler_qa_2 | 32768 | 100 | 0.32 | 0.00 | 0.00 | 3.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_1 | 4096 | 100 | 0.70 | 0.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_1 | 16384 | 100 | 0.50 | 0.00 | 0.00 | 2.4 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_1 | 32768 | 100 | 0.38 | 0.00 | 0.00 | 3.6 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_2 | 4096 | 100 | 0.44 | 0.00 | 0.00 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_2 | 16384 | 100 | 0.34 | 0.00 | 0.00 | 2.4 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | ruler_qa_2 | 32768 | 100 | 0.38 | 0.00 | 0.00 | 3.7 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_1 | 4096 | 100 | 0.70 | 0.00 | 0.00 | 2.1 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_1 | 16384 | 100 | 0.39 | 0.00 | 0.00 | 3.0 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_1 | 32768 | 100 | 0.12 | 0.00 | 0.00 | 4.4 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_2 | 4096 | 100 | 0.50 | 0.00 | 0.00 | 2.1 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_2 | 16384 | 100 | 0.28 | 0.00 | 0.00 | 3.7 |
| jet-ai/Jet-Nemotron-2B | ruler_qa_2 | 32768 | 100 | 0.27 | 0.00 | 0.00 | 4.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_1 | 4096 | 100 | 0.67 | 0.00 | 0.00 | 3.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_1 | 16384 | 100 | 0.42 | 0.00 | 0.00 | 3.7 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_1 | 32768 | 100 | 0.26 | 0.00 | 0.00 | 5.2 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_2 | 4096 | 100 | 0.46 | 0.00 | 0.00 | 3.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_2 | 16384 | 100 | 0.33 | 0.00 | 0.00 | 4.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_qa_2 | 32768 | 100 | 0.28 | 0.00 | 0.00 | 5.4 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_1 | 4096 | 100 | 0.92 | 0.00 | 0.00 | 2.2 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_1 | 16384 | 100 | 0.82 | 0.00 | 0.00 | 4.3 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_1 | 32768 | 100 | 0.83 | 0.00 | 0.00 | 9.1 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_2 | 4096 | 100 | 0.67 | 0.00 | 0.00 | 2.1 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_2 | 16384 | 100 | 0.64 | 0.00 | 0.00 | 4.2 |
| meta-llama/Llama-3.1-8B-Instruct | ruler_qa_2 | 32768 | 100 | 0.57 | 0.00 | 0.00 | 8.7 |

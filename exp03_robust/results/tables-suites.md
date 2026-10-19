## Recall (contains) by reference length

| model | task | 16384 | 32768 |
|---|---|---:|---:|
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | heldout_many | 0.33 | 0.17 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_random | 0.25 | 0.25 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | many_similar | 0.11 | 0.09 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | multihop | 0.15 | 0.06 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo | updated | 0.42 | 0.16 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | heldout_many | 0.99 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | many_similar | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | multihop | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | heldout_many |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | many_similar |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | multihop |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | heldout_many |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | many_similar |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | multihop |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | heldout_many | 0.92 | 0.85 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | many_random | 0.96 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | many_similar | 0.85 | 0.77 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | multihop | 0.41 | 0.30 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | updated | 0.99 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | heldout_many |  | 0.80 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | many_random |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | many_similar |  | 0.74 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | multihop |  | 0.34 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | updated |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | heldout_many |  | 0.86 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | many_random |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | many_similar |  | 0.78 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | multihop |  | 0.26 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | updated |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | heldout_many | 0.97 | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | many_similar | 1.00 | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | multihop | 0.37 | 0.30 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | heldout_many |  | 0.92 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | many_random |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | many_similar |  | 0.94 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | multihop |  | 0.32 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | heldout_many |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | many_similar |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | multihop |  | 0.34 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | heldout_many | 0.94 | 0.95 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_random | 1.00 | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_similar | 0.99 | 0.91 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | multihop | 0.93 | 0.85 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | heldout_many | 0.97 | 0.92 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | many_similar | 0.95 | 0.89 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | multihop | 0.97 | 0.90 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | updated | 1.00 | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | heldout_many |  | 0.90 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | many_similar |  | 0.84 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | multihop |  | 0.76 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | updated |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | heldout_many |  | 0.90 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | many_similar |  | 0.86 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | multihop |  | 0.88 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | updated |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | heldout_many | 0.98 | 0.92 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | many_random | 1.00 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | many_similar | 0.89 | 0.86 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | multihop | 0.29 | 0.36 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | heldout_many |  | 0.82 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | many_random |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | many_similar |  | 0.78 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | multihop |  | 0.30 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | heldout_many |  | 0.88 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | many_similar |  | 0.82 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | multihop |  | 0.42 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | heldout_many | 0.98 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | many_random | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | many_similar | 0.99 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | multihop | 0.99 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | updated | 0.99 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | heldout_many |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | many_similar |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | multihop |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | heldout_many |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | many_similar |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | multihop |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | updated |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | heldout_many | 0.99 | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | many_random | 0.99 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | many_similar | 0.99 | 0.99 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | multihop | 0.99 | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | needle | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | updated | 1.00 | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | heldout_many |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | many_similar |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | multihop |  | 0.90 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | heldout_many |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | many_random |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | many_similar |  | 0.98 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | multihop |  | 0.96 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | needle |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | updated |  | 1.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | heldout_many | 0.04 | 0.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | many_random | 0.07 | 0.04 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | many_similar | 0.03 | 0.00 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | multihop | 0.03 | 0.05 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | needle | 0.67 | 0.72 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | updated | 0.11 | 0.03 |
| Qwen/Qwen2.5-1.5B | heldout_many | 0.91 | 0.94 |
| Qwen/Qwen2.5-1.5B | many_random | 0.90 | 0.90 |
| Qwen/Qwen2.5-1.5B | many_similar | 0.88 | 0.75 |
| Qwen/Qwen2.5-1.5B | multihop | 0.20 | 0.14 |
| Qwen/Qwen2.5-1.5B | needle | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B | updated | 0.42 | 0.34 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_random | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_similar | 0.99 | 0.95 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 0.99 | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | needle | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | updated | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | heldout_many |  | 0.20 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | many_random |  | 0.38 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | many_similar |  | 0.44 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | multihop |  | 0.50 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | needle |  | 0.90 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+chat | updated |  | 0.52 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | heldout_many |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | many_random |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | many_similar |  | 0.96 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | multihop |  | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | needle |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1+unmerged | updated |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 1.00 | 0.99 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_random | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_similar | 1.00 | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | needle | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | updated | 1.00 | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | heldout_many |  | 0.96 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | many_random |  | 0.94 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | many_similar |  | 0.90 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | multihop |  | 0.94 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | needle |  | 0.86 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+chat | updated |  | 0.98 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | heldout_many |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | many_random |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | many_similar |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | multihop |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | needle |  | 1.00 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2+unmerged | updated |  | 1.00 |
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
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | heldout_many |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | many_random |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | many_similar |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | multihop |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | needle |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+chat | updated |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | heldout_many |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | many_random |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | many_similar |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | multihop |  | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | needle |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1+unmerged | updated |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | heldout_many | 1.00 | 0.96 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_random | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | many_similar | 1.00 | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | multihop | 0.94 | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | updated | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | heldout_many |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | many_random |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | many_similar |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | multihop |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | needle |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+chat | updated |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | heldout_many |  | 0.94 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | many_random |  | 0.98 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | many_similar |  | 0.96 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | multihop |  | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | needle |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2+unmerged | updated |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | heldout_many | 0.99 | 0.93 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_random | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | many_similar | 0.98 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | multihop | 0.95 | 0.81 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | needle | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | updated | 1.00 | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | heldout_many |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | many_random |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | many_similar |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | multihop |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | needle |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+chat | updated |  | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | heldout_many |  | 0.88 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | many_random |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | many_similar |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | multihop |  | 0.86 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | needle |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3+unmerged | updated |  | 1.00 |
| jet-ai/Jet-Nemotron-2B+qk-restore | heldout_many | 0.00 | 0.00 |
| jet-ai/Jet-Nemotron-2B+qk-restore | many_random | 0.00 | 0.00 |
| jet-ai/Jet-Nemotron-2B+qk-restore | many_similar | 0.00 | 0.00 |
| jet-ai/Jet-Nemotron-2B+qk-restore | multihop | 0.00 | 0.00 |
| jet-ai/Jet-Nemotron-2B+qk-restore | needle | 0.00 | 0.00 |
| jet-ai/Jet-Nemotron-2B+qk-restore | updated | 0.00 | 0.00 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 1.00 | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | many_random | 0.99 | 0.99 |
| meta-llama/Llama-3.1-8B-Instruct | many_similar | 0.95 | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 0.63 | 0.49 |
| meta-llama/Llama-3.1-8B-Instruct | needle | 1.00 | 1.00 |
| meta-llama/Llama-3.1-8B-Instruct | updated | 0.87 | 0.74 |

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
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | multihop | 32768 | 50 | 0.96 | 0.96 | 0.04 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | heldout_many | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | multihop | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | heldout_many | 16384 | 100 | 0.92 | 0.92 | 0.08 | 4.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | heldout_many | 32768 | 100 | 0.85 | 0.85 | 0.15 | 8.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | many_random | 16384 | 100 | 0.96 | 0.96 | 0.04 | 4.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | many_random | 32768 | 100 | 0.99 | 0.99 | 0.01 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | many_similar | 16384 | 100 | 0.85 | 0.85 | 0.15 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | many_similar | 32768 | 100 | 0.77 | 0.77 | 0.22 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | multihop | 16384 | 100 | 0.41 | 0.41 | 0.47 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | multihop | 32768 | 100 | 0.30 | 0.30 | 0.66 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 7.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | updated | 16384 | 100 | 0.99 | 0.99 | 0.01 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay | updated | 32768 | 100 | 0.99 | 0.99 | 0.00 | 8.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | heldout_many | 32768 | 50 | 0.80 | 0.80 | 0.20 | 7.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | many_random | 32768 | 50 | 0.98 | 0.98 | 0.02 | 7.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | many_similar | 32768 | 50 | 0.74 | 0.74 | 0.24 | 7.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | multihop | 32768 | 50 | 0.34 | 0.34 | 0.50 | 7.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+chat | updated | 32768 | 50 | 0.96 | 0.96 | 0.00 | 7.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | heldout_many | 32768 | 50 | 0.86 | 0.86 | 0.14 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | many_random | 32768 | 50 | 0.98 | 0.98 | 0.02 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | many_similar | 32768 | 50 | 0.78 | 0.78 | 0.20 | 9.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | multihop | 32768 | 50 | 0.26 | 0.26 | 0.70 | 9.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle-replay+unmerged | updated | 32768 | 50 | 0.98 | 0.98 | 0.00 | 9.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | heldout_many | 16384 | 100 | 0.97 | 0.97 | 0.03 | 5.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | heldout_many | 32768 | 100 | 0.96 | 0.96 | 0.04 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | many_similar | 32768 | 100 | 0.98 | 0.98 | 0.02 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | multihop | 16384 | 100 | 0.37 | 0.37 | 0.50 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | multihop | 32768 | 100 | 0.30 | 0.30 | 0.68 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25 | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | heldout_many | 32768 | 50 | 0.92 | 0.92 | 0.08 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | many_random | 32768 | 50 | 0.98 | 0.98 | 0.02 | 7.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | many_similar | 32768 | 50 | 0.94 | 0.94 | 0.06 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | multihop | 32768 | 50 | 0.32 | 0.32 | 0.38 | 8.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | many_similar | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | multihop | 32768 | 50 | 0.34 | 0.34 | 0.64 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-gentle2-replay25+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | heldout_many | 16384 | 100 | 0.94 | 0.94 | 0.05 | 2.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | heldout_many | 32768 | 100 | 0.95 | 0.95 | 0.05 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_random | 32768 | 100 | 0.98 | 0.98 | 0.02 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_similar | 16384 | 100 | 0.99 | 0.99 | 0.01 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | many_similar | 32768 | 100 | 0.91 | 0.91 | 0.09 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | multihop | 16384 | 100 | 0.93 | 0.93 | 0.07 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | multihop | 32768 | 100 | 0.85 | 0.85 | 0.15 | 4.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-le16k | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | heldout_many | 16384 | 100 | 0.97 | 0.97 | 0.03 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | heldout_many | 32768 | 100 | 0.92 | 0.92 | 0.08 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | many_similar | 16384 | 100 | 0.95 | 0.95 | 0.05 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | many_similar | 32768 | 100 | 0.89 | 0.89 | 0.11 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | multihop | 16384 | 100 | 0.97 | 0.97 | 0.03 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | multihop | 32768 | 100 | 0.90 | 0.90 | 0.10 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk | updated | 32768 | 100 | 0.96 | 0.96 | 0.03 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | heldout_many | 32768 | 50 | 0.90 | 0.90 | 0.08 | 8.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | many_similar | 32768 | 50 | 0.84 | 0.84 | 0.16 | 8.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | multihop | 32768 | 50 | 0.76 | 0.76 | 0.14 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 8.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+chat | updated | 32768 | 50 | 0.98 | 0.98 | 0.02 | 8.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | heldout_many | 32768 | 50 | 0.90 | 0.90 | 0.10 | 9.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.8 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | many_similar | 32768 | 50 | 0.86 | 0.86 | 0.14 | 9.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | multihop | 32768 | 50 | 0.88 | 0.88 | 0.12 | 9.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-qk+unmerged | updated | 32768 | 50 | 0.96 | 0.96 | 0.02 | 9.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | heldout_many | 16384 | 100 | 0.98 | 0.98 | 0.02 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | heldout_many | 32768 | 100 | 0.92 | 0.92 | 0.08 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | many_random | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | many_similar | 16384 | 100 | 0.89 | 0.89 | 0.11 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | many_similar | 32768 | 100 | 0.86 | 0.86 | 0.14 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | multihop | 16384 | 100 | 0.29 | 0.29 | 0.23 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | multihop | 32768 | 100 | 0.36 | 0.36 | 0.25 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | heldout_many | 32768 | 50 | 0.82 | 0.82 | 0.16 | 7.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | many_random | 32768 | 50 | 0.98 | 0.98 | 0.02 | 7.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | many_similar | 32768 | 50 | 0.78 | 0.78 | 0.22 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | multihop | 32768 | 50 | 0.30 | 0.30 | 0.14 | 7.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | heldout_many | 32768 | 50 | 0.88 | 0.88 | 0.12 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 11.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | many_similar | 32768 | 50 | 0.82 | 0.82 | 0.18 | 10.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | multihop | 32768 | 50 | 0.42 | 0.42 | 0.18 | 10.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed1-replay+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | heldout_many | 16384 | 100 | 0.98 | 0.98 | 0.02 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | heldout_many | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | many_similar | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | multihop | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | multihop | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | updated | 16384 | 100 | 0.99 | 0.99 | 0.01 | 5.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle | updated | 32768 | 100 | 0.99 | 0.99 | 0.01 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | multihop | 32768 | 50 | 0.98 | 0.98 | 0.02 | 7.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.9 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | many_similar | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | multihop | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed2-gentle+unmerged | updated | 32768 | 50 | 0.98 | 0.98 | 0.02 | 10.7 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | heldout_many | 16384 | 100 | 0.99 | 0.99 | 0.01 | 4.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | heldout_many | 32768 | 100 | 0.98 | 0.98 | 0.02 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | many_random | 16384 | 100 | 0.99 | 0.99 | 0.01 | 4.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | many_random | 32768 | 100 | 0.99 | 0.99 | 0.01 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | many_similar | 16384 | 100 | 0.99 | 0.99 | 0.01 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | many_similar | 32768 | 100 | 0.99 | 0.99 | 0.01 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | multihop | 16384 | 100 | 0.99 | 0.99 | 0.01 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | multihop | 32768 | 100 | 0.98 | 0.98 | 0.02 | 8.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 8.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | updated | 16384 | 100 | 1.00 | 1.00 | 0.00 | 4.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle | updated | 32768 | 100 | 1.00 | 1.00 | 0.00 | 8.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | heldout_many | 32768 | 50 | 0.96 | 0.96 | 0.04 | 7.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.5 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | many_similar | 32768 | 50 | 0.98 | 0.98 | 0.02 | 7.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | multihop | 32768 | 50 | 0.90 | 0.90 | 0.08 | 7.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.0 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+chat | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 7.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | heldout_many | 32768 | 50 | 0.98 | 0.98 | 0.02 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | many_random | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | many_similar | 32768 | 50 | 0.98 | 0.98 | 0.02 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | multihop | 32768 | 50 | 0.96 | 0.96 | 0.04 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | needle | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.1 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+adapter-JunxiongWang_Llama3.1-Mamba2-8B-dpo-seed3-gentle+unmerged | updated | 32768 | 50 | 1.00 | 1.00 | 0.00 | 9.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | heldout_many | 16384 | 100 | 0.04 | 0.04 | 0.34 | 3.6 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | heldout_many | 32768 | 56 | 0.00 | 0.00 | 0.21 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | many_random | 16384 | 100 | 0.07 | 0.07 | 0.30 | 3.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | many_random | 32768 | 57 | 0.04 | 0.04 | 0.35 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | many_similar | 16384 | 100 | 0.03 | 0.03 | 0.33 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | many_similar | 32768 | 58 | 0.00 | 0.00 | 0.34 | 7.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | multihop | 16384 | 100 | 0.03 | 0.03 | 0.39 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | multihop | 32768 | 59 | 0.05 | 0.05 | 0.27 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | needle | 16384 | 100 | 0.67 | 0.67 | 0.00 | 3.4 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | needle | 32768 | 60 | 0.72 | 0.72 | 0.00 | 7.2 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | updated | 16384 | 100 | 0.11 | 0.11 | 0.00 | 3.3 |
| JunxiongWang/Llama3.1-Mamba2-8B-dpo+qk-restore | updated | 32768 | 60 | 0.03 | 0.03 | 0.02 | 7.2 |
| Qwen/Qwen2.5-1.5B | heldout_many | 16384 | 100 | 0.91 | 0.91 | 0.06 | 1.1 |
| Qwen/Qwen2.5-1.5B | heldout_many | 32768 | 100 | 0.94 | 0.94 | 0.05 | 1.7 |
| Qwen/Qwen2.5-1.5B | many_random | 16384 | 100 | 0.90 | 0.90 | 0.10 | 1.0 |
| Qwen/Qwen2.5-1.5B | many_random | 32768 | 100 | 0.90 | 0.90 | 0.09 | 1.7 |
| Qwen/Qwen2.5-1.5B | many_similar | 16384 | 100 | 0.88 | 0.88 | 0.12 | 0.9 |
| Qwen/Qwen2.5-1.5B | many_similar | 32768 | 100 | 0.75 | 0.75 | 0.24 | 1.7 |
| Qwen/Qwen2.5-1.5B | multihop | 16384 | 100 | 0.20 | 0.20 | 0.74 | 1.1 |
| Qwen/Qwen2.5-1.5B | multihop | 32768 | 100 | 0.14 | 0.14 | 0.81 | 1.7 |
| Qwen/Qwen2.5-1.5B | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 0.8 |
| Qwen/Qwen2.5-1.5B | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.7 |
| Qwen/Qwen2.5-1.5B | updated | 16384 | 100 | 0.42 | 0.42 | 0.47 | 1.1 |
| Qwen/Qwen2.5-1.5B | updated | 32768 | 100 | 0.34 | 0.34 | 0.45 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | heldout_many | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.2 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_similar | 16384 | 100 | 0.99 | 0.99 | 0.01 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | many_similar | 32768 | 100 | 0.95 | 0.95 | 0.02 | 1.7 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 16384 | 100 | 0.99 | 0.99 | 0.01 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed1 | multihop | 32768 | 100 | 0.98 | 0.98 | 0.02 | 1.8 |
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
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | heldout_many | 32768 | 100 | 0.99 | 0.99 | 0.01 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_random | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_random | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_similar | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | many_similar | 32768 | 100 | 0.98 | 0.98 | 0.02 | 1.8 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.1 |
| Qwen/Qwen2.5-1.5B+adapter-Qwen_Qwen2.5-1.5B-seed2 | multihop | 32768 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
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
| jet-ai/Jet-Nemotron-2B+qk-restore | heldout_many | 16384 | 100 | 0.00 | 0.00 | 0.00 | 2.3 |
| jet-ai/Jet-Nemotron-2B+qk-restore | heldout_many | 32768 | 100 | 0.00 | 0.00 | 0.00 | 3.1 |
| jet-ai/Jet-Nemotron-2B+qk-restore | many_random | 16384 | 100 | 0.00 | 0.00 | 0.00 | 2.1 |
| jet-ai/Jet-Nemotron-2B+qk-restore | many_random | 32768 | 100 | 0.00 | 0.00 | 0.00 | 3.0 |
| jet-ai/Jet-Nemotron-2B+qk-restore | many_similar | 16384 | 100 | 0.00 | 0.00 | 0.00 | 1.5 |
| jet-ai/Jet-Nemotron-2B+qk-restore | many_similar | 32768 | 100 | 0.00 | 0.00 | 0.00 | 3.0 |
| jet-ai/Jet-Nemotron-2B+qk-restore | multihop | 16384 | 100 | 0.00 | 0.00 | 0.00 | 1.6 |
| jet-ai/Jet-Nemotron-2B+qk-restore | multihop | 32768 | 100 | 0.00 | 0.00 | 0.00 | 3.1 |
| jet-ai/Jet-Nemotron-2B+qk-restore | needle | 16384 | 100 | 0.00 | 0.00 | 0.00 | 1.7 |
| jet-ai/Jet-Nemotron-2B+qk-restore | needle | 32768 | 100 | 0.00 | 0.00 | 0.00 | 3.1 |
| jet-ai/Jet-Nemotron-2B+qk-restore | updated | 16384 | 100 | 0.00 | 0.00 | 0.00 | 1.6 |
| jet-ai/Jet-Nemotron-2B+qk-restore | updated | 32768 | 100 | 0.00 | 0.00 | 0.00 | 3.1 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 16384 | 100 | 1.00 | 1.00 | 0.00 | 2.0 |
| meta-llama/Llama-3.1-8B-Instruct | heldout_many | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.0 |
| meta-llama/Llama-3.1-8B-Instruct | many_random | 16384 | 100 | 0.99 | 0.99 | 0.01 | 1.8 |
| meta-llama/Llama-3.1-8B-Instruct | many_random | 32768 | 100 | 0.99 | 0.99 | 0.01 | 4.4 |
| meta-llama/Llama-3.1-8B-Instruct | many_similar | 16384 | 100 | 0.95 | 0.95 | 0.04 | 2.1 |
| meta-llama/Llama-3.1-8B-Instruct | many_similar | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.5 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 16384 | 100 | 0.63 | 0.63 | 0.32 | 2.3 |
| meta-llama/Llama-3.1-8B-Instruct | multihop | 32768 | 100 | 0.49 | 0.46 | 0.50 | 4.6 |
| meta-llama/Llama-3.1-8B-Instruct | needle | 16384 | 100 | 1.00 | 1.00 | 0.00 | 1.8 |
| meta-llama/Llama-3.1-8B-Instruct | needle | 32768 | 100 | 1.00 | 1.00 | 0.00 | 4.5 |
| meta-llama/Llama-3.1-8B-Instruct | updated | 16384 | 100 | 0.87 | 0.82 | 0.13 | 2.3 |
| meta-llama/Llama-3.1-8B-Instruct | updated | 32768 | 100 | 0.74 | 0.72 | 0.25 | 4.6 |

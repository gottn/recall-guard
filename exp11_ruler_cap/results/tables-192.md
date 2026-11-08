## Recall (contains) by reference length

| model | task | 16384 | 32768 |
|---|---|---:|---:|
| jet-ai/Jet-Nemotron-2B | ruler_niah_multiquery | 0.16 | 0.00 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multivalue | 0.22 | 0.02 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_niah_multiquery | 0.60 | 0.06 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_niah_multivalue | 0.72 | 0.08 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | ruler_niah_multiquery | 0.44 | 0.00 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | ruler_niah_multivalue | 0.48 | 0.02 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | ruler_niah_multiquery | 0.48 | 0.04 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | ruler_niah_multivalue | 0.52 | 0.02 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 | ruler_niah_multiquery | 0.58 | 0.12 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 | ruler_niah_multivalue | 0.56 | 0.12 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | ruler_niah_multiquery | 0.52 | 0.02 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | ruler_niah_multivalue | 0.74 | 0.10 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | ruler_niah_multiquery | 0.62 | 0.12 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | ruler_niah_multivalue | 0.82 | 0.10 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix | ruler_niah_multiquery | 0.50 | 0.02 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix | ruler_niah_multivalue | 0.62 | 0.08 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | ruler_niah_multiquery | 0.50 | 0.12 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | ruler_niah_multivalue | 0.56 | 0.22 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | ruler_niah_multiquery | 0.60 | 0.08 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | ruler_niah_multivalue | 0.70 | 0.08 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-realmix | ruler_niah_multiquery | 0.50 | 0.06 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-realmix | ruler_niah_multivalue | 0.48 | 0.02 |

## All rows

| model | task | ref tokens | n | contains | exact | stale | wall s |
|---|---|---:|---:|---:|---:|---:|---:|
| jet-ai/Jet-Nemotron-2B | ruler_niah_multiquery | 16384 | 50 | 0.16 | 0.00 | 0.00 | 14.0 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multiquery | 32768 | 50 | 0.00 | 0.00 | 0.00 | 14.4 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multivalue | 16384 | 50 | 0.22 | 0.00 | 0.00 | 14.3 |
| jet-ai/Jet-Nemotron-2B | ruler_niah_multivalue | 32768 | 50 | 0.02 | 0.00 | 0.00 | 16.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_niah_multiquery | 16384 | 50 | 0.60 | 0.00 | 0.00 | 11.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_niah_multiquery | 32768 | 50 | 0.06 | 0.00 | 0.00 | 10.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_niah_multivalue | 16384 | 50 | 0.72 | 0.00 | 0.00 | 9.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1 | ruler_niah_multivalue | 32768 | 50 | 0.08 | 0.00 | 0.00 | 10.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | ruler_niah_multiquery | 16384 | 50 | 0.44 | 0.00 | 0.00 | 18.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | ruler_niah_multiquery | 32768 | 50 | 0.00 | 0.00 | 0.00 | 16.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | ruler_niah_multivalue | 16384 | 50 | 0.48 | 0.00 | 0.00 | 17.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-budget | ruler_niah_multivalue | 32768 | 50 | 0.02 | 0.00 | 0.00 | 19.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | ruler_niah_multiquery | 16384 | 50 | 0.48 | 0.00 | 0.00 | 9.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | ruler_niah_multiquery | 32768 | 50 | 0.04 | 0.00 | 0.00 | 9.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | ruler_niah_multivalue | 16384 | 50 | 0.52 | 0.00 | 0.00 | 9.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-realmix | ruler_niah_multivalue | 32768 | 50 | 0.02 | 0.00 | 0.00 | 10.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 | ruler_niah_multiquery | 16384 | 50 | 0.58 | 0.00 | 0.00 | 9.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 | ruler_niah_multiquery | 32768 | 50 | 0.12 | 0.00 | 0.00 | 10.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 | ruler_niah_multivalue | 16384 | 50 | 0.56 | 0.00 | 0.00 | 9.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed1-syn1200 | ruler_niah_multivalue | 32768 | 50 | 0.12 | 0.00 | 0.00 | 10.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | ruler_niah_multiquery | 16384 | 50 | 0.52 | 0.00 | 0.00 | 19.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | ruler_niah_multiquery | 32768 | 50 | 0.02 | 0.00 | 0.00 | 18.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | ruler_niah_multivalue | 16384 | 50 | 0.74 | 0.00 | 0.00 | 17.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2 | ruler_niah_multivalue | 32768 | 50 | 0.10 | 0.00 | 0.00 | 18.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | ruler_niah_multiquery | 16384 | 50 | 0.62 | 0.00 | 0.00 | 9.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | ruler_niah_multiquery | 32768 | 50 | 0.12 | 0.00 | 0.00 | 10.7 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | ruler_niah_multivalue | 16384 | 50 | 0.82 | 0.00 | 0.00 | 9.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-budget | ruler_niah_multivalue | 32768 | 50 | 0.10 | 0.00 | 0.00 | 10.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix | ruler_niah_multiquery | 16384 | 50 | 0.50 | 0.00 | 0.00 | 9.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix | ruler_niah_multiquery | 32768 | 50 | 0.02 | 0.00 | 0.00 | 10.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix | ruler_niah_multivalue | 16384 | 50 | 0.62 | 0.00 | 0.00 | 9.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed2-realmix | ruler_niah_multivalue | 32768 | 50 | 0.08 | 0.00 | 0.00 | 10.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | ruler_niah_multiquery | 16384 | 50 | 0.50 | 0.00 | 0.00 | 18.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | ruler_niah_multiquery | 32768 | 50 | 0.12 | 0.00 | 0.00 | 18.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | ruler_niah_multivalue | 16384 | 50 | 0.56 | 0.00 | 0.00 | 17.4 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3 | ruler_niah_multivalue | 32768 | 50 | 0.22 | 0.00 | 0.00 | 18.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | ruler_niah_multiquery | 16384 | 50 | 0.60 | 0.00 | 0.00 | 18.1 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | ruler_niah_multiquery | 32768 | 50 | 0.08 | 0.00 | 0.00 | 18.9 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | ruler_niah_multivalue | 16384 | 50 | 0.70 | 0.00 | 0.00 | 17.6 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-budget | ruler_niah_multivalue | 32768 | 50 | 0.08 | 0.00 | 0.00 | 19.0 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-realmix | ruler_niah_multiquery | 16384 | 50 | 0.50 | 0.00 | 0.00 | 17.8 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-realmix | ruler_niah_multiquery | 32768 | 50 | 0.06 | 0.00 | 0.00 | 18.7 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-realmix | ruler_niah_multivalue | 16384 | 50 | 0.48 | 0.00 | 0.00 | 17.5 |
| jet-ai/Jet-Nemotron-2B+adapter-jet-ai_Jet-Nemotron-2B-seed3-realmix | ruler_niah_multivalue | 32768 | 50 | 0.02 | 0.00 | 0.00 | 18.9 |

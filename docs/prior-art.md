# Prior art check (deep research, 2026-10-16)

Verified by a 103-agent search-fetch-verify run (21 sources, 25 claims, 3-vote adversarial verification).
Each line below survived at least 2 of 3 verifiers. Use this before any write-up.

## Framing corrections to our own claims
- **"Exact base" is wrong wording.** Qwen2.5-1.5B is Jet-Nemotron-2B's *initialisation checkpoint*: PostNAS froze the
  MLPs during stage 1, but stage 2 trained the whole model (MLPs included) for 50B then 350B tokens
  (arXiv 2508.15884 §3.1). Say "the model it was converted from".
- **A long-context deficit in Jet-Nemotron-2B is already hinted at**, unpaired: Jet-Long (arXiv 2607.07740, Table 4)
  reports a 13-task RULER aggregate of 82.35 / 68.93 / 61.21 / 46.59 / 20.34 / 8.54 at 4K-128K, with no Qwen2.5 row and no
  per-subtask split. Our contribution is the pairing and the single-needle vs multi-key split, not the existence of a deficit.
- **Single-needle 1.00 at 32K is independently confirmed**: Attention Amnesia (arXiv 2606.11052) reports NIAH-Single-1 =
  100.0 at 32K-256K for the released Jet-Nemotron-2B; it runs no multi-key task and no base model.

## Published paired converted-vs-source comparisons (none at 32K with a multi-key split)
- RADLADS (arXiv 2505.03005): QRWKV7-7B RULER 39.7 / 26.1 / 16.5 at 4K / 8K / 16K vs teacher 69.7 at 16K; passkey reliable
  to ~8K vs 34K+. Pure RNN (0 softmax layers), aggregate only, max 16K, single needle also fails.
- LoLA (arXiv 2505.23666, Table 2): LoLCATs-8B+ vs Llama-3.1-8B RULER at 4K, MK1/2/3 = 12.8 / 1.4 / 0.4 vs 100 / 100 / 98;
  single needle also fails (0.6 at 4K). Its training-free fix reaches 97.4 on S-NIAH-1 while MK1/2/3 stay 39.4 / 11.6 / 7.6:
  published evidence at 4K that single-needle success is a weak proxy for multi-key recall.
- LoLCATs (arXiv 2410.10254, Table 21): Alpaca-linearised Llama-3-8B 0% on 8K passkey vs base 92-100% vs an identically
  LoRA-tuned full-attention control 100%. Trained control like ours; single needle only; <= 10K.
- **Counter-signal**: Lizard (arXiv 2507.09025, ACL 2026) keeps 50% softmax layers and reports RULER parity with its teacher
  to 32K (81.3 vs 80.5). Conversion-induced multi-key deficits are not universal; they depend on how few attention layers survive.

## Published repair with synthetic retrieval data
- LoLCATs App. B.5.2: 10K generated ~8K passkey samples used *as the linearising data* (during conversion, not post-hoc)
  recover 100% 8K passkey. No benchmark numbers, no transfer, no multi-key, does not extend to 10K.
- arXiv 2510.26912 (BabyLM 2025): "NIAH fine-tuning significantly harms commonsense" rests on a 1.1-point drop (51.5 to 50.4)
  for a 430M from-scratch Mamba+SWA hybrid trained at 4K; the large damage (-6.2) came from Based/SQuAD data. No converted
  model, nothing beyond 16K, no multi-key test. Does not contradict "ARC-Easy/HellaSwag unchanged within 0.02".
- Not found anywhere: post-hoc LoRA on ~1% of parameters repairing multi-key recall at 32K on an already-converted model,
  with transfer to an unseen template and unchanged general benchmarks.

## Added 2026-10-16 night (checked against arXiv search results, not full text)
- **Attention Amnesia (arXiv 2606.11052, June 2026; HKUST(GZ), UCL, Mistral, Tsinghua, SUTD).** Chain-of-thought SFT degrades
  long-range recall in hybrids (HypeNet, Jet-Nemotron); e.g. HypeNet-9B NIAH-S2 at 256K from 67.2 to 9.4. Cause attributed to
  W_Q / W_K drifting toward short-range patterns; fix "QK-Restore" (training-free: restore W_Q, W_K from the pre-SFT checkpoint).
  **This pre-empts the basic form of our step 2** ("fine-tuning silently breaks hybrid recall"). What remains open: ordinary
  (non-CoT) instruction SFT; whether our LoRA repair survives SFT; whether QK-Restore and the repair compose; the freeze rule.
  Note our repair trains q/k projections among others, which is consistent with their routing explanation.
- **When Synthetic Data Hurts (arXiv 2609.10750, Sept 2026).** Aggressive LoRA (rank 16-32) on synthetic skill-retrieval data for
  LLM agents overfits and forgets real data; mitigations compared (anchor, LwF, L2-init, EWC). Different task family (agent skill
  lookup, bi-encoder style) and they measure forgetting on retrieval tasks, not on LM/commonsense. Cite as the expected objection to
  synthetic-data fine-tuning; our ARC/HellaSwag/bpb numbers are the answer, and our +0.4% bpb is the honest cost.
- **Corrections to an AI-drafted related-work note seen on 2026-10-16:** RADLADS is Goldstein et al. (Recursal), not Hatamizadeh;
  Lizard is a linearisation of LLaMA-3-8B-Instruct trained at 2K that keeps 50% softmax layers and reports RULER parity to 32K,
  not an architecture trained from scratch with "perfect recall"; Jet-Nemotron is 2B, not 1.5B; numbered references like [109]
  were placeholders; Shivagunde et al. 2026 was not verified. The "numeric vs UUID" result is a boundary of the *repair's*
  training coverage, not a property of hybrid memory (the source model is also weak on UUIDs: 0.40); the multi-hop collapse was
  a data-induced shortcut removed by the v2 mix, and must be reported as such.

## What RULER would see
RULER's default suite has niah_multikey_1/2/3, multivalue and multiquery; in principle it detects the same pattern. No
per-subtask RULER breakdown is published for Jet-Nemotron, and nothing was found for Qwen3.5-4B, Falcon-H1 or Kimi Linear.
Consequence: the next run must include RULER's multi-key subtasks on the same models, before and after repair.

## Not covered by the verified claims
State-capacity bounds for gated-DeltaNet / linear attention (Stuffed Mamba, Mamba Modulation, Qwen3-Next reports) returned
no verified claim; search again before citing.

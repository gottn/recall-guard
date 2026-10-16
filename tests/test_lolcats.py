import math

import torch

from recall_guard.backends.lolcats import decode_state, decode_step, feature_map, prefill

W, H, D = 4, 2, 8  # window, heads, head dim


def their_prefill(q, k, v, fq, fk, wf):
    """lolcats-scaled get_masks + hybrid_attention_quadratic (linear_window_attention_tk.py), quadratic memory."""
    m = math.ceil(q.shape[2] / W)
    mask = torch.block_diag(*[torch.ones(W, W)] * m)
    mask = (mask + torch.roll(mask, -W, -1))[-q.shape[2]:, -k.shape[2]:]
    win, lin = torch.tril(mask).bool(), torch.tril(1 - mask).bool()
    s = (q @ k.transpose(-1, -2) * D**-0.5).masked_fill(~win, -1e8)
    a_sm = wf * torch.exp(s - s.amax(-1, keepdim=True))
    a_ln = (fq @ fk.transpose(-1, -2)).masked_fill(~lin, 0)
    return (a_sm + a_ln) @ v / (a_sm.sum(-1, keepdim=True) + a_ln.sum(-1, keepdim=True))


def sliding(q, k, v, fq, fk, wf):
    """Their decode rule for the last query: softmax over the last W keys, linear over all older ones."""
    s = q @ k[:, :, -W:].transpose(-1, -2) * D**-0.5
    a = wf * torch.exp(s - s.amax(-1, keepdim=True))
    num = a @ v[:, :, -W:] + fq @ fk[:, :, :-W].transpose(-1, -2) @ v[:, :, :-W]
    return num / (a.sum(-1, keepdim=True) + (fq @ fk[:, :, :-W].transpose(-1, -2)).sum(-1, keepdim=True))


def test_prefill_and_decode_match_the_quadratic_reference():
    g = torch.Generator().manual_seed(0)
    wq, wk = torch.randn(H, D, 3, generator=g), torch.randn(H, D, 3, generator=g)
    wf = torch.sigmoid(torch.randn(1, H, 1, 1, generator=g))
    for n in (13, 12, 3):  # padded, block-aligned, shorter than a window
        q, k, v = (torch.randn(1, H, n + 5, D, generator=g) for _ in range(3))
        fq, fk = feature_map(q, wq), feature_map(k, wk)
        if n > W:  # their mask is degenerate for a single block
            ref = their_prefill(q[:, :, :n], k[:, :, :n], v[:, :, :n], fq[:, :, :n], fk[:, :, :n], wf)
            assert torch.allclose(prefill(q[:, :, :n], k[:, :, :n], v[:, :, :n], fq[:, :, :n], fk[:, :, :n], wf, W), ref, atol=1e-5)
        state = decode_state(k[:, :, :n], v[:, :, :n], fk[:, :, :n], W)
        for t in range(n, n + 5):
            y, state = decode_step(q[:, :, t:t + 1], k[:, :, t:t + 1], v[:, :, t:t + 1], fq[:, :, t:t + 1], state, wf, wk, W)
            ref = sliding(q[:, :, t:t + 1], k[:, :, :t + 1], v[:, :, :t + 1], fq[:, :, t:t + 1], fk[:, :, :t + 1], wf)
            assert torch.allclose(y, ref, atol=1e-5)


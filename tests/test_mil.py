import torch
from transformers import AutoModelForCausalLM, LlamaConfig

from recall_guard.backends.mil import cached_mixer_layer, causal_conv1d_torch


def test_causal_conv1d_torch_matches_a_loop():
    g = torch.Generator().manual_seed(0)
    x, w, b = torch.randn(2, 3, 6, generator=g), torch.randn(3, 4, generator=g), torch.randn(3, generator=g)
    ref = torch.stack([b + sum(w[:, k] * x[..., t - 3 + k] for k in range(4) if t - 3 + k >= 0) for t in range(6)], -1)
    assert torch.allclose(causal_conv1d_torch(x, w, b), ref, atol=1e-6)
    assert torch.allclose(causal_conv1d_torch(x, w, b, "silu"), torch.nn.functional.silu(ref), atol=1e-6)


class CumsumMixer(torch.nn.Module):
    """Toy recurrent layer with the MambaDecoderLayer call contract: a running sum of a projection."""

    def __init__(self, d: int, layer_idx: int):
        super().__init__()
        self.proj, self.layer_idx = torch.nn.Linear(d, d), layer_idx

    def forward(self, h: torch.Tensor, inference_params: object = None) -> torch.Tensor:
        y = self.proj(h).cumsum(1)
        if inference_params is not None:
            y = y + inference_params.key_value_memory_dict.get(self.layer_idx, 0)
            inference_params.key_value_memory_dict[self.layer_idx] = y[:, -1:]
        return h + y


def test_cached_decode_matches_full_recompute():
    torch.manual_seed(0)
    cfg = LlamaConfig(hidden_size=32, intermediate_size=64, num_hidden_layers=4, num_attention_heads=4,
                      num_key_value_heads=2, vocab_size=50, max_position_embeddings=64, eos_token_id=None)
    model = AutoModelForCausalLM.from_config(cfg, attn_implementation="sdpa").eval()
    for i in (0, 2):  # layer 0 recurrent: HF reads the cache length from it
        model.model.layers[i] = cached_mixer_layer(CumsumMixer)(32, i)
    ids = torch.randint(0, 50, (1, 7))
    with torch.no_grad():
        out = model.generate(ids, max_new_tokens=8, do_sample=False, pad_token_id=0)
        ref = ids
        for _ in range(8):
            ref = torch.cat([ref, model(ref, use_cache=False).logits[:, -1:].argmax(-1)], 1)
    assert out.shape[1] == 15
    assert torch.equal(out, ref)
    assert model(ids, use_cache=True).past_key_values.get_seq_length() == 7  # read from layer 0, a recurrent one

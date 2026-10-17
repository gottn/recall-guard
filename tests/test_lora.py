import torch

from recall_guard.backends import lora


class Tiny(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_proj = torch.nn.Linear(8, 8)
        self.mlp = torch.nn.Module()
        self.mlp.up_proj = torch.nn.Linear(8, 8)


def test_inject_train_merge_roundtrip(tmp_path):
    torch.manual_seed(0)
    m = Tiny()
    assert lora.target_names(m) == ("q_proj",)
    assert lora.inject(m, ("q_proj",), r=2, alpha=4) == ("q_proj",)
    assert [n for n, p in m.named_parameters() if p.requires_grad] == ["q_proj.A", "q_proj.B"]
    x = torch.randn(3, 8)
    with torch.no_grad():
        m.q_proj.B.copy_(torch.randn(8, 2))  # B starts at zero; give the adapter an effect
    y_adapter = m.q_proj(x)
    assert lora.save(m, str(tmp_path), 2, 4) == 2
    fresh = Tiny()
    fresh.q_proj.load_state_dict(m.q_proj.base.state_dict())
    assert lora.merge(fresh, str(tmp_path)) == 1
    assert torch.allclose(fresh.q_proj(x), y_adapter, atol=1e-5)


def test_attach_matches_merge(tmp_path):
    torch.manual_seed(1)
    m = Tiny()
    lora.inject(m, ("q_proj",), r=2, alpha=4)
    with torch.no_grad():
        m.q_proj.B.copy_(torch.randn(8, 2))
    lora.save(m, str(tmp_path), 2, 4)
    x = torch.randn(2, 8)
    merged, attached = Tiny(), Tiny()
    for t in (merged, attached):
        t.q_proj.load_state_dict(m.q_proj.base.state_dict())
    lora.merge(merged, str(tmp_path))
    assert lora.attach(attached, str(tmp_path)) == 1
    assert torch.allclose(merged.q_proj(x), attached.q_proj(x), atol=1e-5)


def test_wrapped_linear_still_exposes_weight():
    m = Tiny()
    lora.inject(m, ("q_proj",), r=2, alpha=4)
    assert m.q_proj.weight is m.q_proj.base.weight

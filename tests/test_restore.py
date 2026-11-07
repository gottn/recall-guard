import torch

from recall_guard.backends import restore

JET = {
    "model.layers.0.self_attn.q_proj.weight": (1152, 1536),  # linear-attention block, same name, other shape
    "model.layers.14.self_attn.q_proj.weight": (1536, 1536),
    "model.layers.14.self_attn.q_proj.bias": (1536,),
    "model.layers.14.self_attn.k_proj.weight": (256, 1536),
    "model.layers.14.self_attn.v_proj.weight": (256, 1536),
    "model.layers.14.mlp.up_proj.weight": (8960, 1536),
    "model.layers.19.self_attn.k_proj.weight": (256, 1536),
    "model.layers.20.self_attn.k_proj.weight": (256, 1536),
}
QWEN = {**JET, "model.layers.0.self_attn.q_proj.weight": (1536, 1536)}


def test_restorable_takes_qk_with_matching_shape_only():
    assert restore.restorable(JET, QWEN) == (
        "model.layers.14.self_attn.k_proj.weight",
        "model.layers.14.self_attn.q_proj.bias",
        "model.layers.14.self_attn.q_proj.weight",
        "model.layers.19.self_attn.k_proj.weight",
        "model.layers.20.self_attn.k_proj.weight",
    )


def test_pattern_narrows_layers():
    names = restore.restorable(JET, QWEN, r"layers\.1[49]\.self_attn\.[qk]_proj")
    assert {n.split(".")[2] for n in names} == {"14", "19"}


def test_multimodal_checkpoint_keys_match_the_text_model_names():
    model = {"model.layers.15.mlp.down_proj.weight": (1024, 3584), "model.layers.14.mlp.down_proj.weight": (1024, 3584)}
    ckpt = {"model.language_model.layers.15.mlp.down_proj.weight": (1024, 3584), "model.visual.blocks.0.mlp.fc2.weight": (768, 3072)}
    assert restore.restorable(model, ckpt, r"layers\.1[59]\.mlp\.down_proj") == ("model.layers.15.mlp.down_proj.weight",)


def tiny(seed: int) -> torch.nn.Module:
    torch.manual_seed(seed)
    m = torch.nn.Module()
    m.down_proj = torch.nn.Linear(4, 3, bias=False)
    return m


def test_apply_moves_a_weight_part_of_the_way_in_place():
    src = torch.randn(3, 4)
    m, w = tiny(0), tiny(0).down_proj.weight.detach()
    restore.apply(m, "down_proj.weight", src, 0.25)
    assert torch.allclose(m.down_proj.weight, w + 0.25 * (src - w))
    restore.apply(m, "down_proj.weight", src)
    assert torch.equal(m.down_proj.weight, src)


def test_phase_hooks_change_only_prompt_calls_or_only_one_token_calls():
    src, prompt, token = torch.randn(3, 4), torch.randn(1, 5, 4), torch.randn(1, 1, 4)
    base, full = tiny(0), tiny(0)
    restore.apply(full, "down_proj.weight", src)
    for phase, changed, same in (("prompt", prompt, token), ("answer", token, prompt)):
        m = tiny(0)
        restore.apply(m, "down_proj.weight", src, 1.0, phase)
        assert torch.allclose(m.down_proj(changed), full.down_proj(changed), atol=1e-6)
        assert torch.equal(m.down_proj(same), base.down_proj(same))
        assert torch.equal(m.down_proj.weight, base.down_proj.weight)

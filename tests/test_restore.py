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

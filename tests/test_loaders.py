from recall_guard.backends.loaders import loader_for


def test_registered_prefixes_route_to_their_loader():
    assert loader_for("JunxiongWang/Llama3.1-Mamba2-8B-dpo") == "recall_guard.backends.mil:load"
    assert loader_for("hazyresearch/lolcats-llama-3.1-8b-ft-lora") == "recall_guard.backends.lolcats:load"
    assert loader_for("Qwen/Qwen2.5-1.5B") == ""
    assert loader_for("meta-llama/Llama-3.1-8B") == ""

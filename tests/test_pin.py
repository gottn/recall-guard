"""hf.pin_autotune: every Triton-autotuned kernel keeps its first configuration (exp13, exp14)."""
import sys
import types

import pytest

from recall_guard.backends import hf


def test_pin_keeps_the_first_configuration(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: list[tuple] = []
    fake = types.ModuleType("triton")
    fake.autotune = lambda configs, key, **kw: seen.append((configs, key, kw)) or "decorator"
    monkeypatch.setitem(sys.modules, "triton", fake)
    assert hf.pin_autotune() is True
    assert fake.autotune(configs=["a", "b", "c"], key=["K"], use_cuda_graph=False) == "decorator"  # fla's call form
    assert fake.autotune(["x", "y"], ["K"]) == "decorator"
    assert seen == [(["a"], ["K"], {"use_cuda_graph": False}), (["x"], ["K"], {})]
    pinned = fake.autotune
    assert hf.pin_autotune() is True and fake.autotune is pinned  # a second call does not wrap twice


def test_pin_without_triton(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setitem(sys.modules, "triton", None)  # makes `import triton` raise ImportError
    assert hf.pin_autotune() is False

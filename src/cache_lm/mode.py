from __future__ import annotations

from typing import Literal

from cache_lm.env import get_env

Mode = Literal["stub", "llm"]


def get_mode() -> Mode:
    value = (get_env("CACHE_LM_MODE", "stub") or "stub").lower()
    if value in ("llm", "stub"):
        return value  # type: ignore[return-value]
    return "stub"

from __future__ import annotations

import os


def get_env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name)
    if value is None:
        return default
    value = value.strip()
    if value == "":
        return default
    return value

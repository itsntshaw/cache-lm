from __future__ import annotations

import os
from pathlib import Path
import sys


def pytest_configure() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    src = repo_root / "src"
    sys.path.insert(0, str(src))


def pytest_runtest_setup(item) -> None:
    if item.get_closest_marker("integration") is None:
        os.environ["CACHE_LM_MODE"] = "stub"
        os.environ["CACHE_LM_ROUTER_MODE"] = "rules"
        os.environ["CACHE_LM_EXPERT_EXECUTION"] = "sequential"

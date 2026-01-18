import os
from pathlib import Path
import subprocess
import sys


def test_module_help_exits_zero():
    repo_root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()
    env["PYTHONPATH"] = str(repo_root / "src") + os.pathsep + env.get(
        "PYTHONPATH", "")

    result = subprocess.run(
        [sys.executable, "-m", "cache_lm", "--help"],
        env=env,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage" in result.stdout.lower()

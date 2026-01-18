from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cache_lm.hashing import sha256_bytes


def repo_root() -> Path:
    # src/cache_lm/manual.py -> repo root is two parents up from src/
    return Path(__file__).resolve().parents[2]


def default_manual_path() -> Path:
    return repo_root() / "data" / "operations_manual.md"


@dataclass(frozen=True)
class Manual:
    path: Path
    bytes: bytes
    text: str
    sha256: str


_CACHED_MANUAL: Manual | None = None


def load_manual(*, path: Path | None = None) -> Manual:
    manual_path = (path or default_manual_path()).resolve()
    manual_bytes = manual_path.read_bytes()
    manual_text = manual_bytes.decode("utf-8")
    manual_sha256 = sha256_bytes(manual_bytes)
    return Manual(
        path=manual_path,
        bytes=manual_bytes,
        text=manual_text,
        sha256=manual_sha256,
    )


def get_manual(*, path: Path | None = None, use_cache: bool = True) -> Manual:
    global _CACHED_MANUAL

    if not use_cache:
        return load_manual(path=path)

    requested_path = (path or default_manual_path()).resolve()

    if _CACHED_MANUAL is None:
        _CACHED_MANUAL = load_manual(path=requested_path)

    if _CACHED_MANUAL.path != requested_path:
        _CACHED_MANUAL = load_manual(path=requested_path)

    return _CACHED_MANUAL

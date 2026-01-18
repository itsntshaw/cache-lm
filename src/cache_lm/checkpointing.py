from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
import sqlite3

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.serde.jsonplus import JsonPlusSerializer


def inmemory_checkpointer() -> InMemorySaver:
    return InMemorySaver(serde=JsonPlusSerializer(pickle_fallback=True))


@contextmanager
def sqlite_checkpointer(db_path: str) -> Iterator[object]:
    try:
        from langgraph.checkpoint.sqlite import SqliteSaver
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "SQLite checkpointer support requires `langgraph-checkpoint-sqlite` "
            "(install dependencies and retry).") from e

    path = Path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), check_same_thread=False)
    try:
        yield SqliteSaver(
            conn,
            serde=JsonPlusSerializer(pickle_fallback=True),
        )
    finally:
        conn.close()

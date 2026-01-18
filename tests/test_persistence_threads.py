from __future__ import annotations

import json

from langchain_core.messages import HumanMessage

from cache_lm.checkpointing import inmemory_checkpointer
from cache_lm.graph import create_graph
from cache_lm.manual import get_manual
from cache_lm.prompts import MANUAL_BEGIN


def test_thread_persistence_accumulates_messages_and_keeps_prefix_stable(
) -> None:
    checkpointer = inmemory_checkpointer()
    compiled = create_graph().compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "t1"}}

    first = compiled.invoke(
        {"messages": [HumanMessage(content="What is the API limit?")]},
        config=config,
    )
    second = compiled.invoke(
        {"messages": [HumanMessage(content="Summarize that in steps.")]},
        config=config,
    )

    assert len(first["messages"]) == 2
    assert len(second["messages"]) == 4

    assert first["manual_sha256"] == second["manual_sha256"]
    assert first["system_prefix_hash"] == second["system_prefix_hash"]

    manual = get_manual().text
    snapshot = compiled.get_state(config)
    stored = snapshot.values
    assert len(stored["messages"]) == 4
    assert MANUAL_BEGIN not in json.dumps(stored, default=str)
    assert manual not in json.dumps(stored, default=str)

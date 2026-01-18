from __future__ import annotations

import types

from langchain_core.messages import HumanMessage

from cache_lm.graph import create_graph


class _FakeChunk:

    def __init__(self, content: str):
        self.content = content


class _FakeStreamingChatModel:

    def stream(self, messages):
        yield _FakeChunk("ok")


def test_parallel_execution_in_llm_mode_passes_messages_to_experts(
        monkeypatch):
    monkeypatch.setenv("CACHE_LM_MODE", "llm")
    monkeypatch.setenv("CACHE_LM_EXPERT_EXECUTION", "parallel")
    monkeypatch.setenv("CACHE_LM_ROUTER_MODE", "rules")

    # Make sure this test stays offline: replace the real model constructor.
    monkeypatch.setattr(
        "cache_lm.experts.create_chat_model",
        lambda streaming: _FakeStreamingChatModel(),
    )

    graph = create_graph().compile()
    result = graph.invoke({
        "messages": [
            HumanMessage(
                content=
                "Can I do approvals in chat, and what are the minimum logging expectations?"
            )
        ]
    })

    assert "expert_outputs" in result
    assert any(result["expert_outputs"].values())

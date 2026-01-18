from __future__ import annotations

from langchain_core.messages import HumanMessage

from cache_lm.graph import create_graph


def test_parallel_fanout_merges_expert_outputs_without_conflicts(
        monkeypatch) -> None:
    monkeypatch.setenv("CACHE_LM_EXPERT_EXECUTION", "parallel")

    graph = create_graph().compile()
    result = graph.invoke({
        "messages": [
            HumanMessage(
                content=
                "Can I do this under policy, and what are the API limits?")
        ]
    })

    assert "compliance_auditor" in result["expert_outputs"]
    assert "technical_specialist" in result["expert_outputs"]
    assert "support_concierge" not in result["expert_outputs"]

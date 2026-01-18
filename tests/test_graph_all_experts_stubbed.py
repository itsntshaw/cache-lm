from __future__ import annotations

from langchain_core.messages import HumanMessage

from cache_lm.graph import create_graph


def test_graph_can_run_all_three_experts_in_one_turn_stubbed() -> None:
    compiled = create_graph().compile()
    result = compiled.invoke({
        "messages": [
            HumanMessage(
                content=
                "Can I do this under policy, what are the API limits, and summarize in steps?"
            )
        ]
    })

    assert set(result["expert_outputs"].keys()) == {
        "compliance_auditor",
        "technical_specialist",
        "support_concierge",
    }

    response = result["response"]
    assert "Compliance Auditor (stub)" in response
    assert "Technical Specialist (stub)" in response
    assert "Support Concierge (stub)" in response

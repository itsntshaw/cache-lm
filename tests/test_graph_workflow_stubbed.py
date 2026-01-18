from __future__ import annotations

from langchain_core.messages import HumanMessage

from cache_lm.graph import create_graph
from cache_lm.manual import get_manual
from cache_lm.prompts import MANUAL_BEGIN
from cache_lm.router import route_experts_rules


def test_rules_router_selects_expected_expert() -> None:
    assert [
        t["expert"]
        for t in route_experts_rules("What is the API limit?").tasks
    ] == ["technical_specialist"]
    assert [
        t["expert"]
        for t in route_experts_rules("Can I do this under policy?").tasks
    ] == ["compliance_auditor"]
    assert [
        t["expert"] for t in route_experts_rules(
            "Give me step-by-step instructions.").tasks
    ] == ["support_concierge"]


def test_rules_router_can_select_multiple_experts_for_mixed_query() -> None:
    pending = route_experts_rules(
        "Can I do this under policy, and what are the API limits?").tasks
    experts = {t["expert"] for t in pending}
    assert "compliance_auditor" in experts
    assert "technical_specialist" in experts


def test_graph_runs_and_does_not_store_manual_in_messages() -> None:
    manual = get_manual(use_cache=False)
    compiled = create_graph().compile()
    result = compiled.invoke(
        {"messages": [HumanMessage(content="What is the API limit?")]})

    assert result["manual_sha256"] == manual.sha256
    assert result["system_prefix_hash"]
    assert result["response"]

    for message in result["messages"]:
        assert MANUAL_BEGIN not in message.content

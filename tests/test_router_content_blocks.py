from __future__ import annotations

from langchain_core.messages import HumanMessage

from cache_lm.router import router_node


def test_router_node_accepts_list_content_blocks() -> None:
    state = {
        "messages": [
            HumanMessage(content=[{
                "type": "text",
                "text": "Hi, can I do this under policy?"
            }])
        ],
    }
    result = router_node(state)  # type: ignore[arg-type]
    experts = [task["expert"] for task in result["pending_tasks"]]
    assert "compliance_auditor" in experts

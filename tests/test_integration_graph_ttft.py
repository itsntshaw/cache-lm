from __future__ import annotations

import os

from langchain_core.messages import HumanMessage
import pytest

from cache_lm.graph import create_graph


def _get_required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        pytest.skip(f"{name} is not set")
    return value


@pytest.mark.integration
def test_graph_runs_with_llm_and_records_ttft() -> None:
    if os.environ.get("RUN_LLM_TESTS") != "1":
        pytest.skip("RUN_LLM_TESTS != 1")

    _get_required_env("OPENAI_BASE_URL")
    _get_required_env("OPENAI_API_KEY")
    _get_required_env("OPENAI_MODEL")

    os.environ["CACHE_LM_MODE"] = "llm"

    compiled = create_graph().compile()
    result = compiled.invoke({
        "messages": [
            HumanMessage(
                content=
                "Can I do this under policy, and what are the API limits?")
        ]
    })

    assert "compliance_auditor" in result["expert_outputs"]
    assert "technical_specialist" in result["expert_outputs"]

    ttft = result["ttft_ms_by_expert"]
    latency = result["latency_ms_by_expert"]
    assert ttft["compliance_auditor"] > 0
    assert ttft["technical_specialist"] > 0
    assert latency["compliance_auditor"] >= ttft["compliance_auditor"]
    assert latency["technical_specialist"] >= ttft["technical_specialist"]

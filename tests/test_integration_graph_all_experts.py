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
def test_graph_exercises_all_experts_with_llm() -> None:
    if os.environ.get("RUN_LLM_TESTS") != "1":
        pytest.skip("RUN_LLM_TESTS != 1")

    _get_required_env("OPENAI_BASE_URL")
    _get_required_env("OPENAI_API_KEY")
    _get_required_env("OPENAI_MODEL")

    os.environ["CACHE_LM_MODE"] = "llm"

    old_max_tokens = os.environ.get("OPENAI_MAX_TOKENS")
    old_temperature = os.environ.get("OPENAI_TEMPERATURE")
    os.environ["OPENAI_MAX_TOKENS"] = "64"
    os.environ["OPENAI_TEMPERATURE"] = "0"
    try:
        compiled = create_graph().compile()
        result = compiled.invoke({
            "messages": [
                HumanMessage(
                    content=
                    "Can I do this under policy, what are the API limits, and summarize in steps?"
                )
            ]
        })
    finally:
        if old_max_tokens is None:
            os.environ.pop("OPENAI_MAX_TOKENS", None)
        else:
            os.environ["OPENAI_MAX_TOKENS"] = old_max_tokens
        if old_temperature is None:
            os.environ.pop("OPENAI_TEMPERATURE", None)
        else:
            os.environ["OPENAI_TEMPERATURE"] = old_temperature

    assert set(result["expert_outputs"].keys()) == {
        "compliance_auditor",
        "technical_specialist",
        "support_concierge",
    }

    ttft = result["ttft_ms_by_expert"]
    latency = result["latency_ms_by_expert"]
    for expert in result["expert_outputs"].keys():
        assert ttft[expert] > 0
        assert latency[expert] >= ttft[expert]

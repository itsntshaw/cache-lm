from __future__ import annotations

import os

import pytest

from cache_lm.router_llm import llm_route_experts


def _get_required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        pytest.skip(f"{name} is not set")
    return value


@pytest.mark.integration
def test_llm_router_selects_expected_experts_for_mixed_query() -> None:
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
        decision = llm_route_experts(
            user_input=
            "Can I do this under policy, what are the API limits, and summarize in steps?",
            messages=[],
        )
    finally:
        if old_max_tokens is None:
            os.environ.pop("OPENAI_MAX_TOKENS", None)
        else:
            os.environ["OPENAI_MAX_TOKENS"] = old_max_tokens
        if old_temperature is None:
            os.environ.pop("OPENAI_TEMPERATURE", None)
        else:
            os.environ["OPENAI_TEMPERATURE"] = old_temperature

    experts = [t["expert"] for t in decision.tasks]

    assert "compliance_auditor" in experts
    assert "technical_specialist" in experts
    assert len(experts) <= 3

    ordered = [
        e for e in
        ["compliance_auditor", "technical_specialist", "support_concierge"]
        if e in experts
    ]
    assert experts == ordered

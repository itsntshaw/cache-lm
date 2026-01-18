from __future__ import annotations

import time

from cache_lm.llm import create_chat_model
from cache_lm.manual import get_manual
from cache_lm.message_text import message_role
from cache_lm.message_text import message_to_text
from cache_lm.mode import get_mode
from cache_lm.prompts import build_messages
from cache_lm.prompts import to_langchain_messages
from cache_lm.state import Expert
from cache_lm.state import State


def _append_expert_output(
    state: State,
    *,
    expert: Expert,
    output: str,
    ttft_ms: float | None,
    latency_ms: float | None,
) -> dict[str, object]:
    update: dict[str, object] = {"expert_outputs": {expert: output}}
    if ttft_ms is not None:
        update["ttft_ms_by_expert"] = {expert: ttft_ms}
    if latency_ms is not None:
        update["latency_ms_by_expert"] = {expert: latency_ms}
    return update


def _task_query_from_state(state: State) -> str:
    task = state.get("task") or state.get("current_task") or {}
    if isinstance(task, dict):
        query = task.get("query")
        if isinstance(query, str):
            return query
    return ""


def _prepare_history_and_user_input(
    *,
    state_messages: list,
    user_input: str,
) -> tuple[list, str]:
    if not state_messages:
        return [], user_input
    last = state_messages[-1]
    if message_role(last) == "user" and message_to_text(last) == user_input:
        return state_messages[:-1], user_input
    return state_messages, user_input


def _history_as_chat_messages(history_messages: list) -> list[dict]:
    converted: list[dict] = []
    for message in history_messages:
        role = message_role(message)
        if role == "user":
            converted.append({
                "role": "user",
                "content": message_to_text(message)
            })
        elif role == "assistant":
            converted.append({
                "role": "assistant",
                "content": message_to_text(message)
            })
    return converted


def _call_expert_llm(
    *,
    expert: Expert,
    query: str,
    history_messages: list,
) -> tuple[str, float, float]:
    manual = get_manual()
    prompt_messages = build_messages(
        expert=expert,
        user_input=query,
        history=_history_as_chat_messages(history_messages) or None,
        manual_text=manual.text,
    )
    lc_messages = to_langchain_messages(prompt_messages)

    model = create_chat_model(streaming=True)

    start = time.perf_counter()
    first_token_time: float | None = None
    parts: list[str] = []
    for chunk in model.stream(lc_messages):
        chunk_text = chunk.content
        if isinstance(chunk_text, str) and chunk_text:
            if first_token_time is None:
                first_token_time = time.perf_counter()
            parts.append(chunk_text)

    end = time.perf_counter()
    if first_token_time is None:
        first_token_time = end

    content = "".join(parts).strip()
    ttft_ms = (first_token_time - start) * 1000.0
    latency_ms = (end - start) * 1000.0
    return content, ttft_ms, latency_ms


def _stub_output(expert_label: str, query: str) -> str:
    return (
        f"{expert_label} (stub): I will answer from the manual once LLM calls are "
        f"wired in. Query: {query}")


def technical_specialist_node(state: State) -> dict[str, object]:
    query = _task_query_from_state(state)
    if get_mode() != "llm":
        return _append_expert_output(
            state,
            expert="technical_specialist",
            output=_stub_output("Technical Specialist", query),
            ttft_ms=None,
            latency_ms=None,
        )

    history, user_input = _prepare_history_and_user_input(
        state_messages=list(state.get("messages", [])),
        user_input=query,
    )
    content, ttft_ms, latency_ms = _call_expert_llm(
        expert="technical_specialist",
        query=user_input,
        history_messages=history,
    )
    return _append_expert_output(
        state,
        expert="technical_specialist",
        output=content,
        ttft_ms=ttft_ms,
        latency_ms=latency_ms,
    )


def compliance_auditor_node(state: State) -> dict[str, object]:
    query = _task_query_from_state(state)
    if get_mode() != "llm":
        return _append_expert_output(
            state,
            expert="compliance_auditor",
            output=_stub_output("Compliance Auditor", query),
            ttft_ms=None,
            latency_ms=None,
        )

    history, user_input = _prepare_history_and_user_input(
        state_messages=list(state.get("messages", [])),
        user_input=query,
    )
    content, ttft_ms, latency_ms = _call_expert_llm(
        expert="compliance_auditor",
        query=user_input,
        history_messages=history,
    )
    return _append_expert_output(
        state,
        expert="compliance_auditor",
        output=content,
        ttft_ms=ttft_ms,
        latency_ms=latency_ms,
    )


def support_concierge_node(state: State) -> dict[str, object]:
    query = _task_query_from_state(state)
    if get_mode() != "llm":
        return _append_expert_output(
            state,
            expert="support_concierge",
            output=_stub_output("Support Concierge", query),
            ttft_ms=None,
            latency_ms=None,
        )

    history, user_input = _prepare_history_and_user_input(
        state_messages=list(state.get("messages", [])),
        user_input=query,
    )
    content, ttft_ms, latency_ms = _call_expert_llm(
        expert="support_concierge",
        query=user_input,
        history_messages=history,
    )
    return _append_expert_output(
        state,
        expert="support_concierge",
        output=content,
        ttft_ms=ttft_ms,
        latency_ms=latency_ms,
    )

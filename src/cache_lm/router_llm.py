from __future__ import annotations

import json
import re

from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage

from cache_lm.llm import create_chat_model
from cache_lm.message_text import message_role
from cache_lm.message_text import message_to_text
from cache_lm.state import Expert
from cache_lm.state import ExpertTask
from cache_lm.state import RoutingDecision

_ORDERED_EXPERTS: list[Expert] = [
    "compliance_auditor",
    "technical_specialist",
    "support_concierge",
]


def _system_router_prompt() -> str:
    return "\n".join([
        "You are a router for a banking assistant.",
        "Decide which specialist expert(s) should answer the user's request.",
        "",
        "Experts:",
        "- compliance_auditor: policy/regulation/can-cannot/allowed/prohibited questions",
        "- technical_specialist: API limits, specs, errors, troubleshooting questions",
        "- support_concierge: step-by-step procedures, summaries, user guidance",
        "",
        "Rules:",
        "- Return JSON ONLY (no prose, no markdown).",
        "- Output schema: {\"tasks\":[{\"expert\":\"<name>\",\"query\":\"<string>\"}, ...]}",
        "- tasks length: 1 to 3",
        "- expert must be one of: compliance_auditor, technical_specialist, support_concierge",
        "- If multiple experts are needed, include multiple tasks.",
        "- Prefer keeping the same query string for all tasks unless rewriting is necessary.",
        "- Prefer deterministic ordering: compliance_auditor, technical_specialist, support_concierge.",
        "- If unsure, choose support_concierge.",
    ])


def _render_history(messages: list, *, max_messages: int) -> str:
    lines: list[str] = []
    for message in messages[-max_messages:]:
        role = message_role(message)
        if role not in ("user", "assistant"):
            continue
        content = message_to_text(message).strip()
        if not content:
            continue
        prefix = "USER" if role == "user" else "ASSISTANT"
        lines.append(f"{prefix}: {content}")
    return "\n".join(lines)


def _extract_json_object(text: str) -> str:
    stripped = text.strip()
    match = re.search(r"\{.*\}", stripped, flags=re.DOTALL)
    if match:
        return match.group(0)
    return stripped


def _normalize_tasks(
    tasks: list[object],
    *,
    user_input: str,
) -> list[ExpertTask]:
    deduped: dict[Expert, ExpertTask] = {}
    for item in tasks:
        if not isinstance(item, dict):
            continue
        expert = item.get("expert")
        if expert not in _ORDERED_EXPERTS:
            continue
        query = item.get("query")
        if not isinstance(query, str) or not query.strip():
            query = user_input
        deduped[expert] = {
            "expert": expert,
            "query": query,
        }

    ordered: list[ExpertTask] = []
    for expert in _ORDERED_EXPERTS:
        if expert in deduped:
            ordered.append(deduped[expert])
    return ordered[:3]


def parse_routing_json(
    *,
    model_text: str,
    user_input: str,
) -> RoutingDecision | None:
    try:
        obj = json.loads(_extract_json_object(model_text))
    except json.JSONDecodeError:
        return None
    if not isinstance(obj, dict):
        return None
    tasks = obj.get("tasks")
    if not isinstance(tasks, list):
        return None
    normalized = _normalize_tasks(tasks, user_input=user_input)
    if not normalized:
        return None
    return RoutingDecision(tasks=normalized)


def llm_route_experts(
    *,
    user_input: str,
    messages: list,
    max_history_messages: int = 6,
) -> RoutingDecision:
    history_text = _render_history(messages, max_messages=max_history_messages)
    prompt = "\n\n".join([
        f"User input:\n{user_input}",
        f"Recent conversation:\n{history_text}" if history_text else "",
    ]).strip()

    model = create_chat_model(streaming=False)
    response = model.invoke([
        SystemMessage(content=_system_router_prompt()),
        HumanMessage(content=prompt),
    ])
    decision = parse_routing_json(
        model_text=message_to_text(response),
        user_input=user_input,
    )
    if decision is None:
        raise ValueError("Router model did not return valid routing JSON.")
    return decision

from __future__ import annotations

from typing import Literal

from cache_lm.env import get_env
from cache_lm.message_text import message_to_text
from cache_lm.mode import get_mode
from cache_lm.router_llm import llm_route_experts
from cache_lm.state import Expert
from cache_lm.state import ExpertTask
from cache_lm.state import RoutingDecision
from cache_lm.state import State

RouterMode = Literal["rules", "llm"]


def _wants_compliance(text: str) -> bool:
    keywords = [
        "policy",
        "compliance",
        "regulation",
        "regulatory",
        "allowed",
        "can i",
        "cannot",
        "can't",
        "must",
        "prohibited",
        "ban",
        "approve",
    ]
    text_lower = text.lower()
    return any(k in text_lower for k in keywords)


def _wants_technical(text: str) -> bool:
    keywords = [
        "api",
        "limit",
        "timeout",
        "error",
        "exception",
        "troubleshoot",
        "spec",
        "specification",
        "rate",
        "latency",
    ]
    text_lower = text.lower()
    return any(k in text_lower for k in keywords)


def _wants_support(text: str) -> bool:
    keywords = [
        "how do i",
        "how to",
        "steps",
        "step-by-step",
        "step by step",
        "guide",
        "walk me through",
        "explain",
        "summarize",
    ]
    text_lower = text.lower()
    return any(k in text_lower for k in keywords)


def route_experts_rules(user_input: str) -> RoutingDecision:
    pending: list[Expert] = []

    if _wants_compliance(user_input):
        pending.append("compliance_auditor")
    if _wants_technical(user_input):
        pending.append("technical_specialist")
    if _wants_support(user_input):
        pending.append("support_concierge")

    if not pending:
        pending = ["support_concierge"]

    # Deterministic order, and cap to 3 experts.
    deduped: list[Expert] = []
    for expert in pending:
        if expert not in deduped:
            deduped.append(expert)
    tasks: list[ExpertTask] = []
    for expert in deduped[:3]:
        tasks.append({
            "expert": expert,
            "query": user_input,
        })
    return RoutingDecision(tasks=tasks)


def get_router_mode() -> RouterMode:
    value = (get_env("CACHE_LM_ROUTER_MODE") or "").strip().lower()
    if value in ("rules", "llm"):
        return value  # type: ignore[return-value]
    if get_mode() == "llm":
        return "llm"
    return "rules"


def router_node(state: State) -> dict[str, object]:
    user_input = message_to_text(state["messages"][-1])
    decision: RoutingDecision
    if get_router_mode() == "llm":
        try:
            decision = llm_route_experts(
                user_input=user_input,
                messages=list(state.get("messages", [])),
            )
        except Exception:
            decision = route_experts_rules(user_input)
    else:
        decision = route_experts_rules(user_input)
    return {
        "pending_tasks": decision.tasks,
        "current_task": None,
    }

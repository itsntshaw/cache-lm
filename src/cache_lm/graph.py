from __future__ import annotations

from typing import Literal

from langchain_core.messages import AIMessage
from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph
from langgraph.types import Overwrite
from langgraph.types import Send

from cache_lm import experts as expert_nodes
from cache_lm.env import get_env
from cache_lm.manual import get_manual
from cache_lm.prompts import system_prefix_hash
from cache_lm.router import router_node
from cache_lm.state import Expert
from cache_lm.state import State

ExpertExecutionMode = Literal["sequential", "parallel"]


def _initialize_debug_metadata(state: State) -> dict[str, object]:
    manual = get_manual()
    return {
        "manual_sha256": manual.sha256,
        "system_prefix_hash": system_prefix_hash(manual_text=manual.text),
        "expert_outputs": Overwrite({}),
        "response": Overwrite(""),
        "pending_tasks": Overwrite([]),
        "current_task": Overwrite(None),
        "ttft_ms_by_expert": Overwrite({}),
        "latency_ms_by_expert": Overwrite({}),
    }


def _select_next_task(state: State) -> dict[str, object]:
    pending = list(state.get("pending_tasks", []))
    if not pending:
        return {"current_task": None, "pending_tasks": []}
    current_task = pending.pop(0)
    return {"current_task": current_task, "pending_tasks": pending}


def _dispatch(state: State) -> str:
    current_task = state.get("current_task")
    if current_task is None:
        return "finalize"
    return current_task["expert"]


def _finalize(state: State) -> dict[str, object]:
    ordered: list[Expert] = [
        "compliance_auditor",
        "technical_specialist",
        "support_concierge",
    ]
    parts = []
    for expert in ordered:
        text = state.get("expert_outputs", {}).get(expert)
        if text:
            parts.append(text)
    response = "\n\n".join(parts).strip()
    if not response:
        response = "No expert produced an output."
    return {"response": response, "messages": [AIMessage(content=response)]}


def get_expert_execution_mode() -> ExpertExecutionMode:
    value = (get_env("CACHE_LM_EXPERT_EXECUTION") or "").strip().lower()
    if value in ("sequential", "parallel"):
        return value  # type: ignore[return-value]
    return "sequential"


def _fanout_to_experts(state: State):
    tasks = list(state.get("pending_tasks", []))
    if not tasks:
        return "finalize"
    # In parallel execution, `Send(...)` passes a per-task input dict to each
    # expert node. Expert nodes still need access to conversation history to
    # build prompts correctly, so we include `messages` explicitly.
    messages = list(state.get("messages", []))
    return [
        Send(task["expert"], {
            "task": task,
            "messages": messages
        }) for task in tasks
    ]


def _create_sequential_graph() -> StateGraph:
    graph = StateGraph(State)

    graph.add_node("init", _initialize_debug_metadata)
    graph.add_node("router", router_node)
    graph.add_node("next_task", _select_next_task)

    graph.add_node("technical_specialist",
                   expert_nodes.technical_specialist_node)
    graph.add_node("compliance_auditor", expert_nodes.compliance_auditor_node)
    graph.add_node("support_concierge", expert_nodes.support_concierge_node)

    graph.add_node("finalize", _finalize)

    graph.add_edge(START, "init")
    graph.add_edge("init", "router")
    graph.add_edge("router", "next_task")

    graph.add_conditional_edges(
        "next_task",
        _dispatch,
        {
            "technical_specialist": "technical_specialist",
            "compliance_auditor": "compliance_auditor",
            "support_concierge": "support_concierge",
            "finalize": "finalize",
        },
    )

    graph.add_edge("technical_specialist", "next_task")
    graph.add_edge("compliance_auditor", "next_task")
    graph.add_edge("support_concierge", "next_task")

    graph.add_edge("finalize", END)
    return graph


def _create_parallel_graph() -> StateGraph:
    graph = StateGraph(State)

    graph.add_node("init", _initialize_debug_metadata)
    graph.add_node("router", router_node)

    graph.add_node("technical_specialist",
                   expert_nodes.technical_specialist_node)
    graph.add_node("compliance_auditor", expert_nodes.compliance_auditor_node)
    graph.add_node("support_concierge", expert_nodes.support_concierge_node)

    graph.add_node("finalize", _finalize)

    graph.add_edge(START, "init")
    graph.add_edge("init", "router")

    graph.add_conditional_edges(
        "router",
        _fanout_to_experts,
        [
            "technical_specialist",
            "compliance_auditor",
            "support_concierge",
            "finalize",
        ],
    )

    graph.add_edge("technical_specialist", "finalize")
    graph.add_edge("compliance_auditor", "finalize")
    graph.add_edge("support_concierge", "finalize")

    graph.add_edge("finalize", END)
    return graph


def create_graph() -> StateGraph:
    if get_expert_execution_mode() == "parallel":
        return _create_parallel_graph()
    return _create_sequential_graph()


def compiled_graph():
    return create_graph().compile()

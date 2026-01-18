from __future__ import annotations

from dataclasses import dataclass
import operator
from typing import Annotated, Literal, TypedDict

from langgraph.graph import MessagesState

Expert = Literal["technical_specialist", "compliance_auditor",
                 "support_concierge"]


class ExpertTask(TypedDict):
    expert: Expert
    query: str


class State(MessagesState):
    pending_tasks: list[ExpertTask]
    current_task: ExpertTask | None
    expert_outputs: Annotated[dict[Expert, str], operator.or_]
    response: str
    manual_sha256: str
    system_prefix_hash: str
    ttft_ms_by_expert: Annotated[dict[Expert, float], operator.or_]
    latency_ms_by_expert: Annotated[dict[Expert, float], operator.or_]


@dataclass(frozen=True)
class RoutingDecision:
    tasks: list[ExpertTask]

from __future__ import annotations

from typing import Literal, TypedDict

from cache_lm.hashing import sha256_text
from cache_lm.manual import get_manual

Expert = Literal["technical_specialist", "compliance_auditor",
                 "support_concierge"]


class ChatMessage(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


def to_langchain_messages(messages: list[ChatMessage]):
    from langchain_core.messages import AIMessage
    from langchain_core.messages import BaseMessage
    from langchain_core.messages import HumanMessage
    from langchain_core.messages import SystemMessage

    converted: list[BaseMessage] = []
    for message in messages:
        role = message["role"]
        content = message["content"]
        if role == "system":
            converted.append(SystemMessage(content=content))
        elif role == "user":
            converted.append(HumanMessage(content=content))
        elif role == "assistant":
            converted.append(AIMessage(content=content))
        else:
            raise ValueError(f"Unsupported role: {role}")
    return converted


GLOBAL_SYSTEM_INSTRUCTIONS = (
    "You are an internal bank assistant. Answer using only the provided manual "
    "when possible. If the manual does not contain the answer, say so explicitly."
)

MANUAL_BEGIN = "===== BEGIN INTERNAL OPERATIONS & COMPLIANCE MANUAL ====="
MANUAL_END = "===== END INTERNAL OPERATIONS & COMPLIANCE MANUAL ====="


def system_prefix_text(*, manual_text: str | None = None) -> str:
    manual = manual_text if manual_text is not None else get_manual().text
    return "\n\n".join([
        GLOBAL_SYSTEM_INSTRUCTIONS,
        MANUAL_BEGIN,
        manual,
        MANUAL_END,
    ])


def system_prefix_hash(*, manual_text: str | None = None) -> str:
    return sha256_text(system_prefix_text(manual_text=manual_text))


_EXPERT_SYSTEM_SUFFIX: dict[Expert, str] = {
    "technical_specialist":
    ("You are the Technical Specialist. Extract system specifications, API limits, "
     "and troubleshooting steps from the manual. Be precise and cite section names "
     "or headings when applicable."),
    "compliance_auditor":
    ("You are the Compliance Auditor. Interpret regulatory rules and 'Can/Cannot' "
     "constraints from the manual. Be strict about policy boundaries and clearly "
     "state what is allowed vs. disallowed."),
    "support_concierge":
    ("You are the Support Concierge. Summarize complex procedures into clear, "
     "step-by-step guides for non-technical staff. Prefer numbered steps."),
}


def expert_system_suffix_text(expert: Expert) -> str:
    return _EXPERT_SYSTEM_SUFFIX[expert]


def build_messages(
    *,
    expert: Expert,
    user_input: str,
    history: list[ChatMessage] | None = None,
    manual_text: str | None = None,
) -> list[ChatMessage]:
    messages: list[ChatMessage] = [
        {
            "role": "system",
            "content": system_prefix_text(manual_text=manual_text)
        },
        {
            "role": "system",
            "content": expert_system_suffix_text(expert)
        },
    ]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": user_input})
    return messages

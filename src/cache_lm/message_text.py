from __future__ import annotations

from typing import Any


def content_to_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
                continue
            if isinstance(item, dict):
                text = item.get("text")
                if isinstance(text, str):
                    parts.append(text)
                    continue
                embedded = item.get("content")
                if isinstance(embedded, str):
                    parts.append(embedded)
        return "".join(parts)
    return str(content)


def message_to_text(message: Any) -> str:
    if isinstance(message, dict):
        return content_to_text(message.get("content"))
    return content_to_text(getattr(message, "content", None))


def message_role(message: Any) -> str | None:
    if isinstance(message, dict):
        role = message.get("role") or message.get("type")
        if role in ("human", "user"):
            return "user"
        if role in ("ai", "assistant"):
            return "assistant"
        if role == "system":
            return "system"
        return None

    msg_type = getattr(message, "type", None)
    if msg_type == "human":
        return "user"
    if msg_type == "ai":
        return "assistant"
    if msg_type == "system":
        return "system"
    return None

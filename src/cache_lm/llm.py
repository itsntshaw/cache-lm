from __future__ import annotations

from dataclasses import dataclass

from langchain_openai import ChatOpenAI

from cache_lm.env import get_env


@dataclass(frozen=True)
class LlmConfig:
    base_url: str
    api_key: str
    model: str
    temperature: float
    max_tokens: int


def load_llm_config() -> LlmConfig:
    base_url = get_env("OPENAI_BASE_URL", "http://localhost:8000/v1")
    api_key = get_env("OPENAI_API_KEY", "")
    model = get_env("OPENAI_MODEL", "gpt-4o-mini")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY must be set when CACHE_LM_MODE=llm")
    temperature = float(get_env("OPENAI_TEMPERATURE", "0") or "0")
    max_tokens = int(get_env("OPENAI_MAX_TOKENS", "256") or "256")
    return LlmConfig(
        base_url=base_url,
        api_key=api_key,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )


def create_chat_model(*, streaming: bool) -> ChatOpenAI:
    cfg = load_llm_config()
    return ChatOpenAI(
        model=cfg.model,
        api_key=cfg.api_key,
        base_url=cfg.base_url,
        temperature=cfg.temperature,
        max_tokens=cfg.max_tokens,
        streaming=streaming,
    )

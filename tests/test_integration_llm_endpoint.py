from __future__ import annotations

import json
import os
import urllib.error
import urllib.request

import pytest


def _get_required_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        pytest.skip(f"{name} is not set")
    return value


def _build_chat_completions_url(base_url: str) -> str:
    base = base_url.rstrip("/")
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/v1/chat/completions"


@pytest.mark.integration
def test_openai_compatible_chat_completions_smoke() -> None:
    if os.environ.get("RUN_LLM_TESTS") != "1":
        pytest.skip("RUN_LLM_TESTS != 1")

    base_url = _get_required_env("OPENAI_BASE_URL")
    api_key = _get_required_env("OPENAI_API_KEY")
    model = _get_required_env("OPENAI_MODEL")

    url = _build_chat_completions_url(base_url)
    payload = {
        "model": model,
        "messages": [{
            "role": "user",
            "content": "Hello!"
        }],
        "max_tokens": 20,
        "temperature": 0.0,
    }
    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:  # nosec B310
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise AssertionError(f"HTTP {e.code}: {body}") from e

    obj = json.loads(raw)
    assert obj["object"] == "chat.completion"
    assert obj["model"] == model
    assert obj["choices"][0]["message"]["role"] == "assistant"

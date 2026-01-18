from __future__ import annotations

from cache_lm.router_llm import parse_routing_json


def test_parse_routing_json_accepts_code_fenced_json() -> None:
    decision = parse_routing_json(
        model_text="""
```json
{"tasks":[{"expert":"technical_specialist","query":""}]}
```
""",
        user_input="What is the API limit?",
    )
    assert decision is not None
    assert decision.tasks == [{
        "expert": "technical_specialist",
        "query": "What is the API limit?",
    }]

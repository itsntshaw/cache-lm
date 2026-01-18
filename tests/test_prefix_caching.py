from __future__ import annotations

from cache_lm.hashing import sha256_text
from cache_lm.manual import get_manual
from cache_lm.prompts import build_messages
from cache_lm.prompts import Expert
from cache_lm.prompts import MANUAL_BEGIN
from cache_lm.prompts import system_prefix_hash
from cache_lm.prompts import system_prefix_text


def test_manual_roundtrip_matches_raw_bytes():
    manual = get_manual(use_cache=False)
    assert manual.text.encode("utf-8") == manual.bytes


def test_manual_sha256_is_stable_across_loads():
    manual1 = get_manual(use_cache=False)
    manual2 = get_manual(use_cache=False)
    assert manual1.sha256 == manual2.sha256


def test_system_prefix_is_identical_across_experts():
    manual = get_manual(use_cache=False)
    experts: list[Expert] = [
        "technical_specialist",
        "compliance_auditor",
        "support_concierge",
    ]

    prefixes = []
    prefix_hashes = []
    prefix_hashes_from_messages = []
    for expert in experts:
        messages = build_messages(
            expert=expert,
            user_input="hello",
            manual_text=manual.text,
        )
        prefixes.append(messages[0]["content"])
        prefix_hashes.append(system_prefix_hash(manual_text=manual.text))
        prefix_hashes_from_messages.append(sha256_text(messages[0]["content"]))

    assert prefixes[0] == prefixes[1] == prefixes[2]
    assert prefix_hashes[0] == prefix_hashes[1] == prefix_hashes[2]
    assert (prefix_hashes_from_messages[0] == prefix_hashes_from_messages[1] ==
            prefix_hashes_from_messages[2])


def test_expert_suffix_is_after_manual_prefix():
    manual = get_manual(use_cache=False)
    messages = build_messages(
        expert="compliance_auditor",
        user_input="What can we do?",
        manual_text=manual.text,
    )

    assert messages[0]["role"] == "system"
    assert messages[1]["role"] == "system"
    assert messages[0]["content"] == system_prefix_text(
        manual_text=manual.text)
    assert "Compliance Auditor" in messages[1]["content"]
    assert MANUAL_BEGIN not in messages[1]["content"]

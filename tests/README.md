# Tests (cache-lm)

I wrote these tests to validate the assignment’s core requirements:

- **Logic correctness:** routing → expert execution → final response.
- **Cache awareness:** the 25k-token manual remains a stable System #1 prefix and is never persisted in state.
- **Production readiness basics:** safe defaults, compatibility with common message shapes, and integration smoke tests against an OpenAI-compatible endpoint.

## Test Modes and Safety Guards

If you want to run the integration tests, start with `ENV.md`.

## Expected `pytest` Output (All Tests)

When I run the full suite with integration tests enabled, I expect `pytest` to look roughly like this (exact versions/timings may vary):

```text
pytest
=================================================== test session starts ====================================================
platform darwin -- Python 3.13.9, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/shawnguyen/cache-lm
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.12.1, langsmith-0.6.4
collected 17 items

tests/test_graph_all_experts_stubbed.py .                                                                            [  5%]
tests/test_graph_workflow_stubbed.py ...                                                                             [ 23%]
tests/test_integration_graph_all_experts.py .                                                                        [ 29%]
tests/test_integration_graph_ttft.py .                                                                               [ 35%]
tests/test_integration_llm_endpoint.py .                                                                             [ 41%]
tests/test_integration_llm_router.py .                                                                               [ 47%]
tests/test_parallel_execution.py .                                                                                   [ 52%]
tests/test_persistence_threads.py .                                                                                  [ 58%]
tests/test_prefix_caching.py ....                                                                                    [ 82%]
tests/test_router_content_blocks.py .                                                                                [ 88%]
tests/test_router_llm_parsing.py .                                                                                   [ 94%]
tests/test_smoke.py .                                                                                                [100%]

=================================================== 17 passed in 18.54s ====================================================
```

### Offline unit tests (default)

`tests/conftest.py` forces non-integration tests into a fully offline configuration:

- `CACHE_LM_MODE=stub` (never call the network)
- `CACHE_LM_ROUTER_MODE=rules` (deterministic keyword router)
- `CACHE_LM_EXPERT_EXECUTION=sequential` (stable ordering)

This ensures `python -m pytest -q` is safe to run without secrets and without network access.

### Online integration tests (opt-in)

Integration tests are marked with `@pytest.mark.integration` and skip unless:

- `RUN_LLM_TESTS=1`
- `OPENAI_BASE_URL`, `OPENAI_API_KEY`, and `OPENAI_MODEL` are set

Run (loads `.env`): `set -a; source .env; set +a; python -m pytest -q -m integration`

## Test Files (What Each Covers)

### `tests/test_smoke.py`

Packaging and entrypoint smoke test.

- `test_module_help_exits_zero`
  - Verifies `python -m cache_lm --help` exits 0 and prints a usage string.
  - Catches broken installs, missing `__main__`, or CLI arg parsing regressions.

### `tests/test_prefix_caching.py`

Validates the **prefix-caching contract** at the prompt-building layer, independent of LangGraph execution.

- `test_manual_roundtrip_matches_raw_bytes`
  - Ensures `manual.text` is a lossless decode of the manual file bytes (`manual.bytes`).
  - Guards against trimming/normalization that would break prefix caching.
- `test_manual_sha256_is_stable_across_loads`
  - Ensures `manual.sha256` is stable and can detect manual edits.
- `test_system_prefix_is_identical_across_experts`
  - Ensures System #1 content is byte-identical across all experts.
  - Validates `system_prefix_hash(manual_text=...)` is constant across experts.
- `test_expert_suffix_is_after_manual_prefix`
  - Ensures expert persona/formatting is in System #2 and does not contain the manual prefix marker.

### `tests/test_graph_workflow_stubbed.py`

Validates the **Graph API workflow** in stub mode (no network).

- `test_rules_router_selects_expected_expert`
  - Ensures deterministic routing behavior for representative “technical”, “compliance”, and “support” queries.
- `test_rules_router_can_select_multiple_experts_for_mixed_query`
  - Ensures the router can select multiple experts for mixed intent in a single user turn.
- `test_graph_runs_and_does_not_store_manual_in_messages`
  - Executes the compiled graph and asserts:
    - `manual_sha256` matches the loaded manual
    - `system_prefix_hash` exists (prefix drift signal)
    - `response` exists
    - manual text is **not** present in `messages` (system/manual content must not enter state history)

### `tests/test_graph_all_experts_stubbed.py`

Validates the “full 3-expert” path in stub mode.

- `test_graph_can_run_all_three_experts_in_one_turn_stubbed`
  - Forces a query that should route to all 3 experts.
  - Asserts all expert outputs exist and appear in the final synthesized response.

### `tests/test_persistence_threads.py`

Validates **persistent state / threads** without persisting the manual.

- `test_thread_persistence_accumulates_messages_and_keeps_prefix_stable`
  - Compiles with an `InMemorySaver` checkpointer and re-invokes with the same `thread_id`.
  - Asserts:
    - message history accumulates (`messages` grows)
    - `manual_sha256` and `system_prefix_hash` remain constant across turns
    - checkpointed state contains neither the manual prefix marker nor the manual text

### `tests/test_router_content_blocks.py`

Validates router compatibility with “content blocks” message formats.

- `test_router_node_accepts_list_content_blocks`
  - Ensures the router can consume messages where `.content` is a list of structured blocks (common in some UIs/servers).
  - Prevents regressions like `AttributeError("'list' object has no attribute 'lower'")`.

### `tests/test_router_llm_parsing.py`

Validates robustness of LLM-router JSON parsing.

- `test_parse_routing_json_accepts_code_fenced_json`
  - Ensures the parser can recover JSON even if the model wraps it in Markdown fences.
  - Keeps routing resilient against minor formatting drift.

### `tests/test_parallel_execution.py`

Validates that parallel expert execution is state-safe.

- `test_parallel_fanout_merges_expert_outputs_without_conflicts`
  - Runs the graph with `CACHE_LM_EXPERT_EXECUTION=parallel`.
  - Ensures concurrent expert state updates merge correctly (reducer-safe) and produce expected outputs.

## Integration Tests (Live Endpoint)

These tests validate the system against a real OpenAI-compatible endpoint (vLLM in my case).

### `tests/test_integration_llm_endpoint.py`

- `test_openai_compatible_chat_completions_smoke`
  - Minimal direct HTTP call to `/v1/chat/completions`.
  - Validates connectivity, auth, and response schema.

### `tests/test_integration_llm_router.py`

- `test_llm_router_selects_expected_experts_for_mixed_query`
  - Runs the lightweight router LLM call (no manual) and validates:
    - routing includes compliance + technical for a mixed query
    - tasks are deterministically ordered

### `tests/test_integration_graph_ttft.py`

- `test_graph_runs_with_llm_and_records_ttft`
  - Runs the full graph in `CACHE_LM_MODE=llm`.
  - Validates end-to-end execution and that TTFT/latency metrics are recorded and consistent.

### `tests/test_integration_graph_all_experts.py`

- `test_graph_exercises_all_experts_with_llm`
  - Forces a query that should engage all three experts.
  - Validates all expert outputs exist and metrics are present per expert.

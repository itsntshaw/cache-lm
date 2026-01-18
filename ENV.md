# Environment Variables (`.env`)

For local development I use a `.env` file to keep secrets out of the repo and to make CLI/server runs reproducible.

I use env vars for:

- switching between **stub vs live LLM** mode
- configuring the **OpenAI-compatible** endpoint (vLLM)
- enabling **integration tests**
- setting defaults for **thread persistence** in the CLI

## Setup

1. Copy `.env.example` to `.env`.
2. Fill in values for your environment.

To load the file in your current shell session (recommended for running tests):

`set -a; source .env; set +a`

## Required for Live LLM Calls

These are required when `CACHE_LM_MODE=llm` and for integration tests:

- `OPENAI_BASE_URL`
  - Example: `http://89.169.108.198:30080/v1`
  - If you omit `/v1`, the client will append it.
- `OPENAI_API_KEY`
  - With vLLM this is used as a bearer token (`Authorization: Bearer <key>`).
- `OPENAI_MODEL`
  - Example: `Qwen/Qwen3-30B-A3B-Instruct-2507`

## Optional LLM Parameters

- `OPENAI_TEMPERATURE` (default: `0`)
- `OPENAI_MAX_TOKENS` (default: `256`)

Integration tests may temporarily override these to keep tests fast (see `tests/test_integration_graph_all_experts.py` and `tests/test_integration_llm_router.py`).

## Run / Test Switches

- `CACHE_LM_MODE`
  - `stub` (default): no network calls; experts return deterministic stub outputs
  - `llm`: experts call the configured OpenAI-compatible endpoint
- `CACHE_LM_ROUTER_MODE`
  - `rules`: deterministic keyword router (offline)
  - `llm`: lightweight LLM router (does not include the manual)
  - default behavior: `llm` when `CACHE_LM_MODE=llm`, otherwise `rules`
- `CACHE_LM_EXPERT_EXECUTION`
  - `sequential` (default): call experts one-by-one (best for demonstrating “2nd/3rd expert TTFT reduction” on prefix-caching engines)
  - `parallel`: fan out selected experts concurrently (reduces total wall time; may reduce the cache-warming TTFT signal)
- `RUN_LLM_TESTS`
  - `0` (default): integration tests are skipped
  - `1`: integration tests run when `OPENAI_*` vars are present

Note: unit tests force safe defaults regardless of your `.env` (see `tests/conftest.py`).

## CLI Persistence Defaults

These are optional convenience defaults used by `cache-lm run` when flags are omitted:

- `CACHE_LM_CHECKPOINT_DB` (default in `.env.example`: `.cache_lm/checkpoints.sqlite`)
- `CACHE_LM_THREAD_ID` (default in `.env.example`: `demo`)

You can always override them explicitly:

- `cache-lm run --checkpoint-db .cache_lm/checkpoints.sqlite --thread-id t1 --input "..."`.

## Agent Server (`langgraph dev`)

`langgraph.json` points the Agent Server at `.env`, so `langgraph dev` uses the same settings as the CLI.

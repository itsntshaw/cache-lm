# `cache_lm` package (implementation notes)

This folder contains the actual implementation of the **cache-lm** system described in the root `README.md` and `TechnicalAssignment.md`.

When I started this assignment, I tried to keep the code easy to review. The files are small, and each module has a single responsibility.

High-level goals:

- **Prefix/KV cache aware prompting:** the large manual must be a token-identical prefix across all expert calls.
- **Multi-agent orchestration:** router → 1–3 experts → synthesis.
- **Persistent state:** grow conversation history via threads/checkpoints without persisting the manual.
- **TTFT/latency observability:** record per-expert TTFT and total latency.

If you want to follow the main execution path, I’d start here:

- `src/cache_lm/graph.py` (how the workflow is wired)
- `src/cache_lm/router.py` + `src/cache_lm/router_llm.py` (how experts are selected)
- `src/cache_lm/experts.py` (how experts call the model and measure TTFT)
- `src/cache_lm/prompts.py` + `src/cache_lm/manual.py` (how I keep the manual prefix stable)

## Module Map

### Manual loading (immutable input)

- `src/cache_lm/manual.py`
  - Loads `data/operations_manual.md` **verbatim**.
  - Exposes:
    - raw bytes + decoded text (no trimming/normalization)
    - `sha256` fingerprint for drift detection (`manual_sha256` in state)

### Prompt construction (prefix caching contract)

- `src/cache_lm/prompts.py`
  - Builds chat messages in a fixed order that is friendly to prefix caching:
    1. **System #1 (invariant):** global instruction + full manual (verbatim)
    2. **System #2 (expert):** expert persona + response rules
    3. **Dynamic:** conversation history + current user input
  - Exposes:
    - `system_prefix_text(...)` and `system_prefix_hash(...)` used to prove prefix stability
    - `build_messages(...)` used by expert nodes

My hard rule here is simple: I never put expert persona, timestamps, request IDs, or chat history before the manual.

### State schema (what is persisted vs. recomputed)

- `src/cache_lm/state.py`
  - Graph state is based on `MessagesState` (so `messages` grows over time).
  - Only **user/assistant** messages are stored in `messages` (no manual/system messages).
  - Stores small “debug/telemetry” fields to validate cache alignment:
    - `manual_sha256`
    - `system_prefix_hash`
  - Stores orchestration + outputs:
    - `pending_tasks` (router output: up to 1–3 expert tasks)
    - `current_task` (sequential mode)
    - `expert_outputs` (per-expert text)
    - `response` (final synthesized response)
  - Stores metrics (when LLM mode is enabled):
    - `ttft_ms_by_expert`
    - `latency_ms_by_expert`

Important persistence rule: **the manual text is never stored in state/checkpoints**; only hashes are stored.

### Router (rules and lightweight LLM router)

- `src/cache_lm/router.py`

  - Implements the router node used by the graph.
  - Supports:
    - `CACHE_LM_ROUTER_MODE=rules` (deterministic keyword router; offline)
    - `CACHE_LM_ROUTER_MODE=llm` (lightweight router LLM call; no manual)
  - Router output is always normalized into a list of `{expert, query}` tasks.

- `src/cache_lm/router_llm.py`
  - The lightweight LLM router prompt and parsing logic.
  - Key constraint: the router call does **not** include the full manual (to avoid spending 25k tokens on routing).
  - Parsing is defensive: accepts JSON wrapped in code fences and normalizes/validates expert names.

### Experts (stub vs real LLM calls)

- `src/cache_lm/experts.py`
  - Provides three expert nodes:
    - `technical_specialist_node`
    - `compliance_auditor_node`
    - `support_concierge_node`
  - Behavior is controlled by `CACHE_LM_MODE`:
    - `stub`: deterministic placeholder responses (no network)
    - `llm`: calls the OpenAI-compatible endpoint with streaming enabled
  - Prefix-caching rules are enforced by always using `build_messages(...)` from `src/cache_lm/prompts.py`.
  - TTFT measurement:
    - record time at request start
    - record first streamed token time
    - record end time
    - emit `ttft_ms_by_expert` and `latency_ms_by_expert` into state

### LLM client wrapper (OpenAI-compatible)

- `src/cache_lm/llm.py`
  - Centralizes model configuration (base URL, model name, API key, sampling params).
  - Keeps LLM wiring out of graph logic so tests can force stub mode.

### Graph orchestration (Graph API)

- `src/cache_lm/graph.py`
  - Builds a LangGraph `StateGraph(State)` that:
    1. Initializes per-run metadata (`manual_sha256`, `system_prefix_hash`) and resets ephemeral fields.
    2. Routes the user input into `pending_tasks` (up to 3 expert calls).
    3. Executes experts either:
       - **sequentially** (default): `current_task` loop
       - **in parallel**: `Send(...)` fan-out (`CACHE_LM_EXPERT_EXECUTION=parallel`)
    4. Finalizes a combined `response` by concatenating expert outputs in a stable order.
  - Parallel safety:
    - `src/cache_lm/state.py` defines reducer-safe dict merges for `expert_outputs` and metrics so concurrent writes don’t conflict.

Why sequential is the default:

- It best demonstrates the assignment’s “2nd/3rd agent TTFT reduction” story on prefix-caching backends (later expert calls can benefit from a warmed KV cache when System #1 is identical).

### Persistence (threads / checkpointing)

- `src/cache_lm/checkpointing.py`
  - Provides helpers for:
    - in-memory checkpointer (tests)
    - SQLite-backed checkpointer (CLI cross-process threads)
  - Tests use `JsonPlusSerializer(pickle_fallback=True)` so `messages` (LangChain message objects) serialize cleanly.
  - Key behavior: checkpoints persist `messages` + small metadata fields, but **never the manual**.

### Entry points (CLI and Agent Server)

- `src/cache_lm/cli.py`

  - `cache-lm manual-stats`: prints manual bytes + hashes (prefix drift signal).
  - `cache-lm run`: runs one graph invocation (optionally with `--checkpoint-db` + `--thread-id`).

- `src/cache_lm/server.py` and `langgraph.json`
  - Exposes a compiled graph symbol for `langgraph dev`.

### Message normalization (server/UI compatibility)

- `src/cache_lm/message_text.py`
  - Normalizes message content into text.
  - Handles “content blocks” (e.g., list-of-dicts) that can show up via Agent Server/Studio or UI integrations.

## Configuration

- Environment variable guide: `ENV.md`
- Template file: `.env.example`
- Env parsing helpers: `src/cache_lm/env.py`, `src/cache_lm/mode.py`

## Where to look next

- Root overview + run commands: `README.md`
- Test-by-test coverage mapping: `tests/README.md`
- Env var setup: `ENV.md`

# Technical Assignment: High-Efficiency Multi-Agent Orchestration

## Project Overview

Your objective is to build a functional **Multi-Agent Expert System** using **LangGraph**. The goal of this assignment is not just to create a working chatbot, but to demonstrate an architecture that is optimized for **high-performance LLM serving**.

Specifically, your solution must be designed to:

- **Maximize KV Cache hit rates**
- **Minimize Time to First Token (TTFT)**

…when using a serving framework that supports **Prefix Caching**.

---

## The Scenario

You are building an internal AI tool for a bank that helps different departments query a 50-page **"Internal Operations & Compliance Manual"** (approx. **25,000 tokens**).

Because this document is large, re-processing it for every agent interaction is computationally expensive and slow.

---

## System Architecture Requirements

### 1) The Core Agents

You must implement a **LangGraph workflow** containing:

- a **Router**
- **three specialized expert nodes**

All experts reference the same operations manual:

- **The Technical Specialist**

  - Responsible for extracting system specifications, API limits, and troubleshooting steps from the manual.

- **The Compliance Auditor**

  - Interprets regulatory rules, **"Can/Cannot"** constraints, and policy boundaries.

- **The Support Concierge**
  - Summarizes complex procedures into step-by-step guides for non-technical staff.

---

### 2) The "Efficiency" Constraint (The Primary Test)

Your implementation must prove that you understand how **KV Caching** works at the inference level.

#### Prefix Alignment

You must structure your prompt templates so that the large **Manual** remains a **fixed prefix** across all agents.

#### Dynamic vs. Static Content

You must demonstrate where to place agent-specific instructions (e.g., _"You are the Compliance Auditor"_) **relative to the 25k-token manual** to avoid **"busting"** the cache.

---

## Technical Deliverables

### Python Codebase

- A clean, modular implementation using **langgraph** and **langchain**.

### State Management

- Use a **persistent state schema** that allows the conversation history to grow **without re-calculating the fixed context cache**.

### Optimization Report (`README.md`)

Include:

- Your strategy for ensuring a **High Cache Hit Rate**
- How your architecture reduces **TTFT** for the **second and third agents** called in a single sequence
- Detail how you would monitor these efficiencies in production using tools like Langfuse, vLLM logs, or Grafana.



---

## Evaluation Criteria

- **Logic Correctness**

  - Does the LangGraph correctly route and resolve queries?

- **Cache Awareness**

  - Is the prompt structured to allow a serving engine to cache the 25k-token manual once and reuse it for all 3 agents?

- **Production Readiness**
  - Inclusion of error handling, logging, and clear documentation.

---

## Testing Endpoint

```bash
export VLLM_API_KEY="..."

curl -X POST http://89.169.108.198:30080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $VLLM_API_KEY" \
  -d '{
    "model": "Qwen/Qwen3-30B-A3B-Instruct-2507",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "max_tokens": 100,
    "temperature": 0.7
  }'
```

Output:
```bash
{"id": "chatcmpl-3c2c713146d04ab99fcbd75a7f3d8420", "object": "chat.completion", "created": 1768687640, "model": "Qwen/Qwen3-30B-A3B-Instruct-2507", "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hello! How can I help you today? 😊", "refusal": null, "annotations": null, "audio": null, "function_call": null, "tool_calls": [], "reasoning_content": null}, "logprobs": null, "finish_reason": "stop", "stop_reason": null, "token_ids": null}], "service_tier": null, "system_fingerprint": null, "usage": {"prompt_tokens": 10, "total_tokens": 22, "completion_tokens": 12, "prompt_tokens_details": null}, "prompt_logprobs": null, "prompt_token_ids": null, "kv_transfer_params": null}
```

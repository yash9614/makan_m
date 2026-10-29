# Harness, Guardrails & Reliability

In agentic and RAG systems, a “harness” refers to the surrounding infrastructure that makes the model reliable, safe, and controllable in production.

---

## What a Harness Typically Includes

- Input validation and sanitization
- Output validation / structured output enforcement
- Guardrails (content filters, PII detection, policy checks)
- Tool permission checks
- Iteration / step limits
- Fallback strategies
- Observability and tracing
- Human-in-the-loop checkpoints

---

## Common Guardrails

| Type | Purpose |
|------|---------|
| Prompt injection detection | Prevent malicious user instructions from overriding system behavior |
| PII filtering | Avoid leaking sensitive data |
| Output schema validation | Ensure structured responses match expected format |
| Tool allow-lists | Restrict which tools an agent can call |
| Rate limiting & cost controls | Protect expensive endpoints |
| Content safety filters | Block harmful or policy-violating outputs |

---

## Why It Matters

Raw LLM calls are not production-ready. A harness turns a model into a reliable component of a larger system.

Without guardrails:
- Agents can call dangerous tools
- RAG systems can leak private data
- Costs can explode from runaway loops
- Users can jailbreak or inject instructions

---

## Interview Points

- A production AI system needs a harness around the model
- Guardrails include input/output filtering, permission checks, step limits, and observability
- Especially critical for agents that can take actions
- Related to MCP security, JWT scopes, and RAG access control

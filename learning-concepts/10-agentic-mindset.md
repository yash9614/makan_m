# Agentic Mindset: Model as Brain, Tools as Hands

An LLM is a reasoning engine (the brain). It cannot take real-world actions or access live/private data on its own.

An **agent** = LLM + tools (and the loop that decides when to use them).

---

## Core Idea

- Model alone = chatbot (can answer from training data, can hallucinate, has knowledge cutoff).
- Model + tools = agent that can search, call APIs, read documents, book, compute, etc.
- Tools are ordinary functions (or MCP servers) the model is allowed to call.

---

## Why This Matters

- Knowledge cutoff is solved by tools (web search, date APIs, internal systems).
- Hallucination is reduced by grounding in retrieved or tool-returned data.
- Plain chatbots are rarely products; useful applications need RAG + tools + memory + guardrails.

---

## The Agent Loop (ReAct-style)

1. Reason about the task
2. Decide to call a tool (or answer directly)
3. Observe the tool result
4. Reason again
5. Repeat until done or limit reached

This is the cycle implemented in LangGraph, create_agent, CrewAI, etc.

---

## Industry Context

Most production GenAI systems are not pure chatbots. They are applications that call models, inject context via RAG, give the model tools via function calling or MCP, and wrap everything in guardrails, observability, and human-in-the-loop checkpoints.

---

## Interview Points

- An agent is a model plus tools plus a decision loop.
- The model decides *whether* and *which* tool to call; the harness executes it safely.
- Hard part is multi-agent coordination, reliability, and cost control, not creating a single agent.

# Deep Agents

Deep Agents (LangChain) is an opinionated **agent harness** for complex, long-horizon tasks.

It sits on top of LangChain's agent loop and LangGraph's runtime and adds planning, filesystem tools, subagents, and context management out of the box.

Sources: Krish Naik Deep-agents-With-Langchain, LangChain docs.

---

## The Stack

| Layer | Role |
|-------|------|
| **LangGraph** | Runtime — checkpoints, state, streaming, durable execution |
| **LangChain** | Framework — models, tools, minimal agent loop, middleware |
| **Deep Agents** | Harness — planning, filesystem, subagents, context management, skills |

Use Deep Agents when you want the full harness for research, coding, or multi-step work. Drop to LangGraph when you need full control of the graph.

---

## Core Capabilities

- **Planning tool** (`write_todos`) — break tasks into steps, track progress, adapt
- **Filesystem tools** (`ls`, `read_file`, `write_file`, `edit_file`) — offload large context, keep working artifacts
- **Subagents** — spawn specialized agents with isolated context
- **Context management** — summarization, offloading, prompt caching
- **Long-term memory** — via LangGraph Store
- **Human-in-the-loop** — interrupts and approvals

---

## Why It Exists

Naive tool-calling loops work for short tasks. Long-running agents (deep research, coding agents, multi-step workflows) need:
- Explicit planning
- Ways to manage growing context
- Ability to delegate without polluting the main context
- Persistence across turns

Deep Agents packages these patterns so you bring tools + prompt instead of building the harness yourself.

---

## Interview Points

- Deep Agents is a harness, not a new model or runtime
- Built on LangChain + LangGraph
- Key primitives: planning, filesystem, subagents, context management
- Best for long-horizon, multi-step tasks; overkill for simple single-tool agents
- Production systems still need observability, evaluation, and cost controls on top

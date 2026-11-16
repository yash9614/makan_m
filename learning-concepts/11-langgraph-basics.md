# LangGraph Basics

LangGraph lets you build controllable, stateful agent workflows as graphs of nodes and edges.

It is the standard way to implement ReAct loops, multi-step agents, parallel branches, human-in-the-loop, and persistence.

---

## Core Concepts

| Concept | Meaning |
|---------|---------|
| **State** | Shared data structure (usually TypedDict or Pydantic) that nodes read and write |
| **Node** | A function that does work and returns a partial state update |
| **Edge** | Connection that decides which node runs next (fixed or conditional) |
| **START / END** | Entry and exit markers |

---

## Key Patterns

- **Fixed edges**: Always go from A → B
- **Conditional edges**: Router function decides next node (e.g., tool call or END)
- **Parallel**: Multiple edges out of one node; joining node waits for all
- **Loops**: Conditional edge pointing backwards (always add a counter / max-iteration guard)
- **Checkpointers**: Save state so conversations and HITL can resume (MemorySaver for learning, DB-backed for production)

---

## Relationship to LangChain

`create_agent` and many agent APIs are built on LangGraph. LangGraph does not replace LangChain; it adds explicit control over flow, state, and persistence.

---

## Production Notes

- Always add iteration limits on loops
- Use structured output for anything you parse
- Feed previous feedback into the next prompt
- Wrap nodes in try/except and decide failure behavior
- Prefer checkpointers for anything that needs memory or human approval

---

## Interview Points

- LangGraph turns the agent loop into an explicit, inspectable graph
- State is the memory; nodes update it; edges control flow
- Parallel branches wait at the join; loops need counters
- Critical for reliable multi-step agents and human-in-the-loop

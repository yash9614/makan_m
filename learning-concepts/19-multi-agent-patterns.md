# Multi-Agent Patterns

Specialized agents collaborating on a larger goal. Common in research, content, analysis, and customer workflows.

Sources: entbappy LangChain-Multi-Agent-Research-System, Krish/Sunny courses, CrewAI patterns.

---

## Common Roles

Typical research / report pipeline:
- **Searcher** — finds sources (web, internal)
- **Reader / Extractor** — pulls clean content
- **Writer** — synthesizes into structured output
- **Critic / Reviewer** — scores quality, suggests fixes
- **Manager** (hierarchical) — delegates and validates

---

## Orchestration Styles

1. **Sequential pipeline** — fixed order, each step consumes previous output (CrewAI sequential, simple LangGraph chains)
2. **Hierarchical** — manager delegates and reviews (CrewAI hierarchical)
3. **Graph with routing** — LangGraph conditional edges, parallel branches, loops
4. **Subagent spawning** — Deep Agents style; main agent creates isolated workers

---

## Production Considerations

- Narrow roles reduce confusion and token waste
- Explicit handoff formats (structured output) improve reliability
- Critic / evaluator step is often worth the cost
- Cost multiplies with every agent call — set budgets and max iterations
- Observability is essential (trace which agent did what)
- Prefer one orchestration style; mixing too many increases complexity

---

## Interview Points

- Multi-agent systems split work across specialized roles
- Sequential is simplest; hierarchical or graph gives more flexibility
- Critic agents improve quality but add latency
- Always control cost and iteration limits
- LangGraph, CrewAI, and Deep Agents are the main practical options in the Python stack

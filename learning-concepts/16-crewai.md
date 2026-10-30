# CrewAI: Role-Based Multi-Agent Crews

CrewAI is a framework for building multi-agent systems where agents have clear roles and collaborate on tasks inside a crew.

It is opinionated and faster to prototype than pure LangGraph graphs for many team-style workflows.

---

## Core Building Blocks

| Component | What it is |
|-----------|------------|
| **Agent** | A worker defined by `role`, `goal`, and `backstory`. Can have tools. |
| **Task** | A unit of work with a description and expected output. Assigned to an agent (or left for a manager). |
| **Crew** | The team — list of agents + list of tasks + process. |
| **Process** | How work is coordinated: `sequential` or `hierarchical`. |

---

## Processes

**Sequential (default)**  
Tasks run in the order you list them. Output of one becomes context for the next. Simple, predictable, easy to debug.

**Hierarchical**  
A manager agent (or auto-created manager) delegates tasks, reviews results, and coordinates. More flexible for dynamic work, but adds extra LLM calls and cost.

---

## Typical Pattern

```python
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Senior Researcher",
    goal="Find accurate, up-to-date information",
    backstory="You are an expert at gathering and summarizing reliable sources.",
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    role="Technical Writer",
    goal="Produce clear, structured content",
    backstory="You turn research into readable, accurate articles.",
    verbose=True
)

research_task = Task(
    description="Research the topic: {topic}",
    expected_output="A concise research summary with key points and sources",
    agent=researcher
)

write_task = Task(
    description="Write a clear article based on the research",
    expected_output="A well-structured article",
    agent=writer,
    context=[research_task]
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"topic": "LangGraph vs CrewAI"})
```

---

## CrewAI vs LangGraph

| Aspect | CrewAI | LangGraph |
|--------|--------|-----------|
| Mental model | Role-based team (agents + tasks + crew) | Explicit state graph (nodes + edges) |
| Control | Opinionated processes (sequential / hierarchical) | Full control over branching, loops, parallel |
| Speed to prototype | Very fast for multi-role workflows | More boilerplate for simple teams |
| Persistence / HITL | Built-in memory options + human_input | First-class checkpointers and interrupt |
| Best for | Content pipelines, research crews, role-specialized teams | Complex control flow, custom routing, production reliability |

Many production systems use LangGraph for the overall orchestration and CrewAI (or similar) for specific multi-agent sub-teams, or simply stay with one.

---

## Production Notes

- Give agents narrow, non-overlapping roles
- Use `expected_output` and structured outputs where possible
- Set iteration / rate limits
- Prefer sequential for linear pipelines; hierarchical only when delegation is truly needed
- Add tools carefully and with permission checks
- Monitor cost — multi-agent systems multiply token usage

---

## Interview Points

- CrewAI models a team: Agents (role/goal/backstory) + Tasks + Crew + Process
- Sequential is the default and simplest; hierarchical adds a manager for dynamic delegation
- Faster to prototype multi-role systems than raw LangGraph graphs
- Trade-off is less fine-grained control compared with explicit graphs
- Common in content, research, and analysis pipelines

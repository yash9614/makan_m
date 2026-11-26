# Project Streak — Updated Analysis

**Repo:** [yash9614/project_streak_](https://github.com/yash9614/project_streak_)

A collection of beginner-to-intermediate Generative AI projects demonstrating RAG, agents, tool-calling, structured outputs, semantic routing, text-to-SQL, and full-stack LLM applications.

## Project Structure (from README)

| # | Project | Key Skills |
|---|---------|------------|
| 00 | Travel Planning Agent | RAG + Tool calling + MCP (dual path: direct Streamlit + MCP-backed FastAPI) + Chroma |
| 01 | Knowledge Intelligence System | Document upload RAG (PDF/TXT) with LangChain + Chroma |
| 02 | E-commerce Assistant | Semantic routing (small-talk / FAQ RAG / text-to-SQL) + SQLite |
| 03 | Customer Feedback Analyzer | Structured outputs (Pydantic + OpenAI `beta.chat.completions.parse`) + FastAPI + Streamlit dashboard + SQLite |

Architecture diagrams and clear folder layout are in the root README.

## Most Important Skill Highlighted

**Building hybrid agents that combine structured tools + RAG + MCP as a reusable interface**, while also practicing full-stack separation (Streamlit UI + FastAPI + MCP server).

This is the strongest differentiator in the collection — project 00 deliberately shows both a direct tool path and an MCP path so the same tools can be reused by other clients.

Secondary high-value skills:
- Semantic routing for multi-intent chatbots (project 02)
- Reliable structured outputs with Pydantic (project 03)
- Text-to-SQL grounded in a real database

## Skills Demonstrated Across the Repo

- RAG pipelines (ingestion, embeddings, Chroma retrieval)
- OpenAI tool calling / function calling with schemas
- MCP server (streamable HTTP) + MCP client in FastAPI
- Semantic routing between intents
- Text-to-SQL generation and execution
- Structured outputs (`response_format` with Pydantic models)
- Full-stack LLM apps (Streamlit + FastAPI)
- Persistent storage (Chroma + SQLite)
- Layered architecture and dual access paths

## Most Important Interview Questions (drawn from the projects)

1. **Explain the difference between calling tools directly vs exposing them via an MCP server.** When would you choose each?
2. **Walk through the request flow in the Travel Planning Agent** when a user asks for today’s date and Kyoto tips (tool + RAG).
3. **How does semantic routing work** in the e-commerce assistant, and what are the trade-offs vs pure LLM classification?
4. **Why use structured outputs (Pydantic + `parse`) instead of asking the model to return JSON and parsing it yourself?** What failure modes does it prevent?
5. **How would you make the Travel Planning Agent production-ready?** (persistence, auth, observability, cost control, scaling Chroma, etc.)
6. **What is the role of the dual path (Streamlit direct vs FastAPI + MCP) in project 00?**
7. **How would you add conversation memory** that survives restarts in these apps?
8. **Compare ChromaDB (local) vs a hosted vector database** for the RAG pieces in these projects.
9. **How does text-to-SQL stay safe?** (least privilege, validation, read-only user, etc.)
10. **What would you change to evaluate the quality of the RAG answers** in projects 00 or 01?

## Why This Collection Matters

Practical, progressive examples that move beyond single notebooks into multi-file applications covering the core patterns asked in GenAI/Agentic interviews: RAG, tools, MCP, structured output, routing, and full-stack separation.

## Related

- Deployment notes: [project-streak-deployment.md](project-streak-deployment.md)
- Must-do lists in learning-concepts/must-do/

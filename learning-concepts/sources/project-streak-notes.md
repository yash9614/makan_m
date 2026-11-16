# Notes from project_streak_

Progressive GenAI project combining conversational chat, tool calling, vector RAG, MCP server, and FastAPI backend.

**Repo:** [yash9614/project_streak_](https://github.com/yash9614/project_streak_)

## Stack

- UI: Streamlit
- LLM: OpenAI gpt-4o-mini
- Embeddings: text-embedding-3-small
- Vector DB: ChromaDB (persistent)
- MCP: streamable HTTP
- Backend: FastAPI

## Architecture Layers

```
UI (Streamlit) → Agent Loop / FastAPI → MCP Client → MCP Server → Tools + RAG
```

## Skills Practiced

- Conversational memory
- Structured tool calling (OpenAI tools)
- Vector RAG with ChromaDB
- MCP server (streamable HTTP) exposing date, cost, knowledge search
- MCP client inside FastAPI
- Separation of UI / API / MCP layers

## Why It Matters

Good end-to-end example of a hybrid agent that can use both structured tools and unstructured RAG knowledge, with MCP as the standard tool interface. Includes `concepts.md` with interview questions.

## Deployment

Currently local-only. Practical deployment path (Docker → Railway/Render → AWS ECS) is documented in [project-streak-deployment.md](project-streak-deployment.md).

## Related Must-Do

Added to the agents / MCP practice lists.

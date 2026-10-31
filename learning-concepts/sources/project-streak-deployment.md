# Project Streak — Deployment Notes

Practical path to take the multi-component GenAI prototype (Streamlit + FastAPI + MCP + ChromaDB) from local to online.

**Repo:** [yash9614/project_streak_](https://github.com/yash9614/project_streak_)

## Components to Deploy

| Component | Role | Port | Persistence |
|-----------|------|------|-------------|
| Streamlit (`app.py`) | UI | 8501 | No |
| FastAPI (`backend.py`) | API layer | 8001 | No |
| MCP server (`mcp_server.py`) | Tool/RAG server | 8000 | No |
| ChromaDB | Vector store | — | **Yes** (folder) |
| OpenAI keys | LLM + embeddings | — | Secrets |

Must handle multiple processes, persistent storage for Chroma, and secrets.

## Quickest Path (Learn First)

1. Write a basic Dockerfile (or multi-service) and test with docker-compose.
2. Deploy simplest version to Railway, Render, or AWS App Runner.
3. Mount a volume for the ChromaDB folder.
4. Store API keys in the platform secret manager.
5. Expose Streamlit publicly; keep FastAPI/MCP internal.

This teaches ports, env vars, persistence, and basic networking.

## Proper Production Path (AWS)

1. Containerize properly (one Dockerfile per service or multi-stage).
2. docker-compose for local parity.
3. Deploy on ECS Fargate (or EKS if Kubernetes is the goal).
4. Persistent storage: EFS for Chroma, or migrate to managed vector DB later.
5. Secrets: AWS Secrets Manager / Parameter Store.
6. Load balancer + auto-scaling for FastAPI/MCP.
7. CI/CD: GitHub Actions → ECR → ECS.

## Scaling Considerations

- OpenAI cost and rate limits are usually the first bottleneck.
- FastAPI and MCP can scale horizontally (mostly stateless).
- Chroma needs shared storage or a switch to Pinecone/Weaviate/Qdrant.
- Streamlit is less ideal for heavy horizontal scaling.
- Add caching, async patterns, and observability.

## Recommended Sequence

1. Run cleanly locally with your own keys.
2. Write a basic Dockerfile + docker-compose.
3. Deploy simplest version to Railway/Render/App Runner.
4. Then (optionally) hire help for a proper AWS setup with knowledge transfer.

## Related

- Main project notes: [project-streak-notes.md](project-streak-notes.md)
- Must-do: agents and MCP lists

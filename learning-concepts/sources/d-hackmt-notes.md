# Notes from d-hackmt Repos

Useful production-oriented material extracted from d-hackmt repositories.

## Key Repos

- **Basic-Rag** — HR Policy Assistant (LangChain + Groq + Jina + Qdrant)
  - Document loading, chunking, guardrails, LangSmith tracing, Docker, CI/CD
- **enterprise-rag-with-guardrails-gateways-evals** — Full enterprise stack
  - LangGraph + NeMo Guardrails + Portkey LLM Gateway + RAGAS + GCP Cloud Run + Terraform
- **guardrails-webinar** — NeMo Guardrails teaching app (Colang rules)
- **LIVE-WEBINAR-25-MAY-GATEWAYS** — LLM Gateway concepts with Portkey

## High-Value Patterns

1. **NeMo Guardrails / Colang** — define user intents, bot responses, and flows for safety
2. **LLM Gateway (Portkey)** — proxy for resilience, observability, cost control, provider switching
3. **RAGAS evals** as a separate microservice
4. **Layered production stack**: UI → backend → guardrails → gateway → evals
5. **Observability**: LangSmith + Logfire

These complement the existing harness/guardrails and evaluation notes.

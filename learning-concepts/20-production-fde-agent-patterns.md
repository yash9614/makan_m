# Production FDE Agent Patterns

Practical patterns from a cold-chain logistics Forward Deployed Engineer (FDE) project. Combines LangGraph agent, structured SQL tools, vector SOP retrieval, external APIs, and security controls.

Source: nimowhyca/cold-chain-logistics-FDE-Project.

---

## Architecture Overview

- **LangGraph ReAct loop**: reasoner node + ToolNode + conditional edges
- **Tools**:
  - SQL query against a restricted view (telemetry)
  - Live external API (weather/corridor conditions)
  - Vector search over SOPs (Pinecone)
- **Memory**: MemorySaver checkpointer with thread_id
- **Output control**: System prompt enforces structured business format (executive summary, table, action plan + SOP citation)

---

## Key Production Patterns

### 1. Tool Design
- Each tool has a clear, narrow purpose and detailed docstring (used by the LLM for selection)
- SQL tool enforces SELECT-only and limits rows returned
- Vector tool returns formatted context with source metadata
- External API tool has timeout and graceful failure

### 2. Security & Least Privilege
- Dedicated read-only database user (`USR_FDE_RO`)
- Access only to a clean view, not raw tables
- Explicit security block in the tool for non-SELECT queries
- Audit log table with INSERT-only permission for the agent user
- Secrets in `.env` (never committed)

### 3. Hybrid Data Access
- Structured data → SQL view
- Unstructured policy → vector store (Pinecone)
- Real-time external → REST API
- Agent decides the order (system prompt guides preferred flow)

### 4. Structured Output via Prompt
- System prompt mandates exact markdown structure
- Forces citations and action-oriented answers
- Prevents raw tool dumps in the final response

### 5. Operational Resilience
- LLM fallback (OpenAI / DeepSeek / local Ollama)
- Embedding model switch (OpenAI vs local HuggingFace)
- Caching of local embeddings
- Streamlit UI + systemd service for deployment

---

## Interview-Relevant Takeaways

- Production agents need least-privilege tools, not open database access
- Hybrid retrieval (SQL + vector + API) is common in enterprise FDE work
- System prompts can enforce output schemas even without structured-output mode
- Audit logging and view-based access are practical security controls
- Checkpointers + thread_ids enable multi-turn sessions
- Always handle tool failures gracefully

---

## When This Pattern Fits

Domain systems that need to combine:
- Operational databases (telemetry, orders, inventory)
- Policy / SOP documents
- External real-time signals (weather, traffic, market data)
- Business-user friendly structured answers

This is a classic Forward Deployed Engineer style application.

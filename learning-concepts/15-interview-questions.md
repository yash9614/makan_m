# Interview Questions — AI / GenAI / Agentic

Concise, high-signal answers drawn from production patterns and course material.

---

### 1. What is an agent?
An LLM plus tools plus a decision loop. The model decides when to call a tool; the system executes it and returns the result so the model can continue.

### 2. Why RAG instead of fine-tuning for company data?
RAG injects fresh or private knowledge at inference time without retraining. It is cheaper to update, supports citations, and reduces hallucination when retrieval is good. Fine-tuning is better for style or specialized reasoning.

### 3. Explain the agent loop.
Reason → Act (tool call) → Observe (result) → Reason again. Implemented as a graph in LangGraph or a while-loop in simpler agents.

### 4. What is MCP?
A standard protocol for hosts to discover and call tools, resources, and prompts from servers. Replaces custom integrations with a consistent client-server model.

### 5. Temperature vs Top-p?
Temperature scales randomness. Top-p (nucleus) keeps the smallest set of tokens whose probabilities sum to p. Lower values = more factual; higher = more creative.

### 6. Why do we need structured outputs?
So the model returns data that code can reliably parse and validate (Pydantic). Essential for tools, agents, evaluation judges, and APIs.

### 7. What are the four main RAG evaluation metrics?
Correctness (vs ground truth), Relevance (vs question), Groundedness/Faithfulness (vs retrieved docs), Retrieval relevance (docs vs question).

### 8. Why hybrid search?
Vector search is semantic; keyword/BM25 is exact. Combining them (then reranking) covers more query types and improves recall and precision.

### 9. What is a harness / guardrail in production agents?
The surrounding checks: input validation, PII filtering, tool allow-lists, step limits, output schema validation, human-in-the-loop, and observability. Raw model calls are not production-ready.

### 10. How does LangGraph differ from a simple agent loop?
LangGraph makes state, branching, parallel execution, loops, and persistence explicit and inspectable. It is the standard for controllable multi-step and multi-agent workflows.

### 11. Context window implications?
Everything (history, retrieved chunks, tool results, generation) must fit. Production systems summarize history, limit retrieved chunks, and use external memory.

### 12. When would you use a checkpointer?
Anytime the agent needs memory across turns or must pause for human approval (HITL). MemorySaver for prototypes; database-backed for production.

### 13. What is the difference between Self-RAG and CRAG?
CRAG grades the retrieved documents and takes corrective action (rewrite, web search) when confidence is low. Self-RAG additionally lets the model decide whether to retrieve and critique its own generated answer.

### 14. What is Agentic RAG?
Retrieval is treated as a tool the agent controls. The agent decides whether to retrieve, can retrieve multiple times, decompose queries, and stop when it has enough evidence. Higher cost and latency than basic RAG.

### 15. What is a Deep Agent?
An opinionated agent harness (on LangChain + LangGraph) that adds planning tools, filesystem access, subagent spawning, and context management for long-horizon tasks.

### 16. CrewAI sequential vs hierarchical?
Sequential runs tasks in fixed order with outputs flowing forward. Hierarchical adds a manager agent that delegates and reviews. Sequential is simpler and cheaper; hierarchical is more flexible but costs more.

### 17. When would you choose GraphRAG?
When questions are relational or multi-hop ("how does X relate to Y", comparisons). Pure vector search struggles with these; a knowledge graph helps.

---

*Use these as starting points. Expand with concrete examples from systems you have built.*

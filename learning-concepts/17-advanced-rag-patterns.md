# Advanced RAG Patterns

Beyond basic retrieve-then-generate. These patterns add decision-making, self-correction, or richer structure so the system recovers from bad retrievals and handles harder queries.

Sources: entbappy Complete-Agentic-AI-Course, Krish Naik RAG tutorials, industry papers (Self-RAG, CRAG).

---

## Naive / Basic RAG

Single embedding → top-k retrieval → generation. Fast and cheap. Fails when the first retrieval is wrong or the query is multi-hop.

---

## Self-RAG

The model decides whether retrieval is needed and critiques both the retrieved passages and its own answer (via reflection tokens or explicit checks).

Typical decisions:
- Is retrieval needed?
- Are the retrieved docs relevant?
- Is the generated answer supported by the docs?
- Is the answer useful?

Strength: selective retrieval + self-critique reduces hallucination.  
Cost: extra model calls or specialized training.

---

## Corrective RAG (CRAG)

After retrieval, a lightweight evaluator grades relevance.
- High confidence → use the docs
- Low confidence → rewrite query, fall back to web search, or other corrective action

Strength: explicit recovery when the knowledge base is incomplete.  
Common production pattern for customer-facing systems.

---

## Agentic RAG

Retrieval becomes a tool the agent controls. The agent can:
- Decide whether to retrieve at all
- Decompose the query
- Choose sources / tools
- Retrieve multiple times
- Stop when evidence is sufficient

Best for multi-hop, ambiguous, or research-style questions. Higher latency and cost.

---

## GraphRAG

Builds a knowledge graph (entities + relationships) from documents, often with community summaries. Retrieval walks the graph instead of (or in addition to) pure vector search.

Strength: multi-hop and relational questions ("compare X and Y", "how does A connect to B").  
Cost: graph construction and maintenance.

---

## When to Use What

| Pattern | Best for | Trade-off |
|---------|----------|-----------|
| Basic RAG | Simple factual lookups | Fast but brittle |
| Hybrid + Rerank | Most enterprise QA | Better first pass |
| CRAG | Noisy or incomplete corpora | Extra evaluation step |
| Self-RAG | High-stakes factual accuracy | More complex |
| Agentic RAG | Multi-hop / research | Higher cost & latency |
| GraphRAG | Relational / comparative queries | Graph build cost |

Most production systems start with hybrid retrieval and add corrective or agentic loops only where metrics show the need.

---

## Interview Points

- Basic RAG is one-shot; advanced patterns add evaluation or control loops
- CRAG grades retrieval and corrects; Self-RAG critiques both retrieval and generation
- Agentic RAG treats retrieval as a tool the agent can call repeatedly
- GraphRAG shines on relational questions
- Always measure before adding complexity — latency and cost rise quickly

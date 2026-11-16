# Why RAG (Retrieval-Augmented Generation)

LLMs have knowledge cutoffs, can hallucinate, and cannot access private or real-time data. RAG solves this by retrieving relevant external knowledge at inference time and injecting it into the prompt.

---

## Problems RAG Solves

1. **Knowledge cutoff** — model does not know recent events or internal docs
2. **Hallucination** — model invents plausible but wrong answers
3. **Private / enterprise data** — data that cannot be fine-tuned into the model
4. **Updatability** — change the knowledge base without retraining
5. **Citations & grounding** — answers can point to source chunks

---

## Basic RAG Flow

```
User query
    ↓
Embed query
    ↓
Retrieve top-k relevant chunks from vector DB
    ↓
Augment prompt with chunks
    ↓
LLM generates answer (grounded in retrieved context)
```

---

## When to Use RAG vs Fine-tuning vs Long Context

| Approach | Best for | Limitations |
|----------|----------|-------------|
| RAG | Dynamic, large, or private knowledge | Retrieval quality matters |
| Fine-tuning | Style, behavior, specialized reasoning | Expensive to update; knowledge can still be wrong |
| Long context | Small, static knowledge that fits in context | Cost & latency grow with length; still can miss details |

---

## Common Failure Modes

- Poor retrieval (wrong or irrelevant chunks)
- Bad chunking (splits mid-sentence or loses context)
- Over-retrieval (too much noise)
- No answer found but model still hallucinates
- Stale knowledge if index is not updated

---

## Key Interview Answer

RAG grounds the LLM in external knowledge at inference time so it can answer questions about private, recent, or domain-specific data without fine-tuning, while reducing hallucination and enabling citations.

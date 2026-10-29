# Context Window

The context window is the maximum number of tokens an LLM can process in a single request (input + output).

Examples: 8k, 32k, 128k, 200k, 1M+ tokens depending on the model.

---

## Why It Matters

- Everything the model “sees” in one call must fit inside the context window
- Includes system prompt, conversation history, retrieved chunks, tool results, and the generation itself
- Exceeding it causes truncation or an error

---

## Implications for AI Systems

- **RAG**: You can only inject a limited number of retrieved chunks
- **Agents**: Tool results and multi-step reasoning consume context
- **Long conversations**: History must be summarized or truncated
- **Cost & latency**: Larger contexts cost more and are slower

---

## Strategies When Context Is Limited

1. Better retrieval (fewer, more relevant chunks)
2. Summarization of conversation history
3. Hierarchical or multi-step retrieval
4. Use models with larger context windows
5. External memory (vector store, database) instead of stuffing everything into the prompt

---

## Context Engineering

The practice of carefully choosing what goes into the context window so the model has the right information without being overwhelmed.

Key levers:
- System prompt design
- Number and ranking of retrieved chunks
- Conversation summarization
- Tool result truncation

---

## Interview Points

- Context window is finite; everything competes for space
- RAG is partly a solution to limited context (retrieve only what is needed)
- Larger context does not automatically mean better answers — noise still hurts
- Production systems actively manage context (summarization, selective retrieval, truncation)

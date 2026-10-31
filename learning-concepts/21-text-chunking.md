# Text Chunking with Overlap (RAG Interview)

**Interview question:** Write code for chunking a text with a given `chunk_size` and `chunk_overlap`.

Chunking splits long documents into smaller pieces that fit embedding models and retrieval. Overlap keeps context across boundaries so a sentence or fact is not cut in half.

---

## Key Parameters

- **text**: Input string to split.
- **chunk_size**: Maximum characters (or tokens) per chunk.
- **chunk_overlap**: Number of characters shared between consecutive chunks.

**Why overlap?** It retains context across chunk boundaries, improving retrieval quality and helping the LLM generate more coherent answers. Typical overlap is 10–20% of chunk size.

---

## Simple Sliding-Window Implementation

```python
def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> list[str]:
    if chunk_size <= 0 or chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError("Invalid chunk_size or chunk_overlap")
    chunks = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + chunk_size, n)
        chunk = text[start:end]
        chunks.append(chunk)
        if end == n:
            break
        start = end - chunk_overlap
    return chunks

# Example
text = "Retrieval-Augmented Generation (RAG) combines retrieval with LLMs to generate accurate, context-aware responses."
chunks = chunk_text(text, chunk_size=40, chunk_overlap=10)
for i, c in enumerate(chunks, 1):
    print(f"Chunk {i}: {c}")
```

**Output example** (chunk_size=40, chunk_overlap=10):

- Chunk 1: Retrieval-Augmented Generation (RAG) combines
- Chunk 2: (RAG) combines retrieval with LLMs to generate
- Chunk 3: to generate accurate, context-aware responses.

---

## Production Notes

- Prefer **token-based** size (not pure characters) for LLM/embedding limits.
- Use **RecursiveCharacterTextSplitter** (LangChain) or similar that respects sentence/paragraph boundaries instead of pure fixed-size cuts.
- Common starting point: 256–512 tokens, 10–20% overlap.
- Evaluate with real queries (RAGAS or custom) and tune; too much overlap wastes index space and can dilute rankings.
- For structured docs, prefer heading- or section-aware chunking over pure sliding window.

---

## Interview Tips

- Mention that naive fixed-size can break mid-sentence; recursive splitters are better.
- Overlap is a safety net, not a substitute for good boundary detection.
- Relate to context window and embedding model limits.
- Source style: Archi Pathak / Accenture-style interview question.

---

*Added as daily dose concept. Cross-links: 02-why-rag.md, 14-hybrid-rag.md, 17-advanced-rag-patterns.md.*

# Hybrid RAG & Reranking

Pure vector search is good at semantic similarity but can miss exact keywords, names, or codes. Hybrid search combines dense (embedding) and sparse (BM25/keyword) retrieval, then reranks.

---

## Why Hybrid

- Vector: good for meaning ("refund policy" matches "money back rules")
- Keyword/BM25: good for exact terms, IDs, product names
- Together they cover more cases

---

## Typical Pipeline

1. Retrieve top-k from vector store
2. Retrieve top-k from BM25 / sparse index
3. Fuse results (e.g., Reciprocal Rank Fusion — RRF)
4. Rerank the fused list with a cross-encoder or LLM
5. Pass top-n to the generator

---

## Reranking

A stronger (but slower) model scores each (query, chunk) pair. Improves precision at the top of the list.

---

## Industry Reality

Most production RAG systems that need high quality use some form of hybrid + reranking. Pure vector is often the starting point, not the final design.

---

## Interview Points

- Hybrid search combines semantic and lexical retrieval
- RRF is a common fusion method
- Rerankers improve the final context quality
- Metadata filtering and hybrid are usually combined in enterprise systems

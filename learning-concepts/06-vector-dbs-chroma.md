# Vector Databases & Chroma

A vector database stores embeddings and enables fast similarity search (nearest neighbor search).

---

## Why Vector Databases

- Naive search over millions of vectors is too slow
- Vector DBs use approximate nearest neighbor (ANN) indexes (HNSW, IVF, etc.)
- Support metadata filtering alongside vector search
- Persist embeddings so you do not re-embed everything on every restart

---

## Popular Options

| Database | Notes |
|----------|-------|
| **Chroma** | Simple, local-first, great for learning and small-medium apps |
| **FAISS** | Facebook library, very fast, often used in-memory |
| **Qdrant** | Feature-rich, good filtering, open-source |
| **pgvector** | PostgreSQL extension — useful when you already have Postgres |
| **Pinecone / Weaviate** | Managed / cloud options |

---

## Chroma

Chroma is an open-source embedding database that is easy to get started with.

### Basic Concepts

- **Collection**: Named group of embeddings (like a table)
- **Documents**: The original text chunks
- **Embeddings**: The vectors
- **Metadata**: Extra fields for filtering (source, date, department, etc.)
- **IDs**: Unique identifiers

### Typical Workflow

1. Create a collection
2. Add documents + embeddings + metadata
3. Query with a text or embedding + optional filters
4. Get top-k most similar results

### Strengths

- Simple Python API
- Can run fully local
- Good for prototypes and many production use cases
- Supports metadata filtering

### Limitations

- Not as scalable or feature-rich as specialized production vector DBs for very large scale
- Persistence and concurrency need attention in multi-process setups

---

## Hybrid Search

Many systems combine:
- Dense (vector) search for semantic similarity
- Sparse (BM25 / keyword) search for exact matches

Then re-rank the combined results.

---

## Interview Points

- Vector DBs enable efficient similarity search over embeddings
- Chroma is a popular lightweight choice for learning and many apps
- Always store metadata so you can filter (tenant, department, date, etc.)
- Re-embedding is required if you change the embedding model
- Hybrid search often outperforms pure vector search

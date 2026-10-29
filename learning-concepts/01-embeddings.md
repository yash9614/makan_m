# Embedding Models

Embedding models convert text (or other modalities) into dense numerical vectors that capture semantic meaning.

Similar meanings produce vectors that are close together in vector space.

---

## Why Embeddings Matter

- Enable semantic search (not just keyword matching)
- Power RAG (retrieve relevant chunks)
- Used in clustering, classification, recommendation
- Foundation for most modern retrieval systems

---

## How They Work

1. Input text is tokenized
2. Model (transformer-based) processes the tokens
3. Output is a fixed-size vector (e.g., 384, 768, 1536 dimensions)
4. Similarity is measured with cosine similarity or dot product

---

## Popular Embedding Models

| Model | Notes |
|-------|-------|
| `text-embedding-3-small` / `large` (OpenAI) | Strong general performance |
| `sentence-transformers` (e.g., all-MiniLM-L6-v2) | Fast, local, open-source |
| `bge-` series, `e5-` | Strong open models |
| Multimodal (CLIP, SigLIP) | Text + image |

---

## Key Considerations

- **Dimension**: Higher often better but more expensive
- **Normalization**: Many models expect L2-normalized vectors
- **Domain**: General vs code vs domain-specific
- **Latency & cost**: Local vs API
- **Chunk size compatibility**: Embedding quality drops on very long or very short text

---

## In RAG

Documents are chunked → each chunk is embedded → stored in a vector database. At query time the query is embedded and nearest neighbors are retrieved.

---

## Interview Points

- Embeddings capture meaning, not exact keywords
- Cosine similarity is preferred for normalized embeddings
- Different models are not interchangeable without re-embedding
- Always re-embed when you change the embedding model

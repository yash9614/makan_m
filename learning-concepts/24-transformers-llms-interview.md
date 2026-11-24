# Transformers & LLMs — Interview Questions (Day 27)

Concise answers for the 10 classic Transformers & LLM questions.

---

### 1. What is a Transformer, and why did it replace RNNs?
A Transformer is a neural architecture based on self-attention that processes an entire sequence in parallel. It replaced RNNs because:
- Training is highly parallel (no sequential recurrence)
- It handles long-range dependencies directly (constant path length between any tokens)
- It scales better on modern GPUs

Trade-off: quadratic cost in sequence length.

### 2. Explain self-attention in simple terms.
Each token looks at every other token in the sequence and decides how much information to take from each one. The output for a token is a weighted combination of all tokens, where the weights come from how relevant they are to the current token.

### 3. What are Query, Key, and Value in attention?
Learned projections of each token embedding:
- **Query (Q)**: what the current token is looking for
- **Key (K)**: what each token offers / how it can be matched
- **Value (V)**: the actual content that gets aggregated

Attention score = softmax(Q · Kᵀ / √d) · V

### 4. Why do Transformers need positional encoding?
Self-attention is permutation-invariant — it treats the input as a set and has no built-in sense of order. Positional encodings (sinusoidal, learned, or rotary/RoPE) inject position information so the model knows word order.

### 5. What are tokens, and how does tokenization work?
Tokens are the atomic units the model sees (subwords, words, or characters). Tokenization (BPE, SentencePiece, etc.) splits raw text into these units and maps them to integer IDs. The model never sees raw text — only token IDs and their embeddings.

### 6. What is a context window, and why does it matter?
The maximum number of tokens the model can process in one forward pass (prompt + generated output). Everything must fit: system prompt, history, retrieved chunks, and generation. Exceeding it requires truncation, summarization, or external memory. Larger windows cost more memory and latency.

### 7. What do temperature and top-p control in LLM generation?
- **Temperature**: scales the logits before softmax. Lower = more deterministic/factual; higher = more creative/random.
- **Top-p (nucleus sampling)**: keeps the smallest set of tokens whose cumulative probability ≥ p, then samples from that set. Controls diversity without fixed top-k cutoffs.

### 8. Why do LLMs hallucinate, and how do you reduce it?
Hallucinations happen because the model predicts the next token from statistical patterns, not grounded truth. Causes: knowledge cutoff, weak retrieval, ambiguous prompts, overconfidence.

Reduction techniques: RAG with strong retrieval, grounded generation, citations, lower temperature, structured outputs, evaluation (RAGAS), human feedback, and guardrails.

### 9. Fine-tuning vs RAG: when would you use which?
| | RAG | Fine-tuning |
|---|-----|-------------|
| Best for | Dynamic, private, or frequently changing knowledge | Style, behavior, specialized reasoning, format |
| Update cost | Cheap (update index) | Expensive (retrain) |
| Citations | Natural | Harder |
| Latency | Extra retrieval step | No extra step |

Many production systems use both.

### 10. What are embeddings, and how do they power semantic search?
Embeddings are dense vector representations of text (or other modalities) produced by a model. Similar meanings map to nearby vectors. Semantic search embeds the query and retrieves the closest vectors from an index (via cosine similarity or ANN indexes like HNSW). This powers RAG retrieval.

---

*Added from Day 27 Transformers & LLMs Interview Series. Cross-links: 01-embeddings.md, 02-why-rag.md, 03-decoding-params.md, 04-context-window.md, 15-interview-questions.md.*

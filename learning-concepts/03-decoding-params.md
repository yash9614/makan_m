# Decoding Parameters: Temperature, Top-k, Top-p

These parameters control how an LLM samples the next token. They do not change the model's knowledge; they change the randomness and diversity of the output.

---

## Temperature

- Scales the logits before softmax
- **Low (0.0–0.3)**: Deterministic, focused, good for factual or code tasks
- **Medium (0.7)**: Balanced creativity
- **High (1.0+)**: More random, creative, higher risk of nonsense

---

## Top-k

- Keep only the k most likely tokens and sample from them
- Example: top-k = 50 → only consider the 50 highest-probability tokens
- Limits the long tail of unlikely tokens

---

## Top-p (Nucleus Sampling)

- Keep the smallest set of tokens whose cumulative probability ≥ p
- Example: top-p = 0.9 → include tokens until their probabilities sum to 0.9
- Adapts to the distribution (more tokens when the model is uncertain)

---

## Typical Settings

| Use case | Temperature | Top-p | Notes |
|----------|-------------|-------|-------|
| Factual / RAG | 0.0 – 0.3 | 0.9 | Prefer low randomness |
| Chat | 0.7 | 0.9 | Balanced |
| Creative writing | 0.9 – 1.2 | 0.95 | Higher diversity |
| Code | 0.0 – 0.2 | 0.95 | Deterministic preferred |

---

## Key Points

- Temperature and top-p are usually used together; top-k is less common now
- Setting temperature = 0 is equivalent to greedy decoding (always pick highest probability token)
- These do not affect retrieval or tool calling reliability the same way — tool calling often works best with low temperature
- For production RAG or agent systems, prefer lower temperature to reduce hallucination

---

## Interview Answer

Temperature controls randomness by scaling logits. Top-p (nucleus sampling) dynamically selects the smallest set of tokens whose cumulative probability exceeds a threshold. Lower values produce more focused, factual outputs; higher values increase diversity and creativity.

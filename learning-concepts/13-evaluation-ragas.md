# Evaluation & RAGAS

You cannot improve what you do not measure. Evaluation tells you whether your RAG or agent system is actually getting better.

---

## Why Evaluation Matters

- Which model is best for this use case?
- Is the answer correct (vs ground truth)?
- Is the answer grounded in the retrieved documents (no hallucination)?
- Did the retriever fetch relevant chunks?

---

## Common RAG Metrics

| Metric | What it checks |
|--------|----------------|
| **Correctness** | Answer vs reference answer |
| **Relevance** | Answer vs question |
| **Groundedness / Faithfulness** | Answer supported by retrieved docs |
| **Retrieval relevance** | Retrieved chunks vs question |

LLM-as-a-judge is the practical way to score these at scale.

---

## RAGAS

Open-source framework that implements the above metrics (and more) for RAG systems. Widely used in industry for automated evaluation.

---

## LangSmith

LangChain’s platform for tracing, datasets, and experiments. You create a dataset of (input, ground-truth), run your app, and attach evaluators.

---

## Production Practice

- Start with a small golden dataset
- Run evaluation on every major change
- Use the lowest-scoring metric as the improvement target
- Combine automated judges with human review for high-stakes answers

---

## Interview Points

- Evaluation needs ground truth + metrics + a judge (usually LLM)
- Four classic RAG metrics: correctness, relevance, groundedness, retrieval relevance
- LangSmith for tracing + experiments; RAGAS for metric implementations
- Without evaluation you cannot confidently ship or iterate

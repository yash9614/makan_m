# AI Vocabulary for Beginners (21 Core Terms)

Clean, beginner-friendly explanations of essential GenAI and Agentic concepts, drawn from mayank953/python-ai-crash-course (YouTube course notes).

**Source:** [mayank953/python-ai-crash-course](https://github.com/mayank953/python-ai-crash-course) — AI Concepts section + interactive site.

No code in the AI section itself (vocabulary focus). Python practice notebooks and checkpoint assignments are in the same repo under `python/` and `assignments/`.

---

## Stage 1: What You Already Use

- **LLM**: Next-token predictor trained on massive text. Pattern memory, not lookup. Models vary in size/cost.
- **Prompting**: Zero-shot (instruction only) vs few-shot (with examples). Examples are the cheapest reliability upgrade.
- **Temperature**: Controls randomness. Low = reliable/repeatable; high = creative/risky.
- **Hallucination**: Fluent but factually wrong output. Mitigate with RAG, sources, lower temp, verification.
- **Context Engineering**: Everything the model sees (history, docs, tools, preferences) — not just the typed prompt.

## Stage 2: Under the Hood

- **Tokens**: Sub-word units the model processes. Cost, speed, and limits are token-based.
- **Vectors & Embeddings**: Meaning as coordinates. Similar meaning = nearby vectors. Powers semantic search and RAG.
- **Context Window**: Max tokens the model can consider at once. Oldest content drops when full.
- **Model Parameters**: Billions of weights that encode learned knowledge. More ≠ automatically better for every task.
- **Attention Mechanism**: How the model weighs relevant words in context (e.g., disambiguating "bank").
- **Transformer**: The architecture (attention layers) that powers most modern LLMs.

## Stage 3: How It Learns

- **Pretraining**: Massive next-token prediction on unlabeled text.
- **Fine-Tuning**: Further training on focused examples for domain/style specialization.
- **RLHF**: Human preference ranking to make responses more helpful/safe.

## Stage 4: Smarter Without Retraining

- **RAG**: Retrieve relevant docs → inject into prompt → generate grounded answer. Open-book vs closed-book.
- **MCP**: Open standard for exposing tools/resources/prompts so any client can use them (USB-C for AI tools).

## Stage 5: Beyond Chat

- **AI Agents**: Goal-driven loop (perceive → reason → act with tools → observe) vs pure chatbot.
- **Multimodal**: Text + image + audio + video in one model.
- **Reasoning Models**: Extra test-time compute for step-by-step thinking (better for multi-step problems).
- **Small Language Models**: Faster/cheaper specialized models (often distilled).
- **AGI vs ASI**: Artificial General Intelligence vs Artificial Superintelligence (aspirational vs speculative).

## Hands-On Activities (from source)

Each concept includes a short "Try it" exercise (e.g., temperature comparison, attention visualization, RAG sentence finding, agent loop sketch).

## Assignments & Code

- Python fundamentals: theory + code notebooks in `python/` folders.
- Checkpoint assignments (with solutions): `assignments/A1` to `A6` covering setup through functions.
- Useful if strengthening Python before deeper GenAI/Agentic work.

## Interview Angle

These terms appear constantly. Being able to explain them simply (with the analogies above) is a strong signal.

Full interactive version and diagrams: see the source repo and [ai-terms-explained.netlify.app](https://ai-terms-explained.netlify.app).

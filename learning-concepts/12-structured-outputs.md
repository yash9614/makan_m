# Structured Outputs & Pydantic

Force the LLM to return data in a fixed schema (JSON that validates) so downstream code can use it reliably.

---

## Why It Matters

- Free-text answers are hard to parse and error-prone
- Agents, tools, evaluation, and APIs need predictable fields
- Pydantic validates types at runtime and gives clear error messages

---

## Options

1. **Pydantic BaseModel** (recommended) — runtime validation + Field descriptions
2. **TypedDict** — lighter, no runtime checks
3. **Dataclass**

Use `.with_structured_output(Schema)` on the model or `response_format` on agents.

---

## Best Practices

- Give every field a clear `Field(description=...)`
- Prefer strict schemas for production
- Handle validation errors (retry, fallback, or reject)
- Nested models work for complex objects (e.g., list of actors inside a movie)

---

## Industry Use

- Extracting entities from documents
- Tool arguments
- Evaluation judges (score + explanation)
- API responses from agents
- Data pipelines that feed other systems

---

## Interview Points

- Structured output turns free-text generation into typed, usable data
- Pydantic is the standard for validation in the Python GenAI stack
- Always include descriptions; they guide the model
- Critical for reliable agents and evaluation pipelines

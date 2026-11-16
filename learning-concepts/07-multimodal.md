# Multimodal Models

Multimodal models can process and generate more than one type of data — most commonly text + images, but also audio, video, etc.

---

## Common Capabilities

- **Vision-Language Models (VLMs)**: Understand images + text (describe image, answer questions about image, OCR)
- **Text-to-Image**: Generate images from text prompts
- **Image-to-Text**: Captioning, document understanding
- **Audio**: Speech-to-text, text-to-speech, audio understanding

---

## How They Differ from Text-Only Models

- Accept multiple input modalities in the same context
- Often use separate encoders (vision encoder + language model) that are aligned
- Embeddings or tokens from different modalities live in a shared space

---

## Use Cases in AI Systems

- Document understanding (PDFs with tables, charts, scanned pages)
- Visual question answering
- Product search (image + text)
- Accessibility tools
- Agents that can “see” screenshots or UI

---

## Considerations

- Higher cost and latency than text-only
- Context window is still limited (images consume many tokens)
- Quality varies significantly by model
- Need careful prompt engineering for reliable structured output

---

## Interview Points

- Multimodal models process more than one modality (typically text + vision)
- Useful for document-heavy RAG or agents that need to understand screenshots/PDFs
- Still subject to the same context window and hallucination constraints
- Often more expensive; use only when visual understanding is required

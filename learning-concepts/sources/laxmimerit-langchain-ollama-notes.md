# Notes from laxmimerit/Langchain-and-Ollama

Practical local-LLM + LangChain tutorial series.

## Structure

- Ollama setup and Modelfile
- Prompt templates
- Chains
- Output parsing
- Chat message memory
- Build your own chatbot (streaming)
- Document loaders:
  - PDF
  - Webpage
  - Office files (PPT, Excel, Word)
  - MarkItDown (Microsoft)
  - Docling (IBM) — strong for tables and figures

## Useful Takeaways

- Local inference with Ollama is straightforward for learning and privacy-sensitive use
- Docling and MarkItDown are better than basic loaders for complex PDFs and Office docs (preserve tables/structure)
- Streaming chat is easy to add once the basic chain works
- Good companion to cloud-based RAG notebooks when you want offline or cost-free experimentation

Reference: [laxmimerit/Langchain-and-Ollama](https://github.com/laxmimerit/Langchain-and-Ollama)

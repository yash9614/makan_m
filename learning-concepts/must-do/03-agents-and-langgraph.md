# Must-Do: Agents & LangGraph

## Essential Projects / Exercises

1. **Tool-calling agent (Wikipedia / Arxiv)**  
   Source: `generative-ai-learning-path/04-Agents-and-LangGraph`

2. **LangGraph basics + conditional edges**  
   Source: `agentic-ai-learning-path/02-langgraph-basics` + `03-react-and-tool-calling`

3. **Agentic RAG**  
   Source: `Ultimate-RAG-Bootcamp/07-agentic-rag`

4. **Human-in-the-loop with interrupts**  
   Source: `agentic-ai-learning-path/05-human-in-the-loop`

5. **Cold-chain FDE agent (SQL + weather API + SOP vector)**  
   Source: `nimowhyca/cold-chain-logistics-FDE-Project` (reference implementation)

6. **Project Streak — RAG + MCP + FastAPI**  
   Source: `yash9614/project_streak_`  
   Progressive build: tools → RAG (Chroma) → MCP server → FastAPI client + Streamlit

## Must-Do Checklist

- [ ] Build a ReAct agent with at least 2 tools
- [ ] Add a max-iteration limit and error handling
- [ ] Implement one HITL gate
- [ ] Persist state with a checkpointer
- [ ] Create one production-style tool with least privilege (e.g., SELECT-only SQL)
- [ ] Run the Project Streak stack (MCP server + FastAPI + Streamlit) and add one new tool

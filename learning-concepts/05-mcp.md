# MCP (Model Context Protocol)

MCP is an open protocol that standardizes how AI applications (hosts) connect to external tools, data sources, and prompts (servers).

It allows models to discover and call tools in a consistent way instead of every integration being custom.

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Host** | The application that uses the LLM (e.g., Claude Desktop, your FastAPI app) |
| **Client** | Component inside the host that speaks MCP |
| **Server** | Exposes tools, resources, or prompts |
| **Tool** | A function the model can call (with schema) |
| **Resource** | Data the model can read (files, DB rows, etc.) |
| **Prompt** | Reusable prompt templates |

---

## Basic Tool-Calling Loop

```
1. Host lists available tools from MCP server
2. LLM decides to call a tool (with arguments)
3. Host executes the tool via MCP
4. Result is returned to the LLM
5. LLM continues reasoning or calls another tool
```

---

## Transports

- **stdio** — local process (common for desktop)
- **SSE / HTTP** — remote servers
- Others emerging

---

## Why MCP Matters

- Standardized tool interface
- Reusable servers across different hosts
- Easier security and permission control
- Growing ecosystem of ready-made MCP servers

---

## Security Considerations

- Tools can have side effects (write data, send emails, etc.)
- Always apply authentication and authorization (JWT scopes, user permissions)
- Beware of confused deputy problems when forwarding tokens
- Validate tool inputs

---

## Interview Answer

MCP is a protocol that lets AI applications discover and invoke external tools, resources, and prompts through a standardized interface. It replaces ad-hoc tool integrations with a consistent client-server model, making agents more modular and interoperable.

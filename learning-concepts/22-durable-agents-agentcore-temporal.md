# Durable Production Agents: AWS Bedrock AgentCore + Temporal

**Source:** Krish Naik Academy session — “Agents That Never Die: Durable Production Agents on AWS Bedrock AgentCore + Temporal” (Nov 4, 2026).

Production AI agents must survive crashes, recover state, handle retries, and complete long-running tasks. Combining Amazon Bedrock AgentCore with Temporal provides a durable, cloud-native foundation.

---

## Why Durable Execution Matters

- Agents do more than reason and call tools: they wait for humans, run multi-step workflows, call flaky external systems, and run for minutes to days.
- Process crashes, container restarts, or serverless scale-to-zero must not lose progress.
- Temporal provides durable workflows with automatic replay from event history; AgentCore supplies managed AWS runtime, tools, identity, memory, and observability.

---

## Amazon Bedrock AgentCore (Key Components)

| Component | Role |
|-----------|------|
| **Runtime** | Secure, serverless, session-isolated microVM environment for agents/tools. Supports long-running sessions (up to ~8 hours), fast cold starts, and framework-agnostic hosting. |
| **Gateway** | Converts APIs, Lambda, and services into MCP-compatible tools with unified discovery and security. |
| **Identity** | Agent and user identity, inbound auth (Cognito, Entra, Okta, IAM), outbound credential vault (OAuth/API keys) so agents never hold long-lived secrets. |
| **Memory** | Short-term (session events) and long-term (extracted facts, preferences, summaries) with sharing across agents. |
| **Observability** | Built-in traces, metrics, and logs (OpenTelemetry-compatible) via CloudWatch for reasoning steps, tool calls, and performance. |
| **Tools** | Code Interpreter (sandboxed code execution), Browser (managed Chrome), and others. |
| **Policy** | Temporal (session-aware) policies and rate limiting at the gateway for stateful authorization. |

---

## Temporal + AgentCore Pattern

1. **Temporal Workflow = durable agent loop**  
   Coordinates model calls, tool use, retries, timeouts, human-in-the-loop signals, and long waits. Progress is recorded in event history and can be replayed after any failure.

2. **Activities = model calls and tool calls**  
   LLM invocations, Code Interpreter, Gateway tools, and custom functions run as Activities so they can be retried independently.

3. **Serverless Workers on AgentCore Runtime**  
   Temporal starts Worker capacity on demand inside AgentCore Runtime sessions. Compute scales to zero when idle; workflows continue across Worker replacements.

4. **Strands Agents integration**  
   Strands agent loop can be wrapped so model and tool calls automatically become Temporal Activities while keeping the familiar Strands programming model.

5. **Human-in-the-loop & timers**  
   Workflows can wait on signals or durable timers for hours/days with no compute cost.

---

## Key Learning Objectives (from the session)

- Explore AgentCore Runtime, Gateway, Identity, Memory, and Observability
- Build agents with Strands Agents and Code Interpreter
- Design Temporal workflows, activities, event history, and replay
- Implement durable execution, retries, timeouts, and crash recovery
- Handle long-running tasks with durable timers and HITL signals
- Architect serverless workers and resilient agent execution
- Clear boundaries between state, orchestration, tools, and recovery

---

## Interview / Production Talking Points

- **Why Temporal?** Durable execution, automatic retries, workflow history for observability and recovery, support for long-running and human-gated processes.
- **Why AgentCore?** Managed AWS runtime with session isolation, identity, memory, gateway, and observability without operating your own infrastructure.
- **Complementary roles:** AgentCore = compute + agent platform services; Temporal = durable orchestration and recovery layer.
- Common failure modes without durability: lost progress on crash, inconsistent retries, inability to pause for approval, high cost of always-on workers.

---

## References

- Temporal: [Durable agents on AgentCore](https://docs.temporal.io/guides/durable-agent-on-agentcore), [Serverless Workers on AgentCore](https://docs.temporal.io/serverless-workers/agentcore)
- AWS: AgentCore docs (Runtime, Gateway, Identity, Memory, Observability)
- Community examples: temporal-community durable agent harnesses

---

*Added from Krish Naik Academy registration. Cross-links: 10-agentic-mindset.md, 11-langgraph-basics.md, 18-deep-agents.md, 20-production-fde-agent-patterns.md.*

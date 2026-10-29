# JWT (JSON Web Token)

A compact, secure way to transmit information between parties as a JSON object. Commonly used for authentication and authorization in web apps, mobile apps, APIs, and AI systems.

JWT is **not** used for training models. It is used to **secure** AI applications, APIs, agents, and multi-tenant systems.

---

## Structure

A JWT looks like this:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJ1c2VySWQiOjEyMywicm9sZSI6ImFkbWluIn0
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

It has three parts separated by dots:

### 1. Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

### 2. Payload (Claims)
```json
{
  "userId": 123,
  "role": "admin"
}
```

### 3. Signature
Generated using a secret key (HMAC) or private key (RSA/ECDSA). Ensures the token has not been tampered with.

---

## Why JWT?

JWT allows systems to verify a user's identity **without storing session data on the server** (stateless).

**Traditional session flow**
```
User → Login
Server → Store session in DB
Server → Send session ID
```

**JWT flow**
```
User → Login
Server → Create JWT
Server → Send JWT
User → Sends JWT with every request
Server → Verifies JWT signature
```

Because the token contains the claims, the server can stay stateless.

---

## JWT in AI Projects

### 1. User Authentication for AI Apps

```
Frontend
   ↓
AI Backend
   ↓
LLM (OpenAI, Azure OpenAI, etc.)
```

Flow:
1. User logs in → Backend generates a JWT.
2. Frontend stores it.
3. Every chat request sends the JWT.

Example header:
```
Authorization: Bearer <JWT_TOKEN>
```

The backend verifies the token before allowing access to the LLM.

### 2. Protecting AI APIs

```
POST /generate-summary
```

You do not want anonymous users consuming expensive AI resources.

```
User
 ↓
JWT Verification
 ↓
AI Service
 ↓
LLM
```

### 3. Role-Based Access Control (RBAC)

Example payload:
```json
{
  "userId": "123",
  "role": "premium"
}
```

Backend logic:
```python
if token["role"] == "premium":
    allow_gpt4()
else:
    allow_basic_model()
```

Use cases:
- Free users → smaller / cheaper model
- Premium users → advanced models
- Admins → fine-tuning or admin features

### 4. Multi-Tenant AI Applications

Example payload:
```json
{
  "userId": "u123",
  "tenantId": "companyA"
}
```

The backend uses `tenantId` to:
- Load company-specific data
- Restrict access to documents
- Enforce data isolation

```
Company A User → Can access Company A documents
Company B User → Cannot access Company A documents
```

### 5. RAG (Retrieval-Augmented Generation)

JWT can carry department or permission claims:
```json
{
  "userId": "101",
  "department": "finance"
}
```

Retrieval layer filters documents:
```
WHERE department = 'finance'
```

This prevents users from retrieving unauthorized information.

### 6. AI Agent Systems

Agents that can read emails, access documents, or query databases need permissions.

Example payload:
```json
{
  "userId": "123",
  "permissions": [
    "read_docs",
    "read_email"
  ]
}
```

The agent checks the permissions before performing actions.

### 7. Microservices-Based AI Architecture

```
Frontend
   ↓
Auth Service
   ↓
API Gateway
   ↓
AI Service
   ↓
Vector DB
```

The JWT travels across services. Each service can independently verify identity, role, and permissions without repeatedly querying a database.

---

## Example AI Chat Application Flow

1. User logs in
2. Backend creates JWT
   ```json
   {
     "userId": "123",
     "role": "premium"
   }
   ```
3. User sends message with
   ```
   Authorization: Bearer <JWT>
   ```
4. AI Backend verifies JWT
5. Backend checks:
   - Is the user valid?
   - Is the premium model allowed?
6. Call LLM
7. Return response

---

## Advantages of JWT in AI Projects

- Stateless authentication
- Faster API requests (no session lookup)
- Secure identity verification
- Supports multi-tenant AI systems
- Enables role-based access control
- Works well with microservices
- Protects expensive AI endpoints

---

## Common Claims

| Claim | Meaning |
|-------|---------|
| `sub` | Subject (usually user ID) |
| `iss` | Issuer |
| `aud` | Audience |
| `exp` | Expiration time |
| `iat` | Issued at |
| `role` / `permissions` | Authorization data |
| `tenantId` | Multi-tenant isolation |

---

## Security Notes

- Always verify the signature.
- Check `exp` (expiration).
- Validate `aud` (audience) when relevant.
- Do not put sensitive data (passwords, secrets) in the payload — it is only base64-encoded, not encrypted.
- Use short-lived tokens + refresh tokens for long sessions.
- Prefer HTTPS always.

---

## Simple Interview Answer

JWT (JSON Web Token) is a secure, signed token used for authentication and authorization. In AI projects, JWT is commonly used to authenticate users, secure AI APIs, implement role-based access control, manage tenants, protect RAG systems, and pass user identity and permissions between AI microservices without maintaining server-side sessions.

---

## Related Topics

- OAuth 2.0 / OpenID Connect
- API Gateway authentication
- MCP tool permissions and scopes
- RAG document filtering by user/tenant
- Confused deputy problem (especially relevant when forwarding tokens to tools)

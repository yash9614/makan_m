# n8n Code Review Workflow — Beginner README

Local practice workflow: take a GitHub pull request, send the diff to OpenAI, post a review comment back on the PR.

Repo used for the test PR:

- https://github.com/yash9614/ds-ml-case-studies
- Test PR: https://github.com/yash9614/ds-ml-case-studies/pull/1

n8n UI: http://localhost:5678

---

## Objective

When you click **Execute workflow**:

1. Read the files changed on PR `#1`
2. Turn those diffs into a prompt
3. Ask OpenAI to review the change
4. Post that review as a GitHub PR comment
5. Optionally add a label

You should then see the comment on the PR page.

This is a **manual local run**. It is not live automation yet. GitHub webhooks cannot reach `localhost`.

---

## What you need

- Docker + the compose file in `D:\Downloads\n8n`
- n8n running at `http://localhost:5678`
- OpenAI API key
- GitHub fine-grained token for `yash9614/ds-ml-case-studies` with:
  - Contents: Read
  - Pull requests: Read and Write
  - Issues: Read and Write
  - Metadata: Read
- An open PR (PR `#1` already exists)

---

## Start / stop n8n

```bat
cd /d D:\Downloads\n8n
docker compose up -d
```

Open http://localhost:5678

```bat
docker compose down
```

Keeps workflows. `docker compose down -v` wipes n8n data.

If the login page loops on HTTP, add this to the n8n service environment and recreate:

```yaml
- N8N_SECURE_COOKIE=false
```

---

## Target node chain

Use this exact order:

```text
Manual Trigger
  → Get file's Diffs from PR     (HTTP Request)
  → Create target Prompt from PR (Code)
  → Code Review agent
       ↳ OpenAI Chat Model
  → GitHub Robot                 (create review)
  → Add Label to PR              (optional)
```

Do **not** start from **PR Trigger**.

Leave **PR Trigger** deleted or disconnected. It needs a public URL. On localhost it throws:

```text
The Webhook can not work on "localhost"
```

Leave the Google Sheet tool disconnected or deleted for the first run.

---

## One-time setup

### 1. Credentials

**OpenAI**

1. Click **OpenAI Chat Model**
2. Create credential
3. Paste OpenAI API key
4. Pick a model
5. Save

**GitHub** (for GitHub Robot + Add Label)

1. Open **GitHub Robot**
2. Create GitHub credential
3. Paste the fine-grained token
4. Owner = `yash9614`
5. Repository = `ds-ml-case-studies`
6. Repeat the same credential on **Add Label to PR**

**HTTP diffs node**

1. Open **Get file's Diffs from PR**
2. Method = `GET`
3. URL (hardcoded for the test PR):

```text
https://api.github.com/repos/yash9614/ds-ml-case-studies/pulls/1/files
```

4. Authentication = Generic Credential Type → Header Auth
5. Set up credential:
   - Name = `Authorization`
   - Value = `Bearer YOUR_GITHUB_TOKEN`
6. Send Headers ON
   - `User-Agent` = `n8n`
   - `Accept` = `application/vnd.github+json`
7. Save

Do not leave this URL as:

```text
{{$json.body.sender.login}} / {{$json.body.repository.name}} / {{$json.body.number}}
```

That only works when a real GitHub webhook payload is the input. A Manual Trigger does not send that shape.

### 2. Wire the nodes

1. Manual Trigger output → Get file's Diffs
2. Get file's Diffs → Create target Prompt
3. Create target Prompt → Code Review
4. Code Review → GitHub Robot → Add Label
5. Save the workflow
6. Keep **Active** / **Publish** OFF

---

## Execute

1. Click **When clicking ‘Execute workflow’**
2. Click **Execute workflow**
3. Wait for green ticks
4. Click **Get file's Diffs** → Output should include `README.md` and a `patch`
5. Click **Code Review** → Output should be the AI text
6. Click **GitHub Robot** → Output should include a review / comment id
7. Refresh https://github.com/yash9614/ds-ml-case-studies/pull/1

Success = a new review comment on that PR.

---

## How to tell if it actually worked

n8n toast **Workflow executed successfully** is not enough.

| Check | Meaning |
|---|---|
| Green tick on Manual Trigger only | Almost nothing ran |
| Diffs node missing from the line | Review cannot see the PR |
| Diffs Output empty | URL / auth wrong |
| GitHub Robot Output empty / skipped | Comment was not posted |
| PR page has a new review | It worked |

If the PR still has 0 comments after a “success” toast, the HTTP node was out of the chain or GitHub Robot did not run.

---

## Common errors

| Error | What to do |
|---|---|
| Webhook can not work on localhost | Delete / ignore PR Trigger. Run from Manual Trigger. |
| No input data on HTTP node | Click Execute previous nodes, then Execute step. |
| 401 / Incorrect API key | OpenAI key or GitHub token is wrong. |
| 403 Resource not accessible | Token missing PR write permission. |
| 404 | Owner, repo, or PR number is wrong. |
| Authentication = None + rate limit | Add the Bearer header. |
| Google Sheet node red | Delete it for now. |

---

## Beginner learning path

Do these in order. Do not skip ahead to Activate.

1. Start n8n with Compose. Open `/`.
2. Click each node. Read the note on the canvas. Do not edit Code JS yet.
3. Add OpenAI + GitHub credentials.
4. Hardcode the diffs URL to PR `#1`.
5. Delete or ignore PR Trigger and Google Sheets.
6. Connect the six-step chain above.
7. Execute from Manual Trigger.
8. Read Output on every node left to right.
9. Confirm the comment on GitHub.
10. Change one sentence in the Code Review prompt. Run again. See the new comment.
11. Only later: put n8n on a public URL (`WEBHOOK_URL` + tunnel) and reconnect PR Trigger if you want auto-runs.

---

## What each node is for

| Node | Job |
|---|---|
| PR Trigger | Live GitHub webhook. Skip on localhost. |
| Manual Trigger | Starts a test run when you click Execute. |
| Get file's Diffs | `GET /repos/.../pulls/1/files` |
| Create target Prompt | Formats diffs into text for the model. |
| Code Review + OpenAI | Writes the review. |
| GitHub Robot | Posts the review on the PR. |
| Add Label | Optional label such as `ReviewedByAI`. |
| Google Sheet Best Practices | Optional style guide. Not required. |

---

## Later upgrade (not required now)

To make this fire on every new PR:

1. Expose n8n with a tunnel or custom domain
2. Set `WEBHOOK_URL=https://your-public-url/`
3. Recreate the GitHub PR Trigger
4. Put expressions back in the HTTP URL from the webhook payload
5. Turn the workflow Active

Until then, Manual Trigger + hardcoded PR `#1` URL is the correct beginner setup.

---

## Cheatsheet

```bat
cd /d D:\Downloads\n8n
docker compose up -d
```

http://localhost:5678

```text
Manual Trigger → HTTP diffs (PR #1) → Code prompt → OpenAI agent → GitHub review → Label
```

```bat
docker compose down
```

Verify here: https://github.com/yash9614/ds-ml-case-studies/pull/1

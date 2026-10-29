
Both are normal. Industry practice is **not** “always scratch” or “always import JSON.” Teams mix them.

## What people actually dod

**Start from a template / JSON when:**

- the problem is common (Slack alert, Google Sheet sync, webhook → CRM, invoice parse)
- you want the node wiring and error pattern, not a blank canvas
- a vendor, colleague, or [n8n templates](https://n8n.io/workflows/) already solved 80%
- you are learning n8n or demoing a pattern

**Build from scratch when:**

- the flow is company-specific (your auth, your schema, your approval chain)
- credentials, base URLs, and field names will not match any public template
- you need a small, clear workflow you can explain in review
- security / compliance says “don’t paste random community JSON”

**Typical real sequence:**

1. Import a template or JSON to steal the *shape*
2. Rip out sample credentials and hardcoded IDs
3. Rebuild connections, env vars, and error handling for *your* stack
4. Save that as *your* internal template

That last copy is what teams reuse, not the public file unchanged.

## JSON export in practice

n8n workflows are JSON. Export/import is the official sharing format.

Treat imported JSON like copied code:

- read every node before activating
- rotate any credentials that came with it (templates should not contain real secrets; some unofficial dumps do)
- check webhook paths, URLs, and `HTTP Request` destinations
- pin n8n version if the export is old (nodes get renamed)

Internal practice that scales:

- store JSON in git (`workflows/invoice-sync.json`)
- one workflow = one job
- credentials stay in n8n / env, not in the JSON
- document trigger, input, output, and failure path

## Thumb rule

| Situation | Default |
|---|---|
| Learning or spike | Ready-made template / JSON |
| Production for your company | Scratch, or template heavily rewritten |
| Repeatable internal pattern | Your own exported JSON, versioned |
| Client delivery | Template for speed, then customize and own it |

Ready-made JSON is a **starting point**, not a finished production artifact. From-scratch is cleaner when the workflow is simple. Importing is faster when the graph is large and the pattern is known. Mature setups do both: import to move, then make the workflow theirs.









Best local combo with **only OpenAI + GitHub**: a **repo briefing bot**. No Slack, no ngrok, no extra SaaS.

Public templates that need Slack/Sheets/webhooks fight you on localhost. Pull-based GitHub nodes + Manual Trigger work immediately.

## What to build

**“What’s going on in this repo?”**

1. Manual Trigger  
2. GitHub → get repo README / latest issues / open PRs  
3. OpenAI → one-page briefing (risks, stale PRs, suggested labels)  
4. Optional GitHub → comment on a PR or open a tracking issue  

Interesting, uses both keys, safe to test on your own repo.

Ready-made cousins if you want to import first:

- [Review GitHub PRs + label with OpenAI](https://n8n.io/workflows/11967-review-github-pull-requests-and-label-them-using-openai-gpt-4o-mini-and-slack/) — drop Slack  
- [Triage GitHub issues with OpenAI](https://n8n.io/workflows/15251-triage-github-issues-with-openai-categorization-and-embedding-based-duplicate-detection/) — needs a webhook; save for later  

## Local setup

```bat
cd /d D:\Downloads\n8n
docker compose up -d
```

Open [http://localhost:5678](http://localhost:5678)

In n8n:

1. **Credentials → OpenAI** → paste API key  
2. **Credentials → GitHub** → fine-grained token  

Token permissions on the target repo:

- Contents: Read  
- Issues: Read and Write  
- Pull requests: Read and Write  
- Metadata: Read  

## Fastest path: import a template, then strip it

In the editor: **+ Add workflow → … → Import from URL** (or Templates).

Pick the PR-review template. Then:

- delete Slack / Google Sheets nodes  
- change **GitHub Trigger** → **Manual Trigger** + **GitHub: Get many pull requests**  
- set owner/repo to *your* repo  
- attach your two credentials  
- **Execute workflow** (do not Activate yet)

You should see an AI summary of open PRs in the output panel.

## 6-node version if you build it yourself

```text
Manual Trigger
    → GitHub: Get many issues (state=open)
    → GitHub: Get many PRs (state=open)
    → Merge / Code (pack titles + bodies into one text)
    → OpenAI: Message a model
    → (optional) GitHub: Create issue  title="Weekly repo briefing"
```

Prompt that works well:

```text
You are a staff engineer. From these open issues and PRs, write:
1. 5-line health summary
2. PRs that look stale or risky
3. Issues that look like duplicates
4. Suggested labels per item (bug, docs, feature, chore)
Repo context is attached below.
```

Use a cheap model first (`gpt-4.1-mini` or whatever your OpenAI node lists).

## Local thumb rules

- **Manual / Schedule** on localhost. GitHub webhooks cannot reach `localhost:5678` without a tunnel.  
- Don’t Activate until a manual run looks right.  
- First write action should be a **comment**, not close/merge.  
- Keep `N8N_SECURE_COOKIE=false` if HTTP login loops.

## After it works

Next upgrade, still with the same two keys:

- Schedule every weekday 9:00 → create a private “briefing” issue  
- or: get one PR diff → OpenAI review → comment on that PR  

Start with the manual briefing. It is the least fragile ready-made pattern on a local n8n.

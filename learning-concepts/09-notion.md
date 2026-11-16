# Notion — Learning Module

A practical guide to Notion: core concepts, databases, organization patterns, and how it fits into AI / MCP workflows.

---

## What is Notion?

Notion is an all-in-one workspace that combines:
- Notes / docs (pages)
- Databases (structured data)
- Wikis
- Project management
- Lightweight databases and dashboards

Everything is a **block**. Pages contain blocks. Databases are special blocks that store structured records.

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Workspace** | Top-level container. You can have multiple. |
| **Page** | A document. Can contain text, headings, lists, embeds, databases, etc. |
| **Block** | Atomic unit of content (paragraph, heading, to-do, callout, database, etc.). |
| **Database** | Structured collection of pages (records) with properties. |
| **Property** | A field on a database item (text, select, date, relation, formula, etc.). |
| **View** | Different way of looking at the same database (Table, Board, Gallery, Calendar, List, Timeline). |
| **Relation** | Link between two databases. |
| **Rollup** | Aggregate values from a related database. |
| **Formula** | Calculated property. |

---

## Pages vs Databases

- **Pages** are free-form documents. Good for notes, meeting minutes, specs, wikis.
- **Databases** are for structured, repeating information (tasks, contacts, projects, knowledge base articles, logs).

A database item is itself a page. You can open any row and write long-form content inside it.

---

## Common Database Properties

| Property Type | Use Case |
|---------------|----------|
| Title | Name of the item (required) |
| Text / Rich text | Short notes |
| Select / Multi-select | Status, tags, priority |
| Date | Deadlines, created dates |
| Checkbox | Done / not done |
| Number | Quantity, score |
| Person | Assignee |
| Relation | Link to another database |
| Rollup | Sum, average, count from related items |
| Formula | Calculated values |
| Status | Special select optimized for progress |
| Files & media | Attachments |
| URL | Links |

---

## Views

- **Table** — spreadsheet-like
- **Board (Kanban)** — grouped by a select/status property
- **Gallery** — card view (great for visual items)
- **Calendar** — date-based
- **List** — simple list
- **Timeline** — Gantt-style

You can have multiple views of the same database with different filters, sorts, and groupings.

---

## Relations & Rollups (Power Features)

**Relation**: Connect items across databases.  
Example: Projects ↔ Tasks, or Knowledge Base ↔ Sources.

**Rollup**: Pull and aggregate data from the related database.  
Example: Show the number of open tasks on a Project page, or the average score of related items.

These two features turn Notion into a lightweight relational database.

---

## Organization Patterns

### 1. PARA (Projects, Areas, Resources, Archives)
- **Projects**: Time-bound outcomes
- **Areas**: Ongoing responsibilities
- **Resources**: Reference material
- **Archives**: Inactive items

### 2. Simple Wiki + Databases
- One master database for tasks or notes
- Linked databases on different pages with different filters/views
- Dashboards that embed multiple linked databases

### 3. Knowledge Base
- Database of articles with tags, status, owner
- Relations to source material or related topics
- Gallery or list view for browsing

### 4. Project Management
- Projects database + Tasks database (relation)
- Board view by status
- Timeline for scheduling

---

## Templates

Templates let you pre-fill page content and properties when creating a new item.  
Very useful for meeting notes, project briefs, bug reports, etc.

---

## Sharing & Permissions

- Share individual pages or databases
- Permission levels: Full access, Can edit, Can comment, Can view
- Guest access vs workspace members
- Public links (optional)

When using AI tools (Claude, MCP), the AI inherits the permissions of the account that authorized it.

---

## Notion + AI / MCP

Notion has an official hosted MCP server:

```
https://mcp.notion.com/mcp
```

Once connected (via Claude, Claude Code, Cursor, etc.), an AI can:
- Search your workspace
- Read pages and databases
- Create and update pages
- Add comments
- Work with structured data

**Best practices with AI**:
- Connect only the pages/databases you need
- Prefer the official hosted MCP over local self-hosted servers
- Use clear titles and properties so retrieval works well
- Keep important knowledge structured in databases rather than scattered free-form pages

---

## Useful Features for Knowledge Work

- **Synced blocks** — update once, reflect everywhere
- **Linked databases** — show the same data in multiple places with different filters
- **Buttons & automations** (Notion Automations) — trigger actions on property changes or schedules
- **Mentions & backlinks** — connect ideas
- **Full-text search** across the workspace
- **Version history** on pages

---

## Common Mistakes to Avoid

- Putting everything in free-form pages instead of databases when structure is needed
- Over-nesting pages (deep hierarchy becomes hard to navigate)
- Creating too many databases that should be relations
- Not using templates for recurring page types
- Ignoring relations/rollups and duplicating data
- Giving AI tools broad access without thinking about permissions

---

## Learning Path (Practical)

1. Create a simple page and practice blocks.
2. Build one database (tasks or notes) with 4–5 properties.
3. Create multiple views (Table + Board).
4. Add a second database and create a relation + rollup.
5. Build a simple dashboard page that embeds linked databases.
6. Create a template for a recurring item type.
7. Connect Notion MCP to Claude and try searching / creating a page.
8. Organize an existing set of notes into a database.

---

## Interview / Explanation Points

- Notion is block-based. Databases are structured collections of pages.
- Relations and rollups enable relational thinking without a full database.
- Views are just different presentations of the same data.
- For AI workflows, structured databases + clear properties make retrieval and updates more reliable than free-form pages.
- Official way to connect AI tools is via Notion MCP (`https://mcp.notion.com/mcp`).

---

## Related Modules

- [05-mcp.md](05-mcp.md) — Model Context Protocol
- [jwt.md](../jwt.md) — Authentication concepts (relevant for secure tool access)

---

*Living note. Expand with your own patterns and database schemas as you build systems.*

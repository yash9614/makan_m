# n8n — Docker Compose Cheatsheet

Project folder: `D:\Downloads\n8n`  
UI (usual local URL): [http://localhost:5678](http://localhost:5678)

Official docs: [Docker](https://docs.n8n.io/hosting/installation/docker) · [Compose](https://docs.n8n.io/hosting/installation/server-setups/docker-compose/)

---

## 0. First look at *your* file

```bat
cd /d D:\Downloads\n8n
dir
type docker-compose.yml
```

Also check `compose.yml` / `compose.yaml` if there is no `docker-compose.yml`.

Confirm:

- service name (often `n8n`)
- published port (almost always **5678**)
- volume for `/home/node/.n8n` (workflows + encryption key)

If the port mapping is `"5678:5678"`, the URL below is correct. If it is `"8080:5678"`, use `http://localhost:8080`.

---

## 1. Start

```bat
cd /d D:\Downloads\n8n
docker compose up -d
docker compose ps
docker compose logs -f
```

`-d` = background. `logs -f` = follow output; `Ctrl+C` only leaves the logs, it does **not** stop n8n.

Wait until logs look healthy, then open:

```text
http://localhost:5678
```

First visit: create the owner account. That user lives in the n8n volume, not in the compose file.

---

## 2. Everyday commands

| Action | Command |
|---|---|
| Start | `docker compose up -d` |
| Start + rebuild image | `docker compose up -d --build` |
| Status | `docker compose ps` |
| Logs | `docker compose logs -f` |
| Last 100 log lines | `docker compose logs --tail=100` |
| Restart | `docker compose restart` |
| Stop containers, keep data | `docker compose stop` |
| Stop + remove containers, **keep volumes** | `docker compose down` |
| Stop + **wipe workflows/credentials** | `docker compose down -v` |

Always run them from `D:\Downloads\n8n`.

---

## 3. Load / use it

1. Browser → `http://localhost:5678`
2. Sign in (or create owner user on first run)
3. New workflow → add nodes → **Execute step** or **Active** toggle for production-style runs
4. Webhooks are typically:

   ```text
   http://localhost:5678/webhook/<path>
   http://localhost:5678/webhook-test/<path>
   ```

If the editor never finishes loading, or login loops on HTTP:

- add to the n8n service `environment`:

  ```yaml
  - N8N_SECURE_COOKIE=false
  ```

- then `docker compose up -d`

`N8N_SECURE_COOKIE` defaults to true (HTTPS only). Local HTTP needs it false.

---

## 4. Stop / end session

Keep workflows for next time:

```bat
cd /d D:\Downloads\n8n
docker compose down
```

Containers go away. Named volumes stay. Next `up -d` restores the same workflows.

Delete n8n data too (workflows, credentials, encryption key):

```bat
docker compose down -v
```

After `-v` you get a blank n8n and must create the owner user again. Old saved credentials cannot be decrypted if the volume (and its encryption key) is gone.

---

## 5. Important local notes

- **Do not delete the n8n data volume** unless you mean to. It holds the encryption key. Lose it → saved credentials become unreadable even if you export/import workflows later.
- Default DB inside the container is **SQLite** in that volume. Postgres appears only if *your* compose file defines it.
- Port **5678** must be free. If it is taken:

  ```bat
  netstat -ano | findstr :5678
  ```

- Timezone for Cron nodes: `GENERIC_TIMEZONE=Asia/Kolkata` and `TZ=Asia/Kolkata` in `environment`.
- `.env` next to the compose file is picked up for `${VAR}` substitutions. Secrets belong there, not committed to git.
- n8n is **not** started with `python` or `uvicorn`. Only Docker Compose.

---

## 6. Quick debug

```bat
docker compose ps
docker compose logs --tail=80 n8n
docker compose exec n8n n8n --version
```

If `exec` service name fails, use the name from `docker compose ps`.

Cannot reach UI:

1. `docker compose ps` shows `running` / `healthy`
2. port mapping includes `5678`
3. try `http://127.0.0.1:5678`
4. set `N8N_SECURE_COOKIE=false` for plain HTTP

---

## 7. Disk / cleanup (optional)

Keep n8n data:

```bat
docker compose down
docker image prune -f
```

Wipe this stack’s data + unused images:

```bat
docker compose down -v
docker image prune -f
```

Do not run `docker system prune -af --volumes` unless you want other projects’ DBs gone too (Qdrant, etc.).

---

## 8. Minimal mental model

```text
docker compose up -d      →  start n8n
browser :5678             →  use n8n
docker compose down       →  stop, keep data
docker compose down -v    →  stop, erase data
```

Same pattern as Qdrant in `rag_api`: Compose starts the service, the UI is a URL, `down` ends the session, `down -v` frees the volume.

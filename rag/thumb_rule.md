## What each file is

| File | Job | Do you “run the API” with it? |
|---|---|---|
| `index.py` | One-shot job: PDF → embeddings → Qdrant | No. Run it **before** the server, or when the PDF changes. |
| `main.py` | Defines `app = FastAPI()` and mounts routers | No. Uvicorn **imports** this file. |
| `uvicorn main:app` | Starts the HTTP server | Yes. This is how you run FastAPI. |

`main:app` means: module `main.py`, variable `app` inside it.

## When to use what

**Index data (not a server):**

```bat
python index.py
```

Runs once, then exits. Qdrant must already be up.

**Run the API:**

```bat
uvicorn main:app --reload --env-file .env
```

- `main` = the file
- `app` = the FastAPI instance
- `--reload` = restart on code changes (dev only)
- `--env-file .env` = load secrets

Without reload (closer to production):

```bat
uvicorn main:app --host 0.0.0.0 --port 8000
```

You almost never do `python main.py` unless `main.py` itself contains `uvicorn.run(...)`.

## Thumb rule for any FastAPI project

1. Find the file that contains `app = FastAPI()`.
2. From the project root (the folder that makes imports work), run:

```bat
uvicorn <that_file>:<app_variable> --reload
```

Examples:

```bat
uvicorn main:app --reload
uvicorn app.main:app --reload
uvicorn src.api:app --reload
```

3. Databases, Qdrant, Redis, etc. are **separate processes**. Start them first (`docker compose up -d`). FastAPI does not start them for you.
4. Indexing / migrations / seed scripts (`index.py`, `alembic`, etc.) are **not** the server. Run them once, then start Uvicorn.
5. `--reload` is for local development. Don’t use it as your production command.

## For this project, order

```bat
docker compose up -d          # Qdrant
python index.py               # only if collection is missing / PDF changed
uvicorn main:app --reload --env-file .env
```

Then open `http://127.0.0.1:8000/docs`.

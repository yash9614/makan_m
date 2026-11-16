
https://github.com/yash9614/FastAPI-Projects_oo1/tree/main/vakil-vision


Let's test this project using swagger let's start with testing and understand the basics of this project and how it runs what are the utilities of this project and how to understand every end point


Vakil Vision is a small FastAPI contract-review API. You upload a PDF or TXT, it stores the extracted text in MongoDB, then an OpenAI call returns a structured reading under Indian contract law: summary, clauses, risk flags, and recommendations. It is a study aid, not legal advice. Swagger is built in at `http://127.0.0.1:8000/docs` once the app is running. This environment has no Docker or Mongo, so the steps below are what you run locally.

## What it does

```
PDF or TXT
    → POST /contracts/upload
    → save uploads/<uuid>.ext, extract text (PyPDF2 or plain TXT)
    → MongoDB collection contracts  (status: uploaded)
    → POST /analysis/analyse/{contract_id}
    → first 15,000 characters + JSON schema → gpt-4o-mini
    → MongoDB collection analysis
    → contract status becomes analyzed (or error)
```

Unlike a RAG app, the model sees the contract text itself, not retrieved chunks. The file is still named `gemini_analyse.py` because the course used Gemini; this copy calls OpenAI.

Stack: FastAPI, MongoDB (`vakil_vision`), PyPDF2, Pydantic, OpenAI. No auth. Max upload 10 MB. Allowed types: `.pdf`, `.txt`.

## How to run

From the project folder:

```bash
cd vakil-vision
cp app/.env.example app/.env
# put a real OPENAI_API_KEY in app/.env

docker compose up -d          # Mongo on localhost:27017
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Mongo must be up before uvicorn. Startup calls `init_db()`, which creates a unique index on `contracts.filename` and an index on `analysis.contract_id`. If Mongo is down, the process fails on import.

- App: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

`.env` keys:

```
MONGODB_URI=mongodb://localhost:27017/vakil_vision
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
```

Sample file already in the repo: `samples/sample_nda.txt` (NDA between TechVentures Pvt Ltd and InnoSoft Solutions LLP, with a non-compete and a one-sided liability cap).

## Layout

| Piece | Role |
|---|---|
| `app/main.py` | App, lifespan, `GET /`, mounts the two routers |
| `app/config.py` | Mongo URI, OpenAI key/model, 10 MB limit, `.pdf`/`.txt` |
| `app/database.py` | `contracts` and `analysis` collections |
| `app/models.py` | `Contact` (the contract; course name), `ClauseAnalysis`, `RiskFlag`, `AnalysisResult` |
| `app/routes/contracts.py` | Upload, list, get |
| `app/routes/analysis.py` | Analyse, list, get by analysis id, get by contract id |
| `app/service/document_parser.py` | Text extraction only |
| `app/service/gemini_analyse.py` | The only file that talks to OpenAI |
| `app/service/prompt.py` | JSON schema prompt. The clause/risk/summary prompts are unused |

Routes do HTTP and Mongo writes. Services do parsing and the model call.

## Swagger, in order

Open `/docs`. Operations are grouped as `contracts` and `analysis`. Click an operation, then Try it out, then Execute. The id you need is the 24-character Mongo ObjectId in the upload response, not the saved filename.

**1. `GET /`**  
Sanity check. Returns the app name and an endpoint map. No body.

**2. `POST /contracts/upload`**  
Choose `samples/sample_nda.txt`. Expect 200:

- `message`: file uploaded and processed
- `id`: the contract id, copy this
- `contract`: filename (uuid.txt), original name, `text_content`, `page_count` 1 for TXT, `word_count`, `status` `uploaded`, `upload_date`

Negative cases worth trying in the same form:

- `.docx` or no extension → 400, file type not allowed
- file over 10 MB → 400, size limit

**3. `GET /contracts/`**  
Lists contracts with `text_content` omitted. Confirm the new row and `status: uploaded`.

**4. `GET /contracts/{contract_id}`**  
Paste the id. Full text comes back. Bad id (not 24 hex chars) → 400. Unknown but valid ObjectId → 404.

**5. `POST /analysis/analyse/{contract_id}`**  
Paste the same id. This is the only call that spends an OpenAI request. Status moves `uploaded` → `analyzing` → `analyzed`. Response shape:

- `summary`, `contract_type` (should look like an NDA)
- `key_clauses[]`: `clause_title`, `clause_text`, `explanation`, `is_standard`
- `risk_flags[]`: `risk_title`, `description`, `risk_level` (`low`/`medium`/`high`/`critical`), `recommendation`, `clause_reference`
- `overall_risk_level`
- `recommendations[]`
- `id`: the analysis id

On the sample NDA, expect flags around the India-wide non-compete, employee non-solicit, one-sided indemnity, and the INR 10 lakh liability cap that only limits the company.

Failures:

- empty `OPENAI_API_KEY` → 500
- bad id → 400
- unknown contract → 404
- model or JSON failure → 502, and contract status is set to `error`

**6. `GET /analysis/contract/{contract_id}`**  
All analyses for that contract. Registered before `GET /analysis/{analysis_id}` on purpose, otherwise the word `contract` would be captured as an id.

**7. `GET /analysis/`**  
Every analysis in the database. Not listed on `GET /`, but it is in Swagger.

**8. `GET /analysis/{analysis_id}`**  
One analysis by its own id from step 5. Bad id → 400. Missing → 404.

There is no delete, update, or auth endpoint.

## Status machine

`uploaded` → `analyzing` → `analyzed`, or `error` if the model call or JSON parse fails. Same idea as a job state, not a user-editable field.

## Things that trip people up

- The path is British spelling: `/analysis/analyse/{contract_id}`, not `analyze`.
- The Pydantic model is `Contact`, not `Contract`.
- Only the first 15,000 characters are sent to the model.
- `response_format={"type": "json_object"}` forces JSON; Pydantic then builds `ClauseAnalysis` and `RiskFlag`. A schema mismatch becomes a 502.
- ObjectId is converted to a string before JSON. A Database object is compared with `None`, not used in `or`.
- Raw files land in `uploads/` (gitignored). Parsed text and analysis live in Mongo volume `vakil_mongo_data`.
- `CLAUSE_EXTRACTION_PROMPT`, `RISK_ASSESSMENT_PROMPT`, and `SUMMARY_PROMPT` are never called. Only `CONTRACT_ANALYSIS_PROMPT` is used.



This is a local walkthrough. Run the API on your machine, then hit every route in Swagger in the same order a client would. Each step is paired with the idea that step is teaching.

## 0. Start the stack

From the project folder:

```bash
cd vakil-vision
cp app/.env.example app/.env
```

Put a real key in `app/.env`:

```
MONGODB_URI=mongodb://localhost:27017/vakil_vision
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
```

Then:

```bash
docker compose up -d
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs. That page is Swagger UI, generated from the FastAPI routes. ReDoc is at `/redoc`, the raw spec at `/openapi.json`.

Mongo must be up first. On startup, `lifespan` calls `init_db()`, which creates indexes. If Mongo is down, uvicorn dies on import because `database.py` connects at module load.

Concept: a process lifespan hook runs setup once, not on every request. Secrets stay in `.env` and are read by `python-dotenv`, never hardcoded.

## 1. Confirm the app is alive

In Swagger, open `GET /`, click Try it out, then Execute.

You should get the app name, version `1.0.0`, and a small endpoint map.

Concept: a root route is a health-style map, not business logic. FastAPI turns the returned dict into JSON. The two routers are mounted with `app.include_router`, so routes live in `contracts.py` and `analysis.py`, not in `main.py`.

## 2. Upload the sample contract

Open `POST /contracts/upload`. Try it out. For `file`, choose `samples/sample_nda.txt`. Execute.

Expect `200` and a body like:

- `message`: uploaded and processed
- `id`: a 24-character hex string — copy this
- `contract.filename`: a uuid plus `.txt`
- `contract.original_name`: `sample_nda.txt`
- `contract.text_content`: the NDA text
- `contract.page_count`: `1` for a txt file
- `contract.word_count`: a positive number
- `contract.status`: `uploaded`

What happened in code:

1. Extension checked against `.pdf` and `.txt`.
2. Bytes read and size checked against 10 MB.
3. File written to `uploads/<uuid>.txt`.
4. `document_parser.extract_text` read the file.
5. A `Contact` model was built and inserted into Mongo collection `contracts`.
6. Mongo’s `ObjectId` was turned into a string before the response.

Concept: `UploadFile` is the multipart file type. Validation belongs in the route (type, size). Parsing belongs in a service. The database stores a document, not a flat SQL row: text, counts, and status sit on one record. The model is named `Contact` because the course snapshot used that name; it is the contract.

## 3. Break the upload on purpose

Still on `POST /contracts/upload`:

- Upload a `.docx` or a `.png`. Expect `400` and `File type not allowed`.
- If you have a file over 10 MB, expect `400` and the size-limit message.

Concept: `HTTPException` is how a route returns a controlled error instead of a stack trace. `400` means the client sent something the API refuses. Swagger shows the status and the `detail` string.

## 4. List contracts

`GET /contracts/`. Execute.

The new row should be there, with `status` still `uploaded`, and no `text_content`.

Concept: the list query uses a Mongo projection, `{"text_content": 0}`, so big fields stay out of list responses. Listing and “get one” are different shapes on purpose.

## 5. Fetch one contract

`GET /contracts/{contract_id}`. Paste the id from step 2. Execute.

You get the full document, including `text_content`.

Then try two bad calls:

- `contract_id` = `not-an-id` → `400` Invalid contract id
- `contract_id` = `507f1f77bcf86cd799439011` (valid ObjectId shape, not in your DB) → `404` Contract not found

Concept: ObjectId parsing fails with `400`. A well-formed id that does not exist is `404`. Those are different failures. The route converts `_id` to `id` because JSON clients should not have to know about BSON.

## 6. Analyse it

`POST /analysis/analyse/{contract_id}`. Same id. Execute.

This is the only call that uses OpenAI. It can take a few seconds.

Expect `200`:

- `id`: a new analysis id — copy this too
- `analysis.contract_id`: the contract id
- `analysis.summary`: two or three sentences
- `analysis.contract_type`: something like NDA
- `analysis.key_clauses`: title, text, plain-language explanation, `is_standard`
- `analysis.risk_flags`: title, description, `risk_level`, recommendation, clause reference
- `analysis.overall_risk_level`: `low`, `medium`, `high`, or `critical`
- `analysis.recommendations`: a list of strings

On this sample, look for the India-wide non-compete, the employee non-solicit, the one-sided indemnity, and the INR 10 lakh cap that only limits the company.

Behind the route:

1. Missing key → `500` before any model call.
2. Contract loaded from Mongo.
3. Status set to `analyzing`.
4. `gemini_analyse.analyze_contract` sends the first 15,000 characters plus a JSON schema, with `response_format={"type": "json_object"}` and `temperature` 0.2.
5. JSON is parsed into `ClauseAnalysis` and `RiskFlag`, then stored in collection `analysis`.
6. Contract status set to `analyzed`.
7. If the model or JSON fails, status becomes `error` and the route returns `502`.

Concept: job state is a field, not a separate queue: `uploaded` → `analyzing` → `analyzed` or `error`. The prompt is a schema. Pydantic is what turns model output into code instead of a paragraph. `502` means the upstream model failed, not that your request was malformed. The file is still named `gemini_analyse.py`; this copy calls OpenAI.

## 7. Read the analysis back three ways

1. `GET /analysis/contract/{contract_id}` with the contract id. You should see one analysis and `total: 1`.
2. `GET /analysis/` to list every analysis.
3. `GET /analysis/{analysis_id}` with the analysis id from step 6.

Then call `GET /contracts/{contract_id}` again. `status` should now be `analyzed`.

Concept: two collections are linked by `contract_id`, not by a SQL foreign key. Route order matters. `GET /analysis/contract/{contract_id}` is registered before `GET /analysis/{analysis_id}`. If it were the other way around, the word `contract` would be captured as an id and the specific route would never run. `GET /` does not mention `GET /analysis/`, but Swagger does, because Swagger is generated from the routers.

## 8. Break analysis on purpose

- Analyse with `not-an-id` → `400`.
- Analyse with a valid but unknown ObjectId → `404`.
- Temporarily clear `OPENAI_API_KEY`, restart uvicorn, analyse again → `500` OpenAI API key is not configured. Put the key back after.

Concept: the same id checks as the contract routes, plus a config failure that is the server’s fault (`500`), not the client’s.

## 9. Optional PDF pass

Upload any small text-based PDF under 10 MB. `page_count` should match the PDF page count, because `PyPDF2` walks `reader.pages`. A scanned PDF with no text layer will upload but store empty or near-empty text, and analyse will then return `400` Contract has no text content.

Concept: “file accepted” is not the same as “text extracted”. The parser is the only place that knows PDF versus TXT.

## What this project is teaching

| Idea | Where you saw it |
|---|---|
| Router split | `contracts` vs `analysis` tags in Swagger |
| Route does HTTP, service does work | upload checks the file; `document_parser` only extracts text; only `gemini_analyse.py` talks to OpenAI |
| Multipart upload | Swagger file picker on `POST /contracts/upload` |
| Document database | nested clauses and risks, not columns |
| ObjectId to string | every response uses `id`, never `_id` |
| Status as workflow | `uploaded`, `analyzing`, `analyzed`, `error` |
| Prompt as a schema | analysis JSON always has the same keys |
| Upstream errors | `502` when the model fails, `500` when the key is missing |
| Route order | `/analysis/contract/...` before `/analysis/{analysis_id}` |

There is no auth, no delete, and no update. Unused prompts in `prompt.py` (`CLAUSE_EXTRACTION_PROMPT`, `RISK_ASSESSMENT_PROMPT`, `SUMMARY_PROMPT`) are not wired to any route.

The equivalent curl, if you want to compare with Swagger:

```bash
curl -F "file=@samples/sample_nda.txt" http://127.0.0.1:8000/contracts/upload
curl -X POST http://127.0.0.1:8000/analysis/analyse/<contract_id>
curl http://127.0.0.1:8000/analysis/contract/<contract_id>
```

The id in those calls is the 24-character value from the upload response, not the filename.


This is a local walkthrough. Run the API on your machine, then hit every route in Swagger in the same order a client would. Each step is paired with the idea that step is teaching.

## 0. Start the stack

From the project folder:

```bash
cd vakil-vision
cp app/.env.example app/.env
```

Put a real key in `app/.env`:

```
MONGODB_URI=mongodb://localhost:27017/vakil_vision
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
```

Then:

```bash
docker compose up -d
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs. That page is Swagger UI, generated from the FastAPI routes. ReDoc is at `/redoc`, the raw spec at `/openapi.json`.

Mongo must be up first. On startup, `lifespan` calls `init_db()`, which creates indexes. If Mongo is down, uvicorn dies on import because `database.py` connects at module load.

Concept: a process lifespan hook runs setup once, not on every request. Secrets stay in `.env` and are read by `python-dotenv`, never hardcoded.

## 1. Confirm the app is alive

In Swagger, open `GET /`, click Try it out, then Execute.

You should get the app name, version `1.0.0`, and a small endpoint map.

Concept: a root route is a health-style map, not business logic. FastAPI turns the returned dict into JSON. The two routers are mounted with `app.include_router`, so routes live in `contracts.py` and `analysis.py`, not in `main.py`.

## 2. Upload the sample contract

Open `POST /contracts/upload`. Try it out. For `file`, choose `samples/sample_nda.txt`. Execute.

Expect `200` and a body like:

- `message`: uploaded and processed
- `id`: a 24-character hex string — copy this
- `contract.filename`: a uuid plus `.txt`
- `contract.original_name`: `sample_nda.txt`
- `contract.text_content`: the NDA text
- `contract.page_count`: `1` for a txt file
- `contract.word_count`: a positive number
- `contract.status`: `uploaded`

What happened in code:

1. Extension checked against `.pdf` and `.txt`.
2. Bytes read and size checked against 10 MB.
3. File written to `uploads/<uuid>.txt`.
4. `document_parser.extract_text` read the file.
5. A `Contact` model was built and inserted into Mongo collection `contracts`.
6. Mongo’s `ObjectId` was turned into a string before the response.

Concept: `UploadFile` is the multipart file type. Validation belongs in the route (type, size). Parsing belongs in a service. The database stores a document, not a flat SQL row: text, counts, and status sit on one record. The model is named `Contact` because the course snapshot used that name; it is the contract.

## 3. Break the upload on purpose

Still on `POST /contracts/upload`:

- Upload a `.docx` or a `.png`. Expect `400` and `File type not allowed`.
- If you have a file over 10 MB, expect `400` and the size-limit message.

Concept: `HTTPException` is how a route returns a controlled error instead of a stack trace. `400` means the client sent something the API refuses. Swagger shows the status and the `detail` string.

## 4. List contracts

`GET /contracts/`. Execute.

The new row should be there, with `status` still `uploaded`, and no `text_content`.

Concept: the list query uses a Mongo projection, `{"text_content": 0}`, so big fields stay out of list responses. Listing and “get one” are different shapes on purpose.

## 5. Fetch one contract

`GET /contracts/{contract_id}`. Paste the id from step 2. Execute.

You get the full document, including `text_content`.

Then try two bad calls:

- `contract_id` = `not-an-id` → `400` Invalid contract id
- `contract_id` = `507f1f77bcf86cd799439011` (valid ObjectId shape, not in your DB) → `404` Contract not found

Concept: ObjectId parsing fails with `400`. A well-formed id that does not exist is `404`. Those are different failures. The route converts `_id` to `id` because JSON clients should not have to know about BSON.

## 6. Analyse it

`POST /analysis/analyse/{contract_id}`. Same id. Execute.

This is the only call that uses OpenAI. It can take a few seconds.

Expect `200`:

- `id`: a new analysis id — copy this too
- `analysis.contract_id`: the contract id
- `analysis.summary`: two or three sentences
- `analysis.contract_type`: something like NDA
- `analysis.key_clauses`: title, text, plain-language explanation, `is_standard`
- `analysis.risk_flags`: title, description, `risk_level`, recommendation, clause reference
- `analysis.overall_risk_level`: `low`, `medium`, `high`, or `critical`
- `analysis.recommendations`: a list of strings

On this sample, look for the India-wide non-compete, the employee non-solicit, the one-sided indemnity, and the INR 10 lakh cap that only limits the company.

Behind the route:

1. Missing key → `500` before any model call.
2. Contract loaded from Mongo.
3. Status set to `analyzing`.
4. `gemini_analyse.analyze_contract` sends the first 15,000 characters plus a JSON schema, with `response_format={"type": "json_object"}` and `temperature` 0.2.
5. JSON is parsed into `ClauseAnalysis` and `RiskFlag`, then stored in collection `analysis`.
6. Contract status set to `analyzed`.
7. If the model or JSON fails, status becomes `error` and the route returns `502`.

Concept: job state is a field, not a separate queue: `uploaded` → `analyzing` → `analyzed` or `error`. The prompt is a schema. Pydantic is what turns model output into code instead of a paragraph. `502` means the upstream model failed, not that your request was malformed. The file is still named `gemini_analyse.py`; this copy calls OpenAI.

## 7. Read the analysis back three ways

1. `GET /analysis/contract/{contract_id}` with the contract id. You should see one analysis and `total: 1`.
2. `GET /analysis/` to list every analysis.
3. `GET /analysis/{analysis_id}` with the analysis id from step 6.

Then call `GET /contracts/{contract_id}` again. `status` should now be `analyzed`.

Concept: two collections are linked by `contract_id`, not by a SQL foreign key. Route order matters. `GET /analysis/contract/{contract_id}` is registered before `GET /analysis/{analysis_id}`. If it were the other way around, the word `contract` would be captured as an id and the specific route would never run. `GET /` does not mention `GET /analysis/`, but Swagger does, because Swagger is generated from the routers.

## 8. Break analysis on purpose

- Analyse with `not-an-id` → `400`.
- Analyse with a valid but unknown ObjectId → `404`.
- Temporarily clear `OPENAI_API_KEY`, restart uvicorn, analyse again → `500` OpenAI API key is not configured. Put the key back after.

Concept: the same id checks as the contract routes, plus a config failure that is the server’s fault (`500`), not the client’s.

## 9. Optional PDF pass

Upload any small text-based PDF under 10 MB. `page_count` should match the PDF page count, because `PyPDF2` walks `reader.pages`. A scanned PDF with no text layer will upload but store empty or near-empty text, and analyse will then return `400` Contract has no text content.

Concept: “file accepted” is not the same as “text extracted”. The parser is the only place that knows PDF versus TXT.

## What this project is teaching

| Idea | Where you saw it |
|---|---|
| Router split | `contracts` vs `analysis` tags in Swagger |
| Route does HTTP, service does work | upload checks the file; `document_parser` only extracts text; only `gemini_analyse.py` talks to OpenAI |
| Multipart upload | Swagger file picker on `POST /contracts/upload` |
| Document database | nested clauses and risks, not columns |
| ObjectId to string | every response uses `id`, never `_id` |
| Status as workflow | `uploaded`, `analyzing`, `analyzed`, `error` |
| Prompt as a schema | analysis JSON always has the same keys |
| Upstream errors | `502` when the model fails, `500` when the key is missing |
| Route order | `/analysis/contract/...` before `/analysis/{analysis_id}` |

There is no auth, no delete, and no update. Unused prompts in `prompt.py` (`CLAUSE_EXTRACTION_PROMPT`, `RISK_ASSESSMENT_PROMPT`, `SUMMARY_PROMPT`) are not wired to any route.

The equivalent curl, if you want to compare with Swagger:

```bash
curl -F "file=@samples/sample_nda.txt" http://127.0.0.1:8000/contracts/upload
curl -X POST http://127.0.0.1:8000/analysis/analyse/<contract_id>
curl http://127.0.0.1:8000/analysis/contract/<contract_id>
```


Stop the API first, then stop Mongo. Do not pass `-v` to Compose, and do not prune volumes, or the saved contracts and analyses go with the Mongo volume.

## Stop the app

In the terminal where `uvicorn` is running, press Ctrl+C once. Wait until you see the process exit. That only stops the Python server. It does not touch your code, `uploads/`, or Mongo.

If it does not exit, press Ctrl+C again. Only if it is still stuck:

```bash
# from another terminal, only if Ctrl+C failed
pkill -f "uvicorn app.main:app"
```

## Stop Docker, keep the data

From the `vakil-vision` folder:

```bash
docker compose down
```

That stops and removes the `vakil_mongo` container and its Compose network. It keeps the named volume `vakil_mongo_data`, so contracts and analyses are still there the next time you run `docker compose up -d`.

Do not run `docker compose down -v`. The `-v` flag deletes that volume.

Your project files are never removed by Compose. Those stay on disk:

- source code in `vakil-vision/`
- `app/.env`
- parsed uploads in `uploads/`

## Start it again later

```bash
cd vakil-vision
docker compose up -d
uvicorn app.main:app --reload
```

Same database, same uploaded files.

## Clear Docker cache without deleting this data

Unused images and build cache are the usual space hogs. Volumes are the project data, so leave them alone.

Check what is using space:

```bash
docker system df
```

Safe cleanup:

```bash
docker container prune
docker image prune
docker builder prune
```

- `container prune` removes stopped containers only.
- `image prune` removes dangling images, not images a container is using.
- `builder prune` removes BuildKit cache. This project barely builds anything, because Compose just pulls `mongo:7`, so this may free little.

A broader but still volume-safe sweep:

```bash
docker system prune
```

That removes stopped containers, unused networks, dangling images, and build cache. It does not remove volumes unless you add `--volumes`.

Skip these if you want the Vakil Vision database kept:

```bash
docker compose down -v
docker volume prune
docker system prune --volumes
docker system prune -a --volumes
```

`docker volume prune` is the easy mistake. After `docker compose down`, no container is using `vakil_mongo_data`, so a volume prune treats it as unused and deletes it.

To see that volume before any cleanup:

```bash
docker volume ls
```

You want `vakil_mongo_data` still listed when you are done.

The id in those calls is the 24-character value from the upload response, not the filename.




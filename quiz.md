## RAG

Question 1:

According to the chapter, what core problem does a RAG pipeline solve when building a system to "talk"
to a large 400-page PDF?

It compresses the PDF into a smaller file so it downloads faster

It avoids feeding the entire document into the LLM, preventing context-window limits
and hallucinations while saving tokens

C

It translates the PDF into multiple languages before querying

It permanently fine-tunes the LLM on the PDF's contents



Question 2:

In the correct order, what are the four steps of the indexing phase described in the chapter?

Take a data source, chunk/split it, generate embeddings, then store the
embeddings plus the actual chunk in a vector store

+ Explain this further

Correct

Perform a similarity search, retrieve top chunks, call the LLM, return a response

Upload the PDF, fine-tune the model, deploy to production, monitor queries

Convert the query to embeddings, search the vector DB, merge chunks, and generate an
answer


Question 3:

During the query phase, how does the system find the parts of the document relevant to a user's question?

It scans every page of the PDF linearly for matching keywords

It sends all 1000 chunks to the LLM and lets the model pick the relevant ones

It asks the user to manually select which chunks to use

It converts the user's query into vector embeddings using the same embedding
model, then performs a similarity search to return only the most relevant chunks

+ Explain this further

Correct


Question 4:

In the setup lecture, how is QuadrantDB (Qdrant) run locally, and on which port is its dashboard accessed?

Installed via pip and accessed on port 8000

Run with a 'docker-compose.yaml` file (using ` docker compose up') and
accessed on port 6333

+ Explain this further

Correct

Deployed to the cloud only, with no local option

Started with `npm start` and accessed on port 5432




Question 5:

When building the indexing script with LangChain, which components were used to load, split, and embed the
PDF?

PyPDFLoader to load the PDF, a text splitter with chunk size and overlap to create
chunks, and OpenAIEmbeddings to embed them into the Quadrant vector store

+ Explain this further

Correct

A raw file reader, a JSON parser, and a local sentence-transformer model

BeautifulSoup for loading, regex for splitting, and Pinecone for embeddings

O

The FastAPI file upload, a manual paragraph counter, and Milvus for storage






Question 1:

In the Yatra Planner project, what does it mean to "aggregate" data, and why is in-memory caching used for
the API?

O

To encrypt data from a single source; caching is used to secure the API key

To collect and combine data from multiple external sources into one place; caching
reduces latency and helps avoid hitting external providers' rate limits

+ Explain this further

Correct

To split one large response into many small databases; caching is used only to compress the
response

To translate data between languages; caching is used to store user login sessions





Question 2:

What special content-type header signals a Server-Sent Events (SSE) streaming response, and in which
direction does the data flow?

C

application/json`; data flows both ways between client and server

O

`text/html`; data flows only from client to server

O

text/event-stream'; the connection stays open and data flows only from server to
client

+ Explain this further

Correct

O

multipart/form-data'; the connection closes after each chunk and only the client sends data


Question 3:

In the FastAPI code, how were the planner routes organized and connected to the main application?

All routes were written directly inside `main.py` with no separate files

Routes were placed in a separate planner.py` file using ` APIRouter` (with a prefix
and tags), then registered in `main.py` via `app.include_router( ... )'

+ Explain this further

Correct

Routes were defined as Pydantic models and imported automatically by FastAPI

Routes were added to requirements.txt' and loaded at server startup


Question 4:

What validation rules were applied to the 'TravelRequestModel' in the create-plan controller?

The destination must be a number and the currency must always be USD

The start date must be greater than the end date and trips must last at least 30 days

The trip duration (end date minus start date) must be at least one day and no more
than 14 days, otherwise an 'HTTPException` with status 400 is raised

+ Explain this further

Correct

There were no validations; any date range was accepted



Question 5:

After the weather, places, and currency fetches were first written as three sequential blocking calls, how were
they made faster?

By caching the entire main.py file so the calls never run again

By using asyncio.gather( ... )' to run the three fetch calls in parallel, so total wait
time is roughly the slowest single call rather than the sum of all three

+ Explain this further

Correct

By switching from 'httpx' to synchronous 'requests' to speed up each call

C

By deleting the places and currency calls entirely to reduce work

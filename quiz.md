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



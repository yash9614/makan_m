from fastapi import APIRouter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

router = APIRouter(
    prefix="/query",
    tags=["query"],
)

openai_client = OpenAI(api_key="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")

# Embedding the chunks using OpenAI Embeddings
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key="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"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    collection_name="sample_collection",
    url="http://localhost:6333"
)

@router.post("/")
async def query(question: str):
    search_results = vector_db.similarity_search(query=question)

    context = " ".join(
        [
            f"[Page {result.metadata.get('page', 'unknown')}] {result.page_content}"
            for result in search_results
        ]
    )

    SYSTEM_PROMPT = f"""
You are a helpful assistant that answers questions based on the provided context.
If the context does not contain the answer, respond with "I don't know."

Also include the page number of the context in your answer if applicable.

Context:
{context}
    """

    response = openai_client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ]
    )

    return {"question": question, "answer": response.choices[0].message.content  }
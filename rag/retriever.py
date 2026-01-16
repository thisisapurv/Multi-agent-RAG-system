from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DB_PATH = "chroma_db"

# SAME embeddings as ingest.py
embeddings = HuggingFaceEmbeddings()

db = Chroma(
    persist_directory=DB_PATH,
    embedding_function=embeddings
)

def retrieve_docs(query: str):
    docs = db.similarity_search(query, k=3)

    context = ""
    for d in docs:
        context += d.page_content + "\n\n"

    return context

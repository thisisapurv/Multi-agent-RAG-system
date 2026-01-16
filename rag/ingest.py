import os
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

FILE_PATH = "C:\\Projects\\AAProjects\\data\\indian.docx.docx"

print("DEBUG PATH:", FILE_PATH)
print("Exists:", os.path.exists(FILE_PATH))

DB_PATH = "chroma_db"

loader = Docx2txtLoader(FILE_PATH)
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings()

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=DB_PATH
)

db.persist()
print("✅ ChromaDB created")

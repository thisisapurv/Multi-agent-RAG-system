# 🔗 LangGraph Powered RAG System

A clean and minimal **Retrieval-Augmented Generation (RAG)** system
powered by **LangGraph**, **Groq LLM**, and **ChromaDB**.

This project demonstrates how to integrate LangGraph into an existing
RAG pipeline **without breaking the original architecture**.

------------------------------------------------------------------------

## 🚀 Features

-   LangGraph orchestration
-   ChromaDB vector store
-   HuggingFace embeddings
-   Groq LLM integration
-   Clean CLI chat interface
-   Minimal architecture changes
-   Production-friendly structure

------------------------------------------------------------------------

## 📂 Project Structure

    AAProjects/
    │
    ├── rag/
    │   ├── retriever.py
    │   ├── ingest.py
    │   └── __init__.py
    │
    ├── data/
    │   └── indian.docx.docx
    │
    ├── graph.py
    ├── groq_client.py
    ├── main.py
    ├── router.py
    ├── README.md
    └── .env

------------------------------------------------------------------------

## ⚙️ Setup

### 1️⃣ Install dependencies

``` bash
pip install langgraph langchain langchain-community langchain-chroma langchain-huggingface chromadb sentence-transformers groq python-dotenv
```

------------------------------------------------------------------------

### 2️⃣ Environment variables

Create `.env`

    GROQ_API_KEY=your_api_key_here

------------------------------------------------------------------------

### 3️⃣ Ingest documents

``` bash
python rag/ingest.py
```

------------------------------------------------------------------------

### 4️⃣ Run application

``` bash
python main.py
```

------------------------------------------------------------------------

## 💬 Usage

On start:

    🤖 Hi! How can I help you today?

Exit commands:

    exit
    bye
    quit

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 3.11
-   LangGraph
-   LangChain
-   ChromaDB
-   HuggingFace Transformers
-   Groq API

------------------------------------------------------------------------

## 🎯 Use Case

-   Document-based QA
-   Knowledge assistants
-   AI chat systems
-   RAG pipelines

------------------------------------------------------------------------

## 👨‍💻 Author

**Apurv Bhavsar**

------------------------------------------------------------------------

## ⭐ Future Scope

-   Multi-agent routing
-   Memory support
-   Tool calling
-   Web interface
-   Docker deployment

------------------------------------------------------------------------

## 📜 License

MIT License

from rag.retriever import retrieve_docs
from groq_client import call_llm
from memory import add_message, get_history

def run_indian_agent(query):

    add_message("user", query)

    history = get_history()
    chat_context = ""

    for msg in history:
        chat_context += f"{msg['role']}: {msg['content']}\n"

    rag_context = retrieve_docs(query)

    prompt = f"""
You are an Indian finance expert.

Conversation so far:
{chat_context}

Use ONLY the below context:
{rag_context}

Question:
{query}

Answer:
"""

    response = call_llm(prompt)

    add_message("assistant", response)
    return response

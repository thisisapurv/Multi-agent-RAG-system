from groq_client import call_llm
from memory import add_message, get_history

def run_chat_agent(query):

    add_message("user", query)

    history = get_history()
    prompt = ""

    for msg in history:
        prompt += f"{msg['role']}: {msg['content']}\n"

    response = call_llm(prompt)

    add_message("assistant", response)
    return response

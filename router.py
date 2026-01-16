from groq_client import call_llm

def route_query(query):

    intent_prompt = """
Decide which agent should handle this query.
Reply with only one word:
indian, chat, global
"""

    intent = call_llm(
        f"{intent_prompt}\n\nUser Query: {query}"
    ).strip().lower()

    return intent

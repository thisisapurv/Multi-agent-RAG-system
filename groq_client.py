from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(user_prompt):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return completion.choices[0].message.content


if __name__ == "__main__":

    print("Agent: Hello! Type 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Agent: Goodbye! Have a good day!")
            break

        response = call_llm(user_input)
        print("Agent:", response)

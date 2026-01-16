from graph import app

def main():
    print("\nHi! How can I help you today?\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("Agent: Goodbye! Have a good day!")
            break

        res = app.invoke({"query": query})
        print("Agent:", res["response"])


if __name__ == "__main__":
    main()

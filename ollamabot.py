import ollama

MODEL = "phi3:mini"

def main():
    conversation = [
        {"role": "system", "content": "You are helpful assistant"}
    ]

    while True:
        user = input("You: ")
        if user.lower() in ["exit", "quit", "bye"]:
            print("Bot: see you soon")
            break

        conversation.append({"role": "user", "content": user})

        stream = ollama.chat(model=MODEL, messages=conversation, stream=True)

        bot_text = ""
        print("Bot: ", end="", flush=True)
        for chunk in stream:
            piece = chunk["message"]["content"]
            bot_text += piece
            print(piece, end="", flush=True)
        print()

        conversation.append({"role": "assistant", "content": bot_text})

if __name__ == "__main__":
    main()

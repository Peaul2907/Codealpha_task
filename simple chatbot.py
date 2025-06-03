def chatbot():
    name = input("Chatbot: Hey! What's your name?\nYou: ")
    print(f"Chatbot: Nice to meet you, {name}!")
    print(f"You can say 'hello', 'how are you', or 'bye' to chat.")

    while True:
        user_input = input(f"{name}: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print(f"Chatbot: Hi {name}!")
        elif user_input in "how are you":
            print(f"Chatbot: I'm fine, thanks for asking, {name}!")
        elif user_input in "bye":
            print(f"Chatbot: Goodbye, {name}!")
            break
        else:
            print(f"Chatbot: Sorry {name}, I didn't understand that.")

# Run the chatbot
chatbot()
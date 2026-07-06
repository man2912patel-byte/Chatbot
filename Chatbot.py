print("🤖 Welcome to AI ChatBot")
print("Type 'exit' to quit.\n")

responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! 😊",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "My name is DecodeBot.",
    "who created you": "I was created using Python.",
    "good morning": "Good Morning! ☀️",
    "good afternoon": "Good Afternoon! 🌞",
    "good evening": "Good Evening! 🌙",
    "thanks": "You're welcome! 😊",
    "thank you": "My pleasure!",
    "bye": "Goodbye! Have a nice day! 👋"
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! 👋")
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that. 😔"
    )

    print("Bot:", reply)
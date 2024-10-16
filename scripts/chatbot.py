from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ]
)

# Training the chat bot
trainer = ListTrainer(chatbot)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer.train(conversation)

# Getting a response
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Charlie: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print("Charlie:", response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


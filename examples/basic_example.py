from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot("How are you?")

# Get a response to the input "How are you?"
response = chatbot.get_response("find,are you?")

print(response)

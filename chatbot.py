# chatbot.py
def get_response(user_input):
    responses = {
        "hello": "Hi! How can I assist you?",
        "hi": "Hello! How can I help you today?",
        "hey": "Hey there! Need any help?",
        "how are you": "I'm just code, but thanks for asking!",
        "what is your name": "I'm a virtual assistant created by Sayan!",
        "who created you": "I was built by Sayan Ghosh using Python and Flask.",
        "help": "Sure, I'm here to help. Ask me anything!",
        "what can you do": "I can chat, answer simple questions, and help guide you!",
        "thank you": "You're welcome!",
        "thanks": "Glad I could help!",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Take care! See you soon!",
        "what is python": "Python is a powerful, easy-to-learn programming language.",
        "what is flask": "Flask is a lightweight Python web framework.",
        "tell me a joke": "Why don’t programmers like nature? It has too many bugs.",
        "who is the president of india": "As of 2025, the President of India is Droupadi Murmu.",
        "what's the time": "I'm not connected to the real world clock, sorry!",
        "open google": "Sorry, I can't open websites directly.",
        "can you code": "Yes! I can help with Python, JavaScript, and more."
    }
    return responses.get(user_input.lower(), "I'm sorry, I didn't understand that.")

def get_response(user_input, user_name):
    user_input = user_input.lower().strip()

    # ---------------- GREETINGS ----------------

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How are you today? 😊", user_name

    elif user_input in ["good morning", "good afternoon", "good evening"]:
        return "Nice to meet you! How is your day going?", user_name

    # ---------------- FEELINGS ----------------

    elif user_input in ["i am good", "i am fine", "good", "fine", "great"]:
        return "That's great to hear! 😊 What can I help you with?", user_name

    elif user_input in ["i am bad", "i am sad", "not good", "sad"]:
        return "I'm sorry to hear that. Is there anything I can help you with?", user_name

    elif "how are you" in user_input:
        return "I am doing great! Thanks for asking. How are you?", user_name

    # ---------------- NAME ----------------

    elif user_input in ["what is your name", "who are you"]:
        return "I am a rule-based AI chatbot. What's your name?", user_name

    elif user_input.startswith("my name is"):
        name = user_input.replace("my name is", "", 1).strip()

        if name:
            return f"Nice to meet you, {name}! 😊 What can I help you with?", name
        else:
            return "Please tell me your name.", user_name

    elif user_input in [
        "what is my name",
        "what's my name",
        "whats my name",
        "do you know my name",
        "tell me my name",
        "remember my name"
    ]:
        if user_name:
            return f"Your name is {user_name}! 😊", user_name
        else:
            return "I don't know your name yet. Please tell me 'my name is Yashmitha'.", user_name

    # ---------------- PYTHON ----------------

    elif "python" in user_input and "used" in user_input:
        return "Python is used in Artificial Intelligence, Machine Learning, Data Science, Web Development, Automation, and many other fields.", user_name

    elif "python" in user_input:
        return "Python is a popular programming language known for its simple syntax. It is widely used in AI, Machine Learning, Data Science, Web Development, and Automation.", user_name

    # ---------------- ARTIFICIAL INTELLIGENCE ----------------

    elif "application" in user_input and (
        "ai" in user_input or "artificial intelligence" in user_input
    ):
        return "Applications of AI include virtual assistants, recommendation systems, self-driving cars, healthcare, fraud detection, chatbots, robotics, and image recognition.", user_name

    elif "artificial intelligence" in user_input or user_input in [
        "ai",
        "what is ai",
        "explain ai"
    ]:
        return "Artificial Intelligence (AI) is a field of computer science that focuses on creating systems that can perform tasks that normally require human intelligence.", user_name

    # ---------------- MACHINE LEARNING ----------------

    elif "types of machine learning" in user_input:
        return "The three main types of Machine Learning are Supervised Learning, Unsupervised Learning, and Reinforcement Learning.", user_name

    elif "supervised learning" in user_input:
        return "Supervised Learning uses labeled data to train a model to make predictions. Examples include classification and regression.", user_name

    elif "unsupervised learning" in user_input:
        return "Unsupervised Learning works with unlabeled data and finds hidden patterns or groups. Clustering is a common example.", user_name

    elif "reinforcement learning" in user_input:
        return "Reinforcement Learning is a type of Machine Learning where an agent learns by interacting with an environment and receiving rewards or penalties.", user_name

    elif "machine learning" in user_input or user_input in [
        "ml",
        "what is ml",
        "explain ml"
    ]:
        return "Machine Learning is a branch of AI where computers learn patterns from data and use those patterns to make predictions or decisions.", user_name

    # ---------------- DEEP LEARNING ----------------

    elif "deep learning" in user_input:
        return "Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from large amounts of data.", user_name

    # ---------------- NLP ----------------

    elif "natural language processing" in user_input or user_input in [
        "nlp",
        "what is nlp",
        "explain nlp"
    ]:
        return "Natural Language Processing (NLP) is a branch of AI that enables computers to understand, process, and generate human language.", user_name

    # ---------------- CHATBOT ----------------

    elif "rule based chatbot" in user_input:
        return "A rule-based chatbot uses predefined rules, keywords, and responses to communicate with users. It does not learn automatically from conversations.", user_name

    elif "how do you work" in user_input or "how does this chatbot work" in user_input:
        return "I use predefined rules and keywords to understand your message and select an appropriate response.", user_name

    elif "chatbot" in user_input:
        return "A chatbot is a computer program designed to communicate with users through text or voice.", user_name

    # ---------------- NEURAL NETWORK ----------------

    elif "neural network" in user_input:
        return "A neural network is a computing model inspired by the human brain. It consists of interconnected nodes called neurons and is widely used in AI and Deep Learning.", user_name

    # ---------------- COMPUTER VISION ----------------

    elif "computer vision" in user_input:
        return "Computer Vision is a field of AI that enables computers to understand and analyze images and videos.", user_name

    # ---------------- DATA SCIENCE ----------------

    elif "data science" in user_input:
        return "Data Science combines programming, statistics, mathematics, and machine learning to extract useful information and insights from data.", user_name

    # ---------------- AI APPLICATIONS ----------------

    elif "applications of ai" in user_input:
        return "AI is used in healthcare, education, banking, transportation, robotics, recommendation systems, virtual assistants, and cybersecurity.", user_name

    # ---------------- CAPABILITIES ----------------

    elif "what can you do" in user_input or user_input == "help":
        return "I can answer questions about Python, AI, Machine Learning, Deep Learning, NLP, Computer Vision, Data Science, Neural Networks, and Chatbots.", user_name

    # ---------------- THANKS ----------------

    elif user_input in ["thank you", "thanks", "thankyou"]:
        return "You're welcome! 😊 Is there anything else I can help you with?", user_name

    # ---------------- GOODBYE ----------------

    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋", user_name

    # ---------------- UNKNOWN INPUT ----------------

    else:
        return "I'm not sure about that. Can you ask me something about Python, AI, Machine Learning, Deep Learning, NLP, Computer Vision, or Chatbots?", user_name


def chatbot():

    print("=" * 60)
    print("🤖 Welcome to the AI Rule-Based Chatbot!")
    print("=" * 60)

    print("🤖 Chatbot: Hello! I am your AI chatbot.")
    print("🤖 Chatbot: I can answer questions about:")
    print("   • Python")
    print("   • Artificial Intelligence")
    print("   • Machine Learning")
    print("   • Deep Learning")
    print("   • NLP")
    print("   • Computer Vision")
    print("   • Data Science")
    print("   • Neural Networks")
    print("   • Chatbots")
    print("🤖 Chatbot: I can also remember your name during this conversation.")
    print("🤖 Chatbot: Type 'bye' anytime to exit.")
    print("=" * 60)

    # Store user's name
    user_name = None

    while True:

        user_input = input("You: ").strip()

        # Exit the chatbot
        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a great day! 👋")
            break

        # Get chatbot response
        response, user_name = get_response(user_input, user_name)

        print("🤖 Chatbot:", response)


# ---------------- START CHATBOT ----------------

chatbot()
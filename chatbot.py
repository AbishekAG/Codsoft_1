def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm fine, How can I assist you?"

    elif "can you narrate articles" in user_input:
        return "Yes, Would you like to know more about it?"

    elif "topics" in user_input:
        return "The topics include AI, Cybersecurity, Data Science, and many more exciting areas."

    elif "it is awesome" in user_input:
        return "Thank you for your appreciations."

    elif "Would you know about symposium" in user_input:
        return "Yes,I know about it for more info go to official website"

    elif "can you show live news" in user_input:
        return "I can't check live news."
    
    elif "create a joke" in user_input:
        return "Why did the math book look sad? Because it had too many problems!"
    
    elif "help" in user_input:
        return "I'm here to help! How can I help you?."

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Hope to see you at the symposium!"

    else:
        return "I'm not sure I understand. Could you please replace or ask about a specific topic?"

    
while True:
  user_input = input("You: ")
  response = chatbot_response(user_input)
  print("Chatbot:", response)
  if "bye" in user_input or "goodbye" in user_input:
        break

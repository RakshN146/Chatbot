import random
import json
import nltk
from nltk.tokenize import word_tokenize
import string

# Download necessary NLTK resources
nltk.download('punkt')

# Sample product knowledge base (this can be expanded as needed)
product_info = {
    "Product A": "Product A is a high-quality widget designed to solve your daily needs.",
    "Product B": "Product B is a premium gadget with advanced features for tech enthusiasts.",
    "Product C": "Product C is an affordable option for anyone looking for reliable performance."
}

# Sample FAQ dataset
faq_data = {
    "What are your business hours?": "Our business hours are 9 AM to 6 PM from Monday to Friday.",
    "How can I contact customer support?": "You can reach our customer support at support@company.com or call 1800-123-456.",
    "Where are you located?": "We are located at 123 Business Road, Tech City, ABC.",
}

# Intents: what users might ask
intents = {
    "greeting": ["hello", "hi", "hey", "howdy", "good morning", "good evening"],
    "product_info": ["tell me about", "information about", "what is", "product details", "describe"],
    "order_tracking": ["track my order", "order status", "order details", "where is my order"],
    "feedback": ["feedback", "suggestions", "comments", "rate", "review"],
    "complaint": ["complaint", "issue", "problem", "disappointed", "unsatisfied"],
    "thank_you": ["thanks", "thank you", "appreciate it"]
}

# Predefined responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi! How can I help you?", "Greetings! How can I assist you today?"],
    "order_tracking": ["Can you please provide your order number?", "Please provide the order number to track your order."],
    "feedback": ["Thank you for your feedback! We will review it and take action.", "We appreciate your feedback! How can we improve?"],
    "complaint": ["Sorry to hear about your issue! Can you please provide more details?", "We're sorry for the inconvenience. Can you explain your issue in more detail?"],
    "thank_you": ["You're welcome!", "Glad I could help!", "Happy to assist you!"]
}

# Order number validation
valid_order_numbers = ["12345", "67890", "11223", "44556", "78901"]

# Function to match intent with the user's message
def match_intent(user_message):
    user_message = user_message.lower()  # Convert to lowercase for case-insensitivity
    
    # Check which intent matches based on exact matching for phrases
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_message:
                return intent
    return "generic"

# Function to provide responses based on user intent
def get_response(intent, user_message=None):
    if intent in responses:
        return random.choice(responses[intent])
    
    if intent == "product_info":
        product_query = user_message.split()[-1]
        if product_query in product_info:
            return product_info[product_query]
        else:
            return "Sorry, I don't have information about that product."
    
    if intent == "order_tracking":
        # Check if the order number is mentioned in the input
        order_number = [word for word in user_message.split() if word.isdigit()]
        if order_number and order_number[0] in valid_order_numbers:
            return f"Your order {order_number[0]} is being processed and will arrive soon."
        else:
            return "I couldn't find any order with that number. Please check again."
    
    if intent == "feedback":
        return random.choice(responses["feedback"])
    
    if intent == "complaint":
        return random.choice(responses["complaint"])
    
    return "I'm sorry, I didn't understand that. Could you please clarify?"

# Main function to simulate the chatbot interaction
def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    
    conversation_log = []  # To store the conversation
    while True:
        user_input = input("User: ").lower()
        
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Process the user's input and match intent
        intent = match_intent(user_input)
        
        # Get the chatbot's response
        response = get_response(intent, user_input)
        
        # Print the chatbot's response and save to conversation log
        print(f"Chatbot: {response}")
        conversation_log.append({"User": user_input, "Chatbot": response})
        
        # Saving the conversation to a log file
        with open("conversation_log.json", "w") as log_file:
            json.dump(conversation_log, log_file, indent=4)

# Run the chatbot
chatbot()

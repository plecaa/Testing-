 #Import the necessary libraries
import json
import random

# Define a class for the chatbot
class ChatBot:
    # Initialize the chatbot with a filename for the data file
    def __init__(self, filename):
        self.filename = filename
        # Load the data from the file
        self.data = self.load_data()

    # Load the data from the file
    def load_data(self):
        try:
            # Try to open the file aand load the data
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, create a new data structure
            return {"intents": {}}

    # Save the data to the file
    def save_data(self):
        # Open the file and dump the data
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    # Get a response for a given user input
    def get_response(self, user_input):
        # Convert the user input to lowercase
        user_input = user_input.lower()
        # Check if the user input is in the data
        if user_input in self.data["intents"]:
            # If it is, return a random response
            return random.choice(self.data["intents"][user_input])
        else:
            # If not, return a default response
            return "I didn't understand that."

    # Learn a new response for a given user input
    def learn(self, user_input, response):
        # Convert the user input to lowercase
        user_input = user_input.lower()
        # Check if the user input is already in the data
        if user_input not in self.data["intents"]:
            # If not, create a new list for the user input
            self.data["intents"][user_input] = [response]
        else:
            # If it is, append the response to the list
            self.data["intents"][user_input].append(response)
        # Save the data
        self.save_data()

# Define the main function
def main():
    # Create a new chatbot
    chatbot = ChatBot('data.json')
    # Loop indefinitely
    while True:
        # Get the user input
        user_input = input("User: ")
        # Check if the user wants to quit
        if user_input.lower() == "quit":
            break
        # Get the response from tuhe chatbot
        response = chatbot.get_response(user_input)
        # Print the response
        print("Chatbot:", response)
        # Ask the user if the response is correct0................................................................................................................................................................................................................................
        new_response = input("Is this response correct? (yes/no): ")
        # If the response is not correct, learn a new response
        if new_response.lower() == "no":
            new_response = input("What should the response be? ")
            chatbot.learn(user_input, new_response)

# Run the main function
if __name__ == "__main__":
    main()



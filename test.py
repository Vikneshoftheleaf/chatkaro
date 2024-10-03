import os
from dotenv import load_dotenv
from groq import Groq
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API")
)

messages = [
    {
        "role": "user",
        "content": "roleplay like a 21 year old muslim asian girl named Fathima, studying computer science, the response should be short and more human"
    }
]
"""
def chatAppend(new_data, file_path="chatdata.json"):
    with open(file_path, 'r') as file:
        data = json.load(file)  # Load the JSON data as a Python object

# Step 2: Append new data (Assume 'data' is a list)
    if isinstance(data, list):
        data.append(new_data)
    else:
        print("Error: JSON data is not a list. Cannot append.")

    # Step 3: Write the updated JSON data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4) 

    # Initialize messages with the system's roleplay request
   
with open("chatdata.json", "r") as file:
        messages = json.load(file)
"""



# Bot initiates the conversation with a greeting
chat_completion = client.chat.completions.create(
    messages=messages,
    model="llama-3.1-70b-versatile",
)

# Extract and print the bot's initial response
initial_response = chat_completion.choices[0].message.content
print(f"Fathima: {initial_response}")

# Append the bot's initial response to the messages list
messages.append({"role": "assistant", "content": initial_response})
#chatAppend({"role": "assistant", "content": initial_response})

# Begin the loop for continuous conversation
while True:

    # Get user input for continuous chat
    user_input = input("You: ")

    # Add the user input to the messages list
    messages.append({"role": "user", "content": user_input})
    #chatAppend({"role": "user", "content": user_input})

    # Call the chat completion model with updated messages
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-70b-8192",
    )

    # Extract and print the model's response
    response = chat_completion.choices[0].message.content
    print(f"Fathima: {response}")

    # Append the model's response to the messages list
    messages.append({"role": "assistant", "content": response})
    #chatAppend({"role": "assistant", "content": response})

    # Optional: Exit the loop if the user types "exit"
    if user_input.lower() == "exit":
        break

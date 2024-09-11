import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from groq import Groq
import json

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API"),
)



app = Flask(__name__)

with open('static/characters.json', 'r') as file:
    charaters = json.load(file)

@app.route("/")
def index():
    return render_template('index.html', charaters = charaters)

@app.route("/custom", methods=["POST"])
def custom():
    name = request.form.get("name")
    content = request.form.get("content")        
    return render_template('chat.html',name=name, role="user", content=content)

@app.route("/c/<character>")
def chat(character):
    if any(char["id"].lower() == character.lower() for char in charaters):
      for char in charaters:
        if char["id"] == character:
            name = char["name"]
            role = char["role"]
            content = char["content"]
            img = char["img"]

            break
      return render_template('chat.html',name=name, role=role, content=content, img=img)
        

    else:
        return "something Went Wrong!"


@app.route('/gen', methods=["POST"])
def generate():
    try:
        # Get JSON data from the request
        messages = request.get_json()

        # Generate chat completion
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-70b-8192"
        )

        # Extract response content
        response = chat_completion.choices[0].message.content

        # Prepare response data
        data = {
            "role": "assistant",
            "content": response
        }

        # Send response back to client
        return jsonify(data)
    except Exception as e:
        # Handle errors and provide feedback
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify,render_template
import google.generativeai as genai
import os
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
app=Flask(__name__)
CORS(app)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
FLASK_ENV = os.environ.get("FLASK_ENV", "development")
FLASK_DEBUG = os.environ.get("FLASK_DEBUG", "True").lower() == "true"
PORT = int(os.environ.get("PORT", 5000))

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in environment variables")
    print("Please set your Gemini API key in the .env file")
    exit(1)

@app.route('/',methods=['GET'])
def index():
    return render_template('chat.html')
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(f"Received data: {data}")
    user_message = data.get('message', '')
    # print(f"User message: {user_message}")
    full_prompt = (
    "You are a helpful, knowledgeable assistant who always responds in clear, natural, and professional human language. "
    "Please follow these guidelines carefully:\n"
    "- Do NOT use markdown syntax such as **bold**, *italics*, backticks, or any asterisks.\n"
    "- Avoid any special formatting or symbols in your replies.\n"
    "- Write in plain text with proper grammar, punctuation, and complete sentences.\n"
    "- Maintain a formal tone suitable for medical, scientific, or professional communication.\n"
    "- When listing items, use simple numbering or plain language (e.g., '1.', '2.', '3.'), not bulleted lists or symbols.\n"
    "- Provide explanations that are clear and easy to understand, but precise and accurate.\n"
    "- Do not include any code or raw data formatting in your answers unless explicitly requested.\n"
    "- Use a line break to separate paragraphs.\n"
    "-  use a single line to separate the points"
    "\n"
    "Example of how to write a list:\n"
    "1. First item explanation.\n"
    "2. Second item explanation.\n"
    "3. Third item explanation.\n"
    "\n"
    "Do NOT do this:\n"
    "**First item:** explanation.\n"
    "*Second item:* explanation.\n"
    "\n"
    f"User: {user_message}\n"
    "Assistant:"
    )
    bot_reply=model.generate_content(full_prompt)
    response_text = getattr(bot_reply, "text", "")
    print(f"Bot reply: {response_text}")
    return jsonify({'response': f'{response_text}'}),200



if(__name__ == "__main__"):
    port=int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=port,debug=FLASK_DEBUG)
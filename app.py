from flask import Flask, request, jsonify,render_template
import  lmstudio as  lms
import os
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
model=lms.llm("mistralai/mistral-7b-instruct-v0.3")
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
    bot_reply=model.respond(full_prompt)
    return jsonify({'response': f'{bot_reply}'}),200



if(__name__ == "__main__"):
    port=int(os.environ.get('PORT',5000))
    app.run(host="0.0.0.0",port=port,debug=True)
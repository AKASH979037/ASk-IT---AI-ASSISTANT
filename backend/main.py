from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    return jsonify({"response": f"Echo: {message}"}), 200



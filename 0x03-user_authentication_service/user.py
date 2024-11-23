#!/usr/bin/env python3
"""
Route 
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the User Authentication Service")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Add authentication logic here
    return jsonify(message="Login successful")

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Add registration logic here
    return jsonify(message="Registration successful")

if __name__ == '__main__':
    app.run(debug=True)
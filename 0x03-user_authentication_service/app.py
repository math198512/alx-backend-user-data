#!/usr/bin/env python3
"""'Bienvenue' basic Flask app
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'Hello, World!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

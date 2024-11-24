#!/usr/bin/env python3
"""'Bienvenue' basic Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    try:
        AUTH.register_user(email, password)
    except Exception:
        return jsonify({"message": "email already registered"})
    return jsonify({"email": email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

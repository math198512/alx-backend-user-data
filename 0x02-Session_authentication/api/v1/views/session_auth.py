#!/usr/bin/env python3
"""Session authentication views module"""


from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles user login and creates a session"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == "":
        return jsonify({"error": "email missing"}), 400
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if len(users) <= 0:
        return jsonify({"error": "no user found for this email"}), 404

    if not users or not users.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(users.id)
    response = jsonify(users.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)
    return response

# @app_views.route('/auth_session/logout',
# methods=['DELETE'], strict_slashes=False)
# def logout():
#     """Handles user logout and deletes a session"""
#     if not auth.destroy_session(request):
#         abort(404)
#     return jsonify({}), 200

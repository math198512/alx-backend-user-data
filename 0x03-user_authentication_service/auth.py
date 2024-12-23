#!/usr/bin/env python3
"""
User Authentication Service
"""
from user import User
import bcrypt
from db import DB
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    Args:
        password (str): The password to hash.
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    returns a string representation of a new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with the provided email and password.

        Args:
            email (str): The email address of the user to register.
            password (str): The password for the user to register.

        Returns:
            User: The newly registered user object.

        Raises:
            ValueError: If the email is already registered.
        """
        try:
            self._db.find_user_by(email=email)
        except Exception:
            return self._db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists.")

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates if the provided email and password match a registered user.
        Args:
            email (str): The email address of the user.
            password (str): The password of the user.
        Returns:
            bool: True if the login is valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """
        It takes an email string argument and
        returns the session ID as a string
        """
        try:
            user = self._db.find_user_by(email=email)
        except Exception:
            return None
        sess_id = _generate_uuid()
        user.session_id = sess_id
        self._db.update_user(user.id, session_id=sess_id)
        return sess_id

#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
import base64
from typing import Tuple, TypeVar
import re
from .auth import Auth
import binascii
from models.user import User


user_type = TypeVar('User')


class BasicAuth(Auth):
    """Basic authentication class.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header[:6] == "Basic ":
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        """
        b64ah = base64_authorization_header
        if b64ah is None or type(b64ah) != str:
            return None
        try:
            res = base64.b64decode(
                b64ah,
                validate=True,
                )
            return res.decode("utf-8")
        except(binascii.Error):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        returns the user email and password from the Base64 decoded value.
        """
        db64ah = decoded_base64_authorization_header
        if db64ah is None or type(db64ah) != str:
            return (None, None)
        if ":" not in db64ah:
            return (None, None)
        else:
            return (db64ah.split(":")[0], db64ah.split(":")[1])

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> user_type:
        """returns the User instance based on his email and password."""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if not users[0].is_valid_password(user_pwd):
            return None
        return users[0]

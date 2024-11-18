#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
import base64
from typing import Tuple, TypeVar
import re
from .auth import Auth
import binascii


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

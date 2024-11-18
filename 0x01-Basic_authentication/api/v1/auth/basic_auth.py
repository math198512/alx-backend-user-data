#!/usr/bin/env python3
"""Basic authentication module for the API.
"""
import base64
import re
from .auth import Auth


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

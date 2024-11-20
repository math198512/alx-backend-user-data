#!/usr/bin/env python3
"""Session authentication module for the API.
"""
import base64
from typing import Tuple, TypeVar
import re
from .auth import Auth
import binascii
from models.user import User


user_type = TypeVar('User')


class SessionAuth(Auth):
    """Basic authentication class.
    """
    pass

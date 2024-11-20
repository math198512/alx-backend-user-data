#!/usr/bin/env python3
"""Session authentication module for the API.
"""
import base64
from typing import Tuple, TypeVar
import re
from .auth import Auth
import binascii
from models.user import User
import uuid


user_type = TypeVar('User')


class SessionAuth(Auth):
    """Basic authentication class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        self.id = str(uuid.uuid4())
        self.user_id_by_session_id[self.id] = user_id
        return self.id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:

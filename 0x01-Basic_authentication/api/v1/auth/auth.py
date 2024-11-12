#!/usr/bin/env python3
"""Authentication module for the API.
"""
from flask import request
from api.v1.views.users import User
from typing import List, TypeVar


user_type = TypeVar('User')


class Auth():
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths will be used later"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> user_type:
        """eturns None - request will be the Flask request object"""
        return None

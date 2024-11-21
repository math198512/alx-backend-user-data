#!/usr/bin/env python3
"""Authentication module for the API.
"""
from flask import request
from api.v1.views.users import User
from typing import List, TypeVar
import os


user_type = TypeVar('User')


class Auth():
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False - path and excluded_paths will be used later"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> user_type:
        """eturns None - request will be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """that returns a cookie value from a request"""
        if request is None:
            return None
        else:
            cookie = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie)

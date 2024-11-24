#!/usr/bin/env python3
"""
User Authentication Service
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    Args:
        password (str): The password to hash.
    Returns:
        bytes: The hashed password.
    """
    return bcrypt.hashpw(password, 14)

#!/usr/bin/env python3
"""
Auth module to handle user authentication logic with the database.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.   
    Args:password (str): The plain text password to hash.
    Returns:bytes: The hashed password.
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

#!/usr/bin/env python3
"""
Auth module for handling authentication related tasks.

This module defines the `Auth` class responsible for checking 
if authentication is required, handling authorization headers, 
and managing the current user.
"""

from typing import TypeVar, List
from flask import request

class Auth:
    """
    Auth class for handling authentication related tasks.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for the given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            path_unslash = self.slash_tolerant(path)
            excluded_path_unslash = self.slash_tolerant(excluded_path)
            if path_unslash == excluded_path_unslash:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.

        Args:
            request (Request): The request object to extract the header from.

        Returns:
            str: The value of the Authorization header or None if not present.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request.

        Args:
            request (Request): The request object to extract the user from.

        Returns:
            User: The current user associated with the request or None.
        """
        return request

    @staticmethod
    def slash_tolerant(value: str) -> str:
        """
        Removes the trailing slash from a string if present.

        Args:
            value (str): The string to process.

        Returns:
            str: The string without a trailing slash.
        """
        if value.endswith('/'):
            return value[:-1]
        return value

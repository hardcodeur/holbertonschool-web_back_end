#!/usr/bin/env python3

from typing import TypeVar, List
from flask import request

class Auth:
    """
    Auth class for handling authentication related tasks.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for the given path.

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
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request.
        """
        return request

    @staticmethod
    def slash_tolerant(value: str) -> str:
        """
        Removes the trailing slash from a string if present.
        """
        if value.endswith('/'):
            return value[:-1]
        return value


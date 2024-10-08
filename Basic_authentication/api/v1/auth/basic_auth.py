#!/usr/bin/env python3
"""
BasicAuth module for handling basic authentication.
This module provides methods to extract, decode,
and validate user credentials using basic authentication.
"""

from api.v1.auth.auth import Auth
from typing import TypeVar, Tuple, Optional
from models.user import User
import base64

UserType = TypeVar('UserType')


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    This class implements methods to manage basic authentication.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> Optional[str]:
        """
        Extracts the Base64 part of the authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[len('Basic '):]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> Optional[str]:
        """
        Decodes the Base64 encoded authorization header.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            authorization_decode = base64.b64decode(base64_authorization_header)
            return authorization_decode.decode('utf-8')
        except base64.binascii.Error:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Extracts user email and password from the decoded Base64 string.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> Optional[UserType]:
        """
        Retrieves the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> Optional[UserType]:
        """
        Retrieves the current user from the request.
        """
        if request is None:
            return None

        auth_header = super().authorization_header(request)
        base64_str = self.extract_base64_authorization_header(auth_header)
        decoded_str = self.decode_base64_authorization_header(base64_str)
        email, password = self.extract_user_credentials(decoded_str)
        user = self.user_object_from_credentials(email, password)

        return user

#!/usr/bin/env python3

from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64

class BasicAuth(Auth):

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header,str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        
        return authorization_header[len('Basic '):]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header,str):
            return None
        
        try:
            authorizationDecode = base64.b64decode(base64_authorization_header)
            return authorizationDecode.decode('utf-8')
        except base64.binascii.Error:
            return None
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        if decoded_base64_authorization_header is None:
            return (None,None)
        if not isinstance(decoded_base64_authorization_header,str):
            return (None,None)
        if ':' not in decoded_base64_authorization_header:
            return (None,None)
        
        email, password = decoded_base64_authorization_header.split(':')
        return (email,password)
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        if user_email is None and not isinstance(user_email,str):
            return None
        if user_pwd is None and not isinstance(user_pwd,str):
            return None
        
        if (User) :
            users = User.search({'email': user_email})
        else:
            return None

        
        if len(users) == 0:
            return None
        
        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None
        
        return user
    
    def current_user(self, request=None) -> TypeVar('User'):
        if request is None:
            return None
        
        auth_header = super().authorization_header(request)
        base64 = self.extract_base64_authorization_header(auth_header)
        decode = self.decode_base64_authorization_header(base64)
        id = self.extract_user_credentials(decode)
        user = self.user_object_from_credentials(id[0], id[1])
        
        return user
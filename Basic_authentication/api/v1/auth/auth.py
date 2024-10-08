#!/usr/bin/env python3

from typing import TypeVar
from flask import request 

class Auth : 

    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0 :
            return True
        for excluded_path in excluded_paths:
            pathUnslash = self.slashTolerant(path)
            excludedPathUnslash = self.slashTolerant(excluded_path)
            if pathUnslash == excludedPathUnslash : 
                return False
            else : 
                return True
    
    def authorization_header(self, request=None) -> str:
        if request is None:
            return None
        return request.headers.get('Authorization')


    def current_user(self, request=None) -> TypeVar('User'):
        return request
    
    @staticmethod
    def slashTolerant(value:str)->str:
        if value.endswith('/'):
            return value[:-1]
        else:
            return value
            


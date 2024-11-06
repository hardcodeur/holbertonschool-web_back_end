#!/usr/bin/env python3
from typing import Callable,Optional,Union
from functools import wraps
import redis
import uuid

def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        output = method(self, *args, **kwargs)
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))
        
        return output
    
    return wrapper

class Cache():

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self,data :Union[str, int, float, bytes])->str:
        randKey=str(uuid.uuid4())
        self._redis.set(randKey,data)
        return randKey

    def get(
            self, 
            key: str, 
            fn: Optional[
                Callable[[bytes], Union[str, int, float, bytes]]
                ] = None) -> Union[str, int, float, bytes, None]:
        
        keyValue=self._redis.get(key)
        if keyValue is None:
            return None
        
        if fn :
            return fn(keyValue)
        
        return keyValue
    
    def get_str(self,key: str)->Optional[str] :
        def utf8Decode(str :str):
            value=str.decode("utf-8")
            if value is None :
                return None
            return value
        
        return self.get(key,utf8Decode(self.get(key)))

    def get_int(self,key:str):

        def intMutate(str:str):
            value = int(str)

            if value is None : 
                return None
            
            return value
        
        return self.get(key,intMutate(self.get(key)))


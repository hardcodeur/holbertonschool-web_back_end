#!/usr/bin/env python3
from typing import Callable, Optional, Union
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

        # Store method output after calling it
        output = method(self, *args, **kwargs)
        self._redis.rpush(input_key, str(args))  # Save inputs
        self._redis.rpush(output_key, str(output))  # Save output

        return output
    return wrapper

def replay(method: Callable):
    redis_instance = redis.Redis()
    function_name = method.__qualname__
    call_count = redis_instance.get(function_name)
    
    try:
        call_count = int(call_count.decode('utf-8'))
    except (AttributeError, ValueError):
        call_count = 0
    
    time_str = "time:" if call_count == 1 else "times:"
    print(f'{function_name} was called {call_count} {time_str}')
    
    inputs = redis_instance.lrange(function_name + ":inputs", 0, -1)
    outputs = redis_instance.lrange(function_name + ":outputs", 0, -1)
    
    for input_value, output_value in zip(inputs, outputs):
        try:
            input_value = input_value.decode('utf-8')
        except Exception:
            input_value = ""
        try:
            output_value = output_value.decode('utf-8')
        except Exception:
            output_value = ""
        print(f'{function_name}(*{input_value}) -> {output_value}')

class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """Store data in Redis with a unique key and return the key."""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, int, float, bytes, None]:
        """
        Retrieve the data associated with 'key' and optionally transform it using 'fn'.
        """
        key_value = self._redis.get(key)
        
        # Return None if key does not exist
        if key_value is None:
            return None
        
        # Apply transformation function if provided
        if fn:
            return fn(key_value)
        
        return key_value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the data as a UTF-8 decoded string from Redis for a given key.
        """
        def utf8_decode(data: bytes) -> Optional[str]:
            try:
                return data.decode("utf-8")
            except (AttributeError, UnicodeDecodeError):
                return None

        return self.get(key, utf8_decode)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the data as an integer from Redis for a given key.
        """
        def int_mutate(data: bytes) -> Optional[int]:
            try:
                return int(data.decode("utf-8"))
            except (AttributeError, ValueError):
                return None

        return self.get(key, int_mutate)

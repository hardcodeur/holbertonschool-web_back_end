#!/usr/bin/env python3
"""
Module to implement a caching system using Redis. This module provides a
Cache class that allows storing, retrieving, and counting calls to cached
data with type annotations and proper documentation.
"""

from typing import Callable, Optional, Union
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    Increments a counter in Redis each time the method is invoked.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with counting functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a method.
    Stores the method's arguments and result in Redis lists.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method with call history functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        output = method(self, *args, **kwargs)
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))
        
        return output
    
    return wrapper


def replay(method: Callable) -> None:
    """
    Display the history of calls to a particular function, including the count,
    arguments, and outputs.

    Args:
        method (Callable): The method for which to replay the call history.
    """
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
        except (AttributeError, ValueError):
            input_value = ""
        try:
            output_value = output_value.decode('utf-8')
        except (AttributeError, ValueError):
            output_value = ""
        print(f'{function_name}(*{input_value}) -> {output_value}')


class Cache:
    """
    A class to interact with a Redis cache, supporting storage, retrieval, and
    call tracking functionalities.

    Attributes:
        _redis (redis.Redis): Redis client instance.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis connection and flushes the
        Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        Store data in Redis and return a unique key for retrieval.

        Args:
            data (Union[str, int, float, bytes]): Data to store in Redis.

        Returns:
            str: Unique key assigned to the stored data.
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(
        self, 
        key: str, 
        fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None
    ) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieve data from Redis and optionally apply a transformation function.

        Args:
            key (str): The key for the data in Redis.
            fn (Optional[Callable]): Optional function to transform the data.

        Returns:
            Optional[Union[str, int, float, bytes]]: Retrieved and optionally
            transformed data, or None if key does not exist.
        """
        key_value = self._redis.get(key)
        
        if key_value is None:
            return None
        
        if fn:
            return fn(key_value)
        
        return key_value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from Redis as a UTF-8 string.

        Args:
            key (str): The key for the data in Redis.

        Returns:
            Optional[str]: The retrieved data decoded as a UTF-8 string,
            or None if key does not exist.
        """
        return self.get(key, lambda data: data.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from Redis and convert it to an integer.

        Args:
            key (str): The key for the data in Redis.

        Returns:
            Optional[int]: The retrieved data converted to an integer,
            or None if key does not exist.
        """
        return self.get(key, lambda data: int(data))

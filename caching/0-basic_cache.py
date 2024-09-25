#!/usr/bin/python3
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic caching implementation."""

    def put(self, key, item):
        """
        Adds a key-value pair to the cache.

        Args:
            key (str): The key to associate with the item.
            item (object): The item to be cached.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache based on its key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The cached item if found, otherwise None.
        """
        return self.cache_data.get(key, None)
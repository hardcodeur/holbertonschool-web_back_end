#!/usr/bin/env python3

from base_caching import BaseCaching

""" Basic LIFO cache implementation."""

class LIFOCache(BaseCaching):
    """LIFO Cache class."""

    def __init__(self):
        """Initialize the LIFO Cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the LIFO Cache."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_last_item()
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the LIFO Cache."""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

    def discard_last_item(self):
        """Remove the least recently used item from the LIFO Cache."""
        delete_index = self.cache_data.popitem()
        print("DISCARD: {}".format(delete_index[0]))
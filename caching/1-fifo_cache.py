#!/usr/bin/env python3
""" Basic FIFO cache implementation."""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system inherits from BaseCaching."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache."""
        if key is not None and item is not None:
            if key not in self.cache_data.keys() and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.outFistStack()
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None

    def outFistStack(self):
        """Remove the first item added to the cache (FIFO)."""
        key_list = list(self.cache_data)
        delete_index = key_list[0]
        del self.cache_data[delete_index]
        print("DISCARD: {}".format(delete_index))

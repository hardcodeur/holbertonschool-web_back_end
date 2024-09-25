#!/usr/bin/env python3

from base_caching import BaseCaching

""" Basic FIFO cache implementation."""

class FIFOCache(BaseCaching):
    """
    FIFOCache class implementing a First-In-First-Out (FIFO) caching strategy.
    """

    def __init__(self):
        """
        Initializes the FIFOCache object, calling the parent class's constructor.
        """
        super().__init__()

    def put(self, key, item):
        """
        Adds a new item to the cache with the given key and value.
        If the cache is full, removes the oldest item (FIFO).

        Args:
            key (str): The key of the item to add.
            item (any): The value associated with the key.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_first_item()
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache using the given key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if not found.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

    def discard_first_item(self):
        """
        Removes the oldest item from the cache (FIFO).
        """
        first_key = list(self.cache_data.keys())[0]
        del self.cache_data[first_key]
        print("DISCARD: {}".format(first_key))

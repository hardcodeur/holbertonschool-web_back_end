#!/usr/bin/env python3
"""
Basic MRU (Most Recently Used) cache implementation.
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements
    the most recently used (MRU) cache eviction policy.
    """

    def __init__(self):
        """
        Initialize the MRUCache class by calling the parent class initializer.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.

        If the number of items in the cache exceeds the maximum allowed
        (BaseCaching.MAX_ITEMS), it discards the most recently used item
        before adding the new one.

        Args:
            key: The key for the cache.
            item: The item to add to the cache.
        """
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_last_item()
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        If the key is in the cache, move the key to the end to mark it
        as most recently used and return the item. Otherwise, return None.

        Args:
            key: The key to retrieve from the cache.

        Returns:
            The item associated with the key, or None if the key doesn't exist.
        """
        if key in self.cache_data:
            self.down_item_in_stack(key)
            return self.cache_data.get(key)
        return None

    def discard_last_item(self):
        """
        Discard the most recently used item from the cache.
        """
        delete_index = self.cache_data.popitem()
        print("DISCARD: {}".format(delete_index[0]))

    def down_item_in_stack(self, key):
        """
        Move the given key to the end of the cache to mark it as most recently used.

        Args:
            key: The key to move.
        """
        item = self.cache_data.pop(key)
        self.cache_data[key] = item

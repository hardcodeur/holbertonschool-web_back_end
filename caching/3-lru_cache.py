#!/usr/bin/env python3

from base_caching import BaseCaching

""" Basic LRU cache implementation."""

class LRUCache(BaseCaching):
    """LRU Cache class."""

    def __init__(self):
        """Initialize the LRU Cache."""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key of the item to add.
            item: The value of the item to add.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_last_item()
            self.cache_data[key] = item
            self.lift_item_to_top(key)

    def get(self, key):
        """Get an item from the cache.

        Args:
            key: The key of the item to get.

        Returns:
            The value of the item, or None if not found.
        """
        if key in self.cache_data:
            self.lift_item_to_top(key)
            return self.cache_data[key]
        else:
            return None

    def discard_last_item(self):
        """Discard the least recently used item from the cache."""
        last_item_key = list(self.cache_data.keys())[0]  # Get the key of the first item (least recently used)
        self.cache_data.pop(last_item_key)
        print("DISCARD: {}".format(last_item_key))

    def lift_item_to_top(self, key):
        """Lift the specified item to the top of the cache.

        Args:
            key: The key of the item to lift.
        """
        item = self.cache_data.pop(key)
        self.cache_data[key] = item


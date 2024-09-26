#!/usr/bin/env python3

"""Basic LRU cache implementation with proper documentation."""

BaseCaching = __import__('base_caching').BaseCaching



class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching and implements
    a basic Least Recently Used (LRU) cache system.
    """

    def __init__(self):
        """Initialize the class by calling the parent's constructor."""
        super().__init__()

    def put(self, key, item):
        """Assigns the item to the key in the cache.
        If the number of items in the cache exceeds the limit (MAX_ITEMS),
        it discards the least recently used item.
        
        Args:
            key: The key of the item to put in the cache.
            item: The item to store.
        """
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_last_item()
            self.cache_data[key] = item
            self.liftItemInStack(key)

    def get(self, key):
        """Retrieves the item associated with the given key from the cache.
        
        Args:
            key: The key of the item to retrieve.

        Returns:
            The value associated with the key, or None if the key doesn't exist.
        """
        if key in self.cache_data:
            self.liftItemInStack(key)
            return self.cache_data.get(key)
        return None

    def discard_last_item(self):
        """Removes the least recently used item from the cache."""
        deleteIndex = self.cache_data.popitem()
        print("DISCARD: {}".format(deleteIndex[0]))

    def liftItemInStack(self, key):
        """Moves the accessed item to the top of the cache to mark it as recently used.
        
        Args:
            key: The key of the item to move.
        """
        newStack = {key: self.cache_data[key]}
        self.cache_data.pop(key)
        newStack.update(self.cache_data)
        self.cache_data = newStack

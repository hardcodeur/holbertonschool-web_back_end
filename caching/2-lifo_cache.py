#!/usr/bin/env python3
BaseCaching = __import__('base_caching').BaseCaching

""" Basic LIFO cache implementation. """

class LIFOCache(BaseCaching):
    """ LIFO caching system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the class """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key not in self.cache_data.keys() and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.outLastStack()
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache """
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None

    def outLastStack(self):
        """ Remove the last item added to the cache (LIFO) """
        deleteIndex = self.cache_data.popitem()
        print("DISCARD: {}".format(deleteIndex[0]))

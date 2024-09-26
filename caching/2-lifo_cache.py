#!/usr/bin/env python3

""" Basic LIFO cache implementation. """

BaseCaching = __import__('base_caching').BaseCaching

class LIFOCache(BaseCaching):
    """ LIFO caching system that inherits from BaseCaching """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.lastDataKeyPut=""

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key not in self.cache_data.keys() and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.outLastItemPut(self.lastDataKeyPut)
            self.lastDataKeyPut = key
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key from the cache """
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None

    def outLastItemPut(self,key):
        """ Remove the last item added to the cache (LIFO) """
        self.cache_data.pop(key)
        print("DISCARD: {}".format(key))

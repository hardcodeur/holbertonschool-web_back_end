#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching

"""Basic cache implementation."""

class BasicCache(BaseCaching) :

    def put(self, key, item):
        if key != None or item != None : 
            self.cache_data[key] = item
    
    def get(self, key):
        return self.cache_data.get(key, None)
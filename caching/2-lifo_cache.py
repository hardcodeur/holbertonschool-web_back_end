#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching

""" Basic LFIO cache implementation."""

class LIFOCache(BaseCaching) :
        
    def __init__(self):
        super().__init__()

    def put(self, key, item):        
        if key != None or item != None :
            if key not in self.cache_data.keys() and  len(self.cache_data) >= BaseCaching.MAX_ITEMS :
                self.outLastStack()
            self.cache_data[key] = item
            
    def get(self, key):
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        else:
            return None

    def outLastStack(self):
        deleteIndex=self.cache_data.popitem()
        print("DISCARD: {}".format(deleteIndex[0]))
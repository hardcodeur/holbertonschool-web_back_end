#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching

""" Basic FIFO cache implementation."""

class FIFOCache(BaseCaching) :

    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        if key not in self.cache_data.keys() and  key != None or item != None :
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS :
                self.outFistStack()
            self.cache_data[key] = item
    
    
    def get(self, key):
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        else:
            return None

    def outFistStack(self):
        keyList = [*self.cache_data]
        deleteIndex=keyList[0]
        del self.cache_data[deleteIndex]
        print("DISCARD: {}".format(deleteIndex))


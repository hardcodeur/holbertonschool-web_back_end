#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching

""" Basic LRU cache implementation."""

class MRUCache(BaseCaching) :
        
    def __init__(self):
        super().__init__()

    def put(self, key, item):        
        if key != None or item != None :
            if key not in self.cache_data.keys() and len(self.cache_data) >= BaseCaching.MAX_ITEMS :
                self.discard_last_item()
            self.cache_data[key] = item
            
    def get(self, key):
        if key in self.cache_data.keys():
            self.downItemInStack(key)
            return self.cache_data.get(key)
        else:
            return None

    def discard_last_item(self):
        deleteIndex=self.cache_data.popitem()
        print("DISCARD: {}".format(deleteIndex[0]))
    
    def downItemInStack(self,key):
        newStack={key : self.cache_data[key]}
        self.cache_data.pop(key)
        self.cache_data.update(newStack)
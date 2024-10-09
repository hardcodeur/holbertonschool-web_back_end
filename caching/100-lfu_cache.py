#!/usr/bin/env python3

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_least_frequency_item(key)
            self.frequency[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None


    def getKeyLeastFrequencyItem(self):
        dataleastFrequencyOrder=dict(sorted(self.frequency.items(), key=lambda x: x[1], reverse=True))
        deleteItem = dataleastFrequencyOrder.popitem()
        return deleteItem[0]


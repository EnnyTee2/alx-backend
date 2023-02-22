#!/usr/bin/python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' First In First Out Cache System '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' Add an item to the cache'''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = [key for key in self.cache_data.keys()]
                del self.cache_data[keys[0]]
                print(f"DISCARD: {keys[0]}")

    def get(self, key):
        '''get an item with specified key from cache'''
        return self.cache_data.get(key)
    

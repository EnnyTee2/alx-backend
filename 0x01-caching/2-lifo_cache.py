#!/usr/bin/python3
""" LIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    ''' First In First Out Cache System '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        ''' Add an item to the cache
            Remove last item if cache size is
            greater than BaseCaching.MAX_ITEMS
        '''
        if key and item:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                keys = [key for key in self.cache_data.keys()]
                del self.cache_data[keys[-1]]
                print(f"DISCARD: {keys[-1]}")
            self.cache_data[key] = item

    def get(self, key):
        '''get an item with specified key from cache'''
        return self.cache_data.get(key)

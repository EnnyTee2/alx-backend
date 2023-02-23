#!/usr/bin/python3
""" LIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    ''' Least Recently Used Caching System '''
    def __init__(self):
        super().__init__()
        self.key_usage = []

    def put(self, key, item):
        ''' Add an item to the cache
            Remove last item if cache size is
            greater than BaseCaching.MAX_ITEMS
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.key_usage.append(key)

            updated = True if key in self.cache_data.keys() else False
            if updated:
                self.key_usage.remove(key)
                return

            if len(self.cache_data) > self.MAX_ITEMS:
                del self.cache_data[self.key_usage[0]]
                print(f"DISCARD: {self.key_usage[0]}")
                del self.key_usage[0]

        return

    def get(self, key):
        '''get an item with specified key from cache'''
        if key in self.cache_data:
            self.key_usage.append(key)
            self.key_usage.remove(key)
        return self.cache_data.get(key)

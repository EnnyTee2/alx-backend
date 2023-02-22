#!/usr/bin/python3
""" Basic dictionary Caching """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' Basic Caching Class '''

    def put(self, key, item):
        ''' put method for putting a new key and item '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        ''' get method for retrieving item stored in key '''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

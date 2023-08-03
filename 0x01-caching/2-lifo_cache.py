#!/bin/usr/env python3
"""LIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """Initializes cache"""
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                lastkey, _ = self.cache_data.popitem()
                print('DISCARD:', lastkey)

            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)


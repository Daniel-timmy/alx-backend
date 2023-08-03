#!/bin/usr/env python3
"""FIFOCache"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class"""

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """adds to the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mKey, _ = self.cache_data.popitem(False)
                print('DISCARD:', mKey)

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is None:
            return None
        return self.cache_data.get(key, None)

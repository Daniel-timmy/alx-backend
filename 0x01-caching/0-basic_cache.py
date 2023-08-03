#!/bin/usr/env python3
"""BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """caching system"""

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key."""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        if key is None:
            return None
        return self.cache_data.get(key, None)


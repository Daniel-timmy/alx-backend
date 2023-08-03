<<<<<<< HEAD
#!/bin/usr/env python3
"""BasicCache"""
=======
#!/usr/bin/env python3
"""Basic caching module.
"""
>>>>>>> origin/main
from base_caching import BaseCaching


class BasicCache(BaseCaching):
<<<<<<< HEAD
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

=======
    """Represents an object that allows storing and
    retrieving items from a dictionary.
    """
    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
>>>>>>> origin/main

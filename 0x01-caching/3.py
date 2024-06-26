#!/usr/bin/python3
""" BaseCaching module
"""

class LRUCache():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}
        self.frequency = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache with respect to FIFO
        """
        discarded = str()
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.frequency[key] += 1
        if len(self.cache_data) >= self.MAX_ITEMS:
            i = 0
            lru_item = next(iter(self.cache_data))
            for index in self.cache_data:
                if i > 0:
                    if self.cache_data[index] < self.cache_data[lru_item]:
                        lru_item = index
                        discarded = index
                    #else:
                        #lru_item = self.cache_data[index]
                i += 1
            self.cache_data.pop(lru_item)
            self.frequency.pop(lru_item)
            print("DISCARD:",discarded)
        self.cache_data[key] = item
        self.frequency[key] = 1

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

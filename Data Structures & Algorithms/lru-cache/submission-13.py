class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru_key = self.mru_key = None
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        prev_key, val, next_key = self.cache[key]
        if len(self.cache) == 1 or key == self.mru_key:
            return val

        if prev_key is not None:
            self.cache[prev_key][2] = next_key
        if next_key is not None:
            self.cache[next_key][0] = prev_key
        if key == self.lru_key:
            self.lru_key = next_key
        
        self.cache[self.mru_key][2] = key
        self.cache[key][0] = self.mru_key
        self.cache[key][2] = None
        self.mru_key = key
        
        return val
        

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == 0:
            self.cache[key] = [None, value, None]
            self.lru_key = self.mru_key = key
            return

        if key not in self.cache:
            self.cache[key] = [self.mru_key, value, None]
            self.cache[self.mru_key][2] = key
            self.mru_key = key
        else:
            self.cache[key][1] = value
            self.get(key)

        if len(self.cache) > self.capacity:
            new_lru_key = self.cache[self.lru_key][2]
            self.cache[new_lru_key][0] = None
            del self.cache[self.lru_key]
            self.lru_key = new_lru_key
        
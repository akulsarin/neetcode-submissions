class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {} # Contains (value, prevKey, nextKey)
        self.mru = None  # Contains key of MRU item (Head)
        self.lru = None  # Contains key of LRU item (Tail)

        
    def get(self, key: int) -> int:
        result = self.keyMap.get(key)
        if not result:
            return -1

        value, prevKey, nextKey = result
        if self.mru == key:
            return value
        if prevKey is not None:
            self.keyMap[prevKey][2] = nextKey
        if nextKey is not None:
            self.keyMap[nextKey][1] = prevKey
        else:
            self.lru = prevKey if prevKey is not None else key

        self.keyMap[key][1] = None
        self.keyMap[key][2] = self.mru
        self.keyMap[self.mru][1] = key
        self.mru = key

        return value

        
    def put(self, key: int, value: int) -> None:
        if not self.keyMap:
            self.keyMap[key] = [value, None, None]
            self.mru = key
            self.lru = key
            return

        currVal = self.get(key)
        if currVal != -1:
            self.keyMap[key][0] = value
            return


        self.keyMap[key] = [value, None, self.mru]
        self.keyMap[self.mru][1] = key
        self.mru = key

        if len(self.keyMap) > self.capacity:
            _, newLruKey, _  = self.keyMap[self.lru]
            del self.keyMap[self.lru]
            self.lru = newLruKey
            self.keyMap[self.lru][2] = None





        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val, prev, next = self.cache[key]

        if len(self.cache) == 1 or self.tail == key:
            return val
        
        if next is not None:
            self.cache[next][1] = prev
        
        if prev is not None:
            self.cache[prev][2] = next

        if self.head == key:
            self.head = next
        
        self.cache[key][1] = self.tail
        self.cache[key][2] = None

        if self.tail is not None:
            self.cache[self.tail][2] = key
        
        self.tail = key

        return val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key][0] = value
            self.get(key)
        else:
            self.cache[key] = [value, self.tail, None]
            if self.tail is not None:
                self.cache[self.tail][2] = key
            self.tail = key
            if self.head is None:
                self.head = key

        if len(self.cache) > self.capacity:
            curr_head = self.head
            self.head = self.cache[curr_head][2]
            self.cache[self.head][1] = None
            del self.cache[curr_head]

        

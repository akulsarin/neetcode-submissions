import bisect

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        idx = bisect.bisect(self.map[key], timestamp, key=lambda i: i[0])
        self.map[key].insert(idx, (timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.map[key], timestamp, key=lambda i: i[0])
        if idx == 0:
            return ""
        return self.map[key][idx - 1][1]

        

import bisect

class TimeMap:

    def __init__(self):
        self.map = defaultdict(lambda: [(-1, "")])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect(self.map[key], timestamp, key=lambda i: i[0])
        return self.map[key][idx - 1][1]

        

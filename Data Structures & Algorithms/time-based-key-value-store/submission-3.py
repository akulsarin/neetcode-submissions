class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        mapVals = self.map[key]

        l, r = 0, len(mapVals) - 1
        closest = ""
        while l <= r:
            mid = (l + r) // 2
            if mapVals[mid][0] == timestamp:
                return mapVals[mid][1]
            elif mapVals[mid][0] < timestamp:
                closest = mapVals[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return closest
        
        


        

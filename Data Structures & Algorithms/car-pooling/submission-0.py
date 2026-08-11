class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        N = len(trips)
        events = []

        for passengers, src, dst in trips:
            events.append((src, passengers))
            events.append((dst, -passengers))

        events.sort()
        passengers = 0
        for _, count in events:
            passengers += count
            if passengers > capacity:
                return False
        return True
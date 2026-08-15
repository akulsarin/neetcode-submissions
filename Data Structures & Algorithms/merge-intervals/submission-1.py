class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = defaultdict(int)
        for start, end in intervals:
            events[start] += 1
            events[end] -= 1
        
        merged = []
        interval = []
        openIntervals = 0
        for event in sorted(events.keys()):
            if not interval:
                interval.append(event)
            openIntervals += events[event]
            if openIntervals == 0:
                interval.append(event)
                merged.append(interval)
                interval = []
        return merged

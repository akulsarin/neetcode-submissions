"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = defaultdict(int)
        for interval in intervals:
            events[interval.start] += 1
            events[interval.end] -= 1

        rooms_needed = 0
        meetings = 0
        for time in sorted(events):
            meetings += events[time]
            rooms_needed = max(rooms_needed, meetings)
        
        return rooms_needed
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

        rooms = 0
        ans = 0
        for event in sorted(events.keys()):
            rooms += events[event]
            ans = max(ans, rooms)

        return ans
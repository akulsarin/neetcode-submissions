import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)

        startIdx = bisect.bisect_left(intervals, newInterval)
        if startIdx > 0 and intervals[startIdx - 1][1] >= newInterval[0]:
            startIdx -= 1
            newInterval[0] = intervals[startIdx][0]

        endIdx = startIdx
        while endIdx < N and newInterval[1] >= intervals[endIdx][0]:
            newInterval[1] = max(intervals[endIdx][1], newInterval[1])
            endIdx += 1

        return intervals[:startIdx] + [newInterval] + intervals[endIdx:]
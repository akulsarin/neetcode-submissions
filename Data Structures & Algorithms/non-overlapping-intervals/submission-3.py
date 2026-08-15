class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()

        prevEnd = intervals[0][1]
        res = 0
        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
                continue
            
            res += 1
            prevEnd = min(prevEnd, interval[1])

        return res
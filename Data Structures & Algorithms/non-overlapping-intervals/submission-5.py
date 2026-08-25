class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd:
                prevEnd = min(end, prevEnd)
                count += 1
            else:
                prevEnd = end
        return count
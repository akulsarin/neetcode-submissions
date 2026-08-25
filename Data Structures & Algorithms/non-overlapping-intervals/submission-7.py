class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval: interval[1])
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prevEnd:
                count += 1
            else:
                prevEnd = end
        return count
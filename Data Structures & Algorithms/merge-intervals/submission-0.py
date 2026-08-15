class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= newIntervals[-1][1]:
                newIntervals[-1][1] = max(newIntervals[-1][1], interval[1])
            else:
                newIntervals.append(interval)
        return newIntervals
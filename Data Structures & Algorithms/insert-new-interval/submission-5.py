class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        new_intervals = []
        
        i = 0
        while i < N and newInterval[0] > intervals[i][1]:
            new_intervals.append(intervals[i])
            i += 1
        if i < N:
            newInterval[0] = min(newInterval[0], intervals[i][0])

        while i < N and newInterval[1] >= intervals[i][0]:
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        new_intervals.append(newInterval)

        while i < N:
            new_intervals.append(intervals[i])
            i += 1
        
        return new_intervals
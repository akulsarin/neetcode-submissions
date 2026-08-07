class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        globMin, globMax = arrays[0][0], arrays[0][-1]
        res = 0
        for array in arrays[1:]:
            currMin, currMax = array[0], array[-1]
            res = max(res, abs(currMax - globMin), abs(globMax - currMin))
            globMin = min(globMin, currMin)
            globMax = max(globMax, currMax)
        return res
        
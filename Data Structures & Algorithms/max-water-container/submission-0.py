class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        currMax = 0
        while l < r:
            currVol = (r - l) * min(heights[l], heights[r])
            currMax = max(currMax, currVol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return currMax

        
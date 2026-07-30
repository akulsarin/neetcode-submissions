class Solution:
    def maxArea(self, heights: List[int]) -> int:
        N = len(heights)
        l, r = 0, N - 1

        currMax = -1

        while l < r:
            canStore = (r - l) * min(heights[l], heights[r])
            currMax = max(currMax, canStore)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return currMax
        
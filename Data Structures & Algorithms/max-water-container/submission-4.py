class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_amount = min(heights[r], heights[l]) * (r - l)
        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            amount = min(heights[r], heights[l]) * (r - l)
            max_amount = max(max_amount, amount)
        return max_amount
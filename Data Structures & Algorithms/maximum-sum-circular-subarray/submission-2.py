class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin = nums[0], nums[0]
        curMax, curMin, total = 0, 0, 0

        for num in nums:
            curMax = max(num, curMax + num)
            globMax = max(globMax, curMax)

            curMin = min(num, curMin + num)
            globMin = min(globMin, curMin)

            total += num

        return max(globMax, total - globMin) if globMax > 0 else globMax
        
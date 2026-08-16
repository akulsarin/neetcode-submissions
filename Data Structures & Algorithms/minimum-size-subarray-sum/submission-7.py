class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        currentSum = 0
        minLen = len(nums) + 1
        for r in range(len(nums)):
            currentSum += nums[r]
            while currentSum >= target:
                minLen = min(minLen, r - l + 1)
                currentSum -= nums[l]
                l += 1

        return minLen if minLen <= len(nums) else 0
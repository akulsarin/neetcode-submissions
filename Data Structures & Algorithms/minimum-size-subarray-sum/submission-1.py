class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minSoFar = len(nums) + 1
        currCount = 0
        runningSum = 0

        for r in range(len(nums)):
            runningSum += nums[r]
            currCount += 1
            while runningSum >= target:
                minSoFar = min(minSoFar, currCount)
                runningSum -= nums[l]
                l += 1
                currCount -= 1

        return minSoFar if minSoFar <= len(nums) else 0

        
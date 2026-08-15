class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = currSum

        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSum = max(maxSum, currSum)

        return maxSum

        
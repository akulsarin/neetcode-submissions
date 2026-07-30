class Solution:
    def rob(self, nums: List[int]) -> int:
        # max(nums[i] + dp[i - 2], dp[i - 1])
        if len(nums) <= 2:
            return max(nums)

        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            max_at_i = max(nums[i] + dp[0], dp[1])
            dp[0], dp[1] = dp[1], max_at_i
            i += 1

        return dp[1]
            


        
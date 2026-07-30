class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0 or len(nums) < 2:
            return False

        targetSum = totalSum // 2
        dp = [[False] * (targetSum + 1) for _ in nums]

        for t in range(1, targetSum + 1):
            dp[0][t] = t == nums[0]


        for i in range(1, len(nums)):
            for t in range(1, targetSum + 1):
                # Skip this
                dp[i][t] = dp[i - 1][t]

                # Include this
                if t - nums[i] >= 0:
                    dp[i][t] = dp[i][t] or dp[i - 1][t - nums[i]]

        return dp[-1][-1]

                


        
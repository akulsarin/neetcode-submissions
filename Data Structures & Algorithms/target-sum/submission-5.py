class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        maxAdd = sum(nums)
        if abs(target) > abs(maxAdd):
            return 0

        totalRange = 2 * maxAdd

        # dp[i][j] := # of expressions s.t. nums up to i-th index sum to j - maxAdd
        dp = [[0] * (totalRange + 1) for _ in nums]

        dp[0][maxAdd + nums[0]] += 1
        dp[0][maxAdd - nums[0]] += 1

        for i in range(1, len(nums)):
            for j in range(totalRange + 1):
                t = j - maxAdd
                num = nums[i]

                # Subtract it: x - num = t => x = t + num
                if t + num + maxAdd <= totalRange:
                    dp[i][j] += dp[i - 1][t + num + maxAdd]
                
                # Add it: x + num = t => x = t - num
                if t - num + maxAdd >= 0:
                    dp[i][j] += dp[i - 1][t - num + maxAdd]
        print(dp)
        return dp[-1][target + maxAdd]





        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        max_sum = sum(nums)
        if abs(target) > max_sum:
            return 0
        
        M = len(nums)
        N = 2 * max_sum

        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[0][max_sum] = 1

        for i in range(1, M + 1):
            for t in range(-max_sum, max_sum + 1):
                j = t + max_sum
                num = nums[i - 1]

                if j - num >= 0:
                    dp[i][j] += dp[i - 1][j - num]
                
                if j + num <= N:
                    dp[i][j] += dp[i - 1][j + num]
        
        return dp[M][target + max_sum]
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        M, N = len(nums), 2 * total

        if abs(target) > total:
            return 0
        
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[0][total] = 1

        for i in range(1, M + 1):
            for t in range(-total, total + 1):
                j = t + total
                num = nums[i - 1]

                # Add num
                if j - num >= 0:
                    dp[i][j] += dp[i - 1][j - num]

                # Subtract num
                if j + num <= N:
                    dp[i][j] += dp[i - 1][j + num]

        return dp[M][target + total]
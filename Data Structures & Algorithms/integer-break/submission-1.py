class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            for k in range(1, i):
                dp[i] = max(dp[i], k * (i - k), k * dp[i - k])
        
        return dp[n]
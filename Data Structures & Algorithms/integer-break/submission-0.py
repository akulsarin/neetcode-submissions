class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i][i] = 1
            dp[i][1] = i

        for i in range(2, n + 1):
            for k in range(2, i):
                for summand in range(1, i - k + 2):
                    dp[i][k] = max(dp[i][k], summand * dp[i - summand][k - 1])
        
        return max(dp[n][2:])
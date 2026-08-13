class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 1:
            return k ** n

        dp = [0] * n
        dp[0], dp[1] = k, k * k
        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])
        
        return dp[-1]
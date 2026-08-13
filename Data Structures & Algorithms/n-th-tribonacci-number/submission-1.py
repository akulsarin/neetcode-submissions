class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n <= 2:
            return dp[n]
        for _ in range(3, n + 1):
            ti = sum(dp)
            dp[0], dp[1], dp[2] = dp[1], dp[2], ti
        return dp[-1]
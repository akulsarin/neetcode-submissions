class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(m - 1):
            curr = 1
            for j in range(n - 2, -1, -1):
                dp[j] += curr
                curr = dp[j]
            
        return dp[0]
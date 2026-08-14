class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n

        for _ in range(m):
            curr = [0] * n
            curr[-1] = 1
            for i in range(n - 2, -1, -1):
                curr[i] = curr[i + 1] + dp[i]
            dp = curr
        
        return dp[0]
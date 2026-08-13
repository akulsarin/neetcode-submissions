class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n + 1))

        for i in range(2, n + 1):
            rootFloor = int((i ** (1/2)) // 1)
            for j in range(1, rootFloor + 1):
                dp[i] = min(dp[i], 1 + dp[i - (j ** 2)])

        return dp[n]
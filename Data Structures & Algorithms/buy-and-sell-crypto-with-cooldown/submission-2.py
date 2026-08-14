class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[float('-inf'), float('-inf')] for _ in range(N + 2)]
        dp[N] = [0, 0]
        dp[N + 1] = [0, 0]

        for i in range(N - 1, -1, -1):
            dp[i][0] = max(-prices[i] + dp[i + 1][1], dp[i + 1][0])
            dp[i][1] = max(prices[i] + dp[i + 2][0], dp[i + 1][1])

        return dp[0][0]
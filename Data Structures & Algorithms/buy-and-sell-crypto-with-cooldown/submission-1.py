class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        numDays = len(prices)
        numActions = 4 # Buy/Sell/Hold/Cool
        dp = [[0] * numActions for _ in range(numDays)]

        dp[0][0] = -prices[0]
        dp[0][1] = float('-inf')
        dp[0][2] = float('-inf')
        dp[0][3] = 0

        for p in range(1, numDays):
            dp[p][0] = dp[p - 1][-1] - prices[p]
            dp[p][1] = max(dp[p - 1][0], dp[p - 1][2]) + prices[p]
            dp[p][2] = max(dp[p - 1][2], dp[p - 1][0])
            dp[p][3] = max(dp[p - 1][3], dp[p - 1][1])

        return max(dp[-1])



        
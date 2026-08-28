class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        
        dp = [[float('inf')] * (amount + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 0

        for i in range(1, N + 1):
            for target in range(1, amount + 1):
                dp[i][target] = dp[i - 1][target]

                curr_coin = coins[i - 1]
                diff = target - curr_coin
                if diff >= 0:
                    dp[i][target] = min(dp[i][target], 1 + dp[i][diff])
        
        if dp[N][amount] == float('inf'):
            return -1
        return dp[N][amount]
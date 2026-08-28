class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for target in range(coin, amount + 1):
                dp[target] = min(dp[target], 1 + dp[target - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(N):
            dp_next = [float('inf')] * (amount + 1)
            dp_next[0] = 0
            for target in range(1, amount + 1):
                dp_next[target] = dp[target]

                diff = target - coins[i]
                if diff >= 0:
                    dp_next[target] = min(dp_next[target], 1 + dp_next[diff])
            dp = dp_next
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
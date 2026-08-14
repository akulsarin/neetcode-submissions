class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        
        dp = [[0] * (amount + 1) for _ in range(N + 1)]
        for r in range(N + 1):
            dp[r][0] = 1

        for r in range(1, N + 1):
            for t in range(1, amount + 1):
                coin = coins[r - 1]
                dp[r][t] = dp[r - 1][t]
                if t - coin >= 0:
                    dp[r][t] += dp[r][t - coin]

        return dp[N][amount]
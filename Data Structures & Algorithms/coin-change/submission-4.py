class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N, M = len(coins), amount
        dp = [[float('inf')] * (M + 1) for _ in range(N)]
        
        for t in range(M + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]

        for c in range(1, N):
            for t in range(M + 1):
                dp[c][t] = dp[c - 1][t]
                if t - coins[c] >= 0:
                    dp[c][t] = min(dp[c][t], dp[c][t - coins[c]] + 1)

        if dp[N - 1][M] == float('inf'):
            return -1

        return dp[N - 1][M] 
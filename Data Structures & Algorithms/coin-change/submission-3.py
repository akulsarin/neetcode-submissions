class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N, M = len(coins), amount
        dp = [[float('inf')] * (M + 1) for _ in range(N)]
        
        for t in range(M + 1):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]

        for i in range(1, N):
            for t in range(M + 1):
                # Exclude
                exclude = dp[i - 1][t]

                # Include
                include = float('inf')
                if t - coins[i] >= 0:
                    include = dp[i][t - coins[i]] + 1

                dp[i][t] = min(exclude, include)

        if dp[N - 1][M] == float('inf'):
            return -1

        return dp[N - 1][M]
        
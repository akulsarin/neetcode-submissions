class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N, M = len(coins), amount
        dp = [[0] * (M + 1) for _ in range(N)]

        for i in range(N):
            dp[i][0] = 1
        
        for t in range(1, M + 1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        for i in range(1, N):
            for t in range(M + 1):
                # Exclude
                exclude = dp[i - 1][t]

                # Include
                include = 0
                if t - coins[i] >= 0:
                    include = dp[i][t - coins[i]]

                dp[i][t] = exclude + include

        # print(dp)
        return dp[N - 1][M]
        
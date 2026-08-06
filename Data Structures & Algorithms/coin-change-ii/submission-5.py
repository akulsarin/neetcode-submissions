class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        M, N = len(coins), amount
        dp = [[0] * (N + 1) for _ in range(M)]

        for i in range(M):
            dp[i][0] = 1

        for j in range(1, N + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1

        for i in range(1, M):
            for j in range(1, N + 1):
                dp[i][j] = dp[i - 1][j]

                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]

        return dp[-1][-1]

        
        
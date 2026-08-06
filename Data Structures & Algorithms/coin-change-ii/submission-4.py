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
                # dp[i][j] := no. of unique ways to make amount j with coins[:i]
                
                # Without using current coin:
                dp[i][j] = dp[i - 1][j]

                if j - coins[i] >= 0:
                    # With using current coin once:
                    # dp[i][j] += dp[i - 1][j - coins[i]]

                    # With using current coin multiple times:
                    dp[i][j] += dp[i][j - coins[i]]

        return dp[-1][-1]

        
        
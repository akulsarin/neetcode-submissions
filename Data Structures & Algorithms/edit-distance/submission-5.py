class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        
        dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            dp[i][N] = M - i
        for j in range(N):
            dp[M][j] = N - j

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                c1, c2 = word1[i], word2[j]
                if c1 == c2:
                    dp[i][j] = dp[i + 1][j + 1]
                    continue
                
                # 1. Replace it
                dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j + 1])

                # 2. Delete it
                dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])

                # Insert new character
                dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])

        return dp[0][0]
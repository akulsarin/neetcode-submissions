class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        if min(M, N) == 0:
            return max(M, N)

        dp = [[float('inf')] * (N + 1) for _ in range(M + 1)]

        for i in range(M + 1):
            dp[i][0] = i

        for j in range(N + 1):
            dp[0][j] = j

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                c1, c2 = word1[i - 1], word2[j - 1]

                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    replace = dp[i - 1][j - 1]
                    delete = dp[i - 1][j]
                    insert = dp[i][j - 1]
                    dp[i][j] = min(replace, insert, delete) + 1

        return dp[M][N]






        
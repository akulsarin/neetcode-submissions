class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        if M + N != len(s3):
            return False

        dp = [[False]* (N + 1) for _ in range(M + 1)]
        dp[0][0] = True

        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 and j == 0:
                    continue

                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]

                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]

        return dp[M][N]
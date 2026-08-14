class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N = len(s1), len(s2)
        if M + N != len(s3):
            return False

        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = True
        for r in range(1, M + 1):
            dp[r][0] = dp[r - 1][0] and s1[r - 1] == s3[r - 1]
        for c in range(1, N + 1):
            dp[0][c] = dp[0][c - 1] and s2[c - 1] == s3[c - 1]

        for r in range(1, M + 1):
            for c in range(1, N + 1):
                dp[r][c] |= dp[r - 1][c] and s1[r - 1] == s3[r + c - 1]
                dp[r][c] |= dp[r][c - 1] and s2[c - 1] == s3[r + c - 1]

        return dp[M][N]
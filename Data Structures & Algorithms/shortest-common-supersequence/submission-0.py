class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        M, N = len(str1), len(str2)
        dp = [[''] * (N + 1) for _ in range(M + 1)]

        for i in range(M + 1):
            dp[i][0] = str1[:i]
        
        for j in range(N + 1):
            dp[0][j] = str2[:j]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                c1, c2 = str1[i - 1], str2[j - 1]

                if c1 == c2:
                    dp[i][j] = dp[i - 1][j - 1] + c1
                else:
                    if len(dp[i - 1][j]) <= len(dp[i][j - 1]):
                        dp[i][j] = dp[i - 1][j] + c1
                    else:
                        dp[i][j] = dp[i][j - 1] + c2

        return dp[M][N]

        
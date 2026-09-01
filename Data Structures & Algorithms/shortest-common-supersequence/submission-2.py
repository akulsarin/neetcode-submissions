class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        M, N = len(str1), len(str2)
        
        dp = [[""] * (N + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            dp[i][N] = str1[i:]
        for j in range(N + 1):
            dp[M][j] = str2[j:]

        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                elif len(dp[i + 1][j]) < len(dp[i][j + 1]):
                    dp[i][j] = str1[i] + dp[i + 1][j]
                else:
                    dp[i][j] = str2[j] + dp[i][j + 1]
        
        return dp[0][0]
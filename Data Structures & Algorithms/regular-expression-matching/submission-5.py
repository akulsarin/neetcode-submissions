class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)

        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[M][N] = True

        for i in range(M, -1, -1):
            for j in range(N - 1, -1, -1):
                match = i < M and (s[i] == p[j] or p[j] == ".")
                if j + 1 < N and p[j + 1] == "*":
                    no_wildcard = dp[i][j + 2]
                    wildcard = match and dp[i + 1][j]
                    dp[i][j] = wildcard or no_wildcard
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        
        return dp[0][0]
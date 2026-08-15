class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        
        dp = [[False] * (N + 1) for _ in range(M + 1)]
        dp[M][N] = True

        for i in range(M, -1, -1):
            for j in range(N - 1, -1, -1):
                match = i < M and j < N and p[j] in {s[i], "."}

                if j + 1 < N and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2]
                    if match:
                        dp[i][j] |= dp[i + 1][j]
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]
        
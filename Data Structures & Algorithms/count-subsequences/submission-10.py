class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M, N = len(s), len(t)
        
        dp = [0] * (N + 1)
        dp[-1] = 1

        for i in range(M - 1, -1, -1):
            dp_next = [0] * (N + 1)
            dp_next[-1] = 1
            for j in range(N - 1, -1, -1):
                dp_next[j] = dp[j]
                if s[i] == t[j]:
                    dp_next[j] += dp[j + 1] 
            dp = dp_next

        return dp[0]
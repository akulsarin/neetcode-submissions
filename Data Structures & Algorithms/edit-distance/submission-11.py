class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        
        dp = [float('inf')] * (N + 1)
        for j in range(N + 1):
            dp[j] = N - j

        for i in range(M - 1, -1, -1):
            curr = [float('inf')] * (N + 1)
            curr[-1] = M - i
            for j in range(N - 1, -1, -1):
                if word1[i] == word2[j]:
                    curr[j] = dp[j + 1]
                else:
                    replace = 1 + dp[j + 1]
                    delete = 1 + dp[j]
                    insert = 1 + curr[j + 1]
                    curr[j] = min(replace, delete, insert)
            dp = curr
        
        return dp[0]
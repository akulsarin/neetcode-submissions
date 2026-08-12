class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        N = len(s)
        words = set(dictionary)

        # dp[i] := minimum extra chars needed for s[i:]
        dp = [float('inf') for _ in range(N + 1)]
        dp[-1] = 0

        for i in range(N - 1, -1, -1):
            # Skip current letter
            dp[i] = 1 + dp[i + 1]

            # Include current letter
            for j in range(i, N):
                if s[i:j+1] in words:
                    dp[i] = min(dp[i], dp[j + 1])
        
        return dp[0]
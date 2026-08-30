class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        
        dp = [0] * (N + 1)
        dp[N] = 1
        if s[N - 1] != "0":
            dp[N - 1] = 1 
        
        for i in range(N - 2, -1, -1):
            if s[i] == "0":
                continue
            
            if 10 <= int(s[i] + s[i + 1]) <= 26:
                dp[i] += dp[i + 2]
            
            if s[i + 1] != "0":
                dp[i] += dp[i + 1]

        return dp[0]
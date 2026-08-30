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
            
            dp[i] = dp[i + 1]
            if "10" <= s[i] + s[i + 1] <= "26":
                dp[i] += dp[i + 2]

        return dp[0]
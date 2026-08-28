class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        dp = [[False] * (n + 2) for _ in range(n + 1)]
        dp[n][0] = True
        
        for i in range(n - 1, -1, -1):
            for num_open in range(n + 1):
                if s[i] == "(":
                    dp[i][num_open] = dp[i + 1][num_open + 1]
                elif s[i] == ")":
                    dp[i][num_open] = num_open > 0 and dp[i + 1][num_open - 1]
                else:
                    empty = dp[i + 1][num_open]
                    opened = dp[i + 1][num_open + 1]
                    closed = num_open > 0 and dp[i + 1][num_open - 1]
                    dp[i][num_open] = empty or opened or closed
                        
        return dp[0][0]
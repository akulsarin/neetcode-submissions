class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        dp = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]
            
            if j == N:
                dp[(i, j)] = (i == M)
                return dp[(i, j)]

            match = i < M and (s[i] == p[j] or p[j] == ".")
            if j + 1 < N and p[j + 1] == "*":
                no_wildcard = dfs(i, j + 2)
                wildcard = match and dfs(i + 1, j)
                dp[(i, j)] = wildcard or no_wildcard
            else:
                dp[(i, j)] = match and dfs(i + 1, j + 1)
            
            return dp[(i, j)]
        
        return dfs(0, 0)
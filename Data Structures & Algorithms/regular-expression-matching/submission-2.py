class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M, N = len(s), len(p)
        dp = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]

            match = i < M and j < N and p[j] in {s[i], "."}

            if i == M and j == N:
                dp[(i, j)] = True
            elif j == N:
                dp[(i, j)] = False
            elif j + 1 < N and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2)
                if match:
                    dp[(i, j)] |= dfs(i + 1, j)
            elif match:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = False

            return dp[(i, j)]


        return dfs(0, 0)
        
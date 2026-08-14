class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        dp = {}

        def dfs(r: int, c: int, fromVal: int) -> int:
            if (r, c, fromVal) in dp:
                return dp[(r, c, fromVal)]

            if min(r, c) < 0 or r == M or c == N or matrix[r][c] <= fromVal:
                return 0

            dp[(r, c, fromVal)] = 0
            currVal = matrix[r][c]
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                dp[(r, c, fromVal)] = max(dp[(r, c, fromVal)], 1 + dfs(r2, c2, currVal))

            return dp[(r, c, fromVal)]

        maxSeen = 0
        for r in range(M):
            for c in range(N):
                maxSeen = max(maxSeen, dfs(r, c, -1))

        return maxSeen
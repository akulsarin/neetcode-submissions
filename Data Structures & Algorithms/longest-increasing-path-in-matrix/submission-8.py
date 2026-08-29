class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        dp = [[0] * COLS for _ in range(ROWS)]

        def dfs(r: int, c: int, prev: int) -> int:
            if min(r, c) < 0 or r == ROWS or c == COLS or matrix[r][c] <= prev:
                return 0

            if dp[r][c]:
                return dp[r][c]
            
            curr_val = matrix[r][c]
            curr_max = 1
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                curr_max = max(curr_max, 1 + dfs(r2, c2, curr_val))
            dp[r][c] = curr_max
            return dp[r][c]

        max_seen = 1
        for r in range(ROWS):
            for c in range(COLS):
                max_seen = max(max_seen, dfs(r, c, float('-inf')))
        
        return max_seen
from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        dp = [[0] * COLS for _ in range(ROWS)]

        @cache
        def dfs(r: int, c: int) -> int:
            curr_val = matrix[r][c]
            curr_max = 1
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < ROWS and 0 <= c2 < COLS and matrix[r2][c2] > curr_val:
                    curr_max = max(curr_max, 1 + dfs(r2, c2))
            return curr_max

        return max(dfs(r, c) for r in range(ROWS) for c in range(COLS))
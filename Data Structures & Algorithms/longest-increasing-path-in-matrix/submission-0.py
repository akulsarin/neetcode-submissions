class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        cache = {}
        maxSoFar = 0

        def dfs(r: int, c: int) -> int:
            if (r, c) in cache:
                return cache[(r, c)]
            
            currMax = 0
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or matrix[r2][c2] <= matrix[r][c]:
                    continue
                currMax = max(currMax, 1 + dfs(r2, c2))

            cache[(r, c)] = currMax
            return currMax

        for r in range(ROWS):
            for c in range(COLS):
                maxSoFar = max(maxSoFar, dfs(r, c))

        return 1 + maxSoFar

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r: int, c: int) -> None:
            grid[r][c] = "0"
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < ROWS and 0 <= c2 < COLS and grid[r2][c2] == "1":
                    dfs(r2, c2)
        
        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
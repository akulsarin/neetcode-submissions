class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dp = grid[-1].copy()
        for c in range(COLS - 2, -1, -1):
            dp[c] += dp[c + 1]

        for r in range(ROWS - 2, -1, -1):
            curr = [0] * COLS
            curr[-1] = grid[r][-1] + dp[-1]
            for c in range(COLS - 2, -1, -1):
                curr[c] = grid[r][c] + min(curr[c + 1], dp[c])
            dp = curr
        
        return dp[0]
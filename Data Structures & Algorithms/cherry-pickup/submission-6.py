class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dp = [[[float('-inf')] * (ROWS + 1) for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        dp[ROWS - 1][COLS - 1][ROWS - 1] = grid[ROWS - 1][COLS - 1]

        for r1 in range(ROWS - 1, -1, -1):
            for c1 in range(COLS - 1, -1, -1):
                for r2 in range(ROWS - 1, -1, -1):
                    c2 = r1 + c1 - r2
                    if c2 < 0 or c2 >= COLS:
                        continue
                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        dp[r1][c1][r2] = float('-inf')
                        continue
                    if r1 == ROWS - 1 and c1 == COLS - 1 and r2 == ROWS - 1:
                        continue
                    numCherries = grid[r1][c1] + grid[r2][c2]
                    if r1 == r2 and c1 == c2:
                        numCherries //= 2
                    dp[r1][c1][r2] = max(
                        dp[r1 + 1][c1][r2 + 1],
                        dp[r1][c1 + 1][r2],
                        dp[r1 + 1][c1][r2],
                        dp[r1][c1 + 1][r2 + 1],
                    ) + numCherries
        return max(0, dp[0][0][0])
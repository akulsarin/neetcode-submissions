class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0
        
        dp = [0] * COLS
        dp[COLS - 1] = 1
        
        for r in range(ROWS - 1, -1, -1):
            dp_next = [0] * COLS
            dp_next[COLS - 1] = dp[COLS - 1] * (1 - obstacleGrid[r][COLS - 1])
            for c in range(COLS - 2, -1, -1):
                dp_next[c] = (dp_next[c + 1] + dp[c]) * (1 - obstacleGrid[r][c])
            dp = dp_next
        
        return dp[0]
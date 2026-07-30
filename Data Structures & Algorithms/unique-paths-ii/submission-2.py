class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[-1] = 1

        for r in range(m - 1, -1, -1):
            if obstacleGrid[r][-1] == 1:
                dp[-1] = 0

            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] += dp[c + 1]

        return dp[0]
                
        
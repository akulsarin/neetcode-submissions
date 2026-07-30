class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * n
        prevRow[-1] = 1

        for r in range(m - 1, -1, -1):
            currRow = [0] * n
            if obstacleGrid[r][-1] == 1:
                currRow[-1] = 0
            else:
                currRow[-1] = prevRow[-1]


            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    currRow[c] = 0
                else:
                    currRow[c] = prevRow[c] + currRow[c + 1]

            prevRow = currRow

        return currRow[0]
                
        
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * COLS for _ in range(ROWS)]

        maxSoFar = 0
        for r in range(ROWS):
            dp[r][0] = int(matrix[r][0])
            maxSoFar = max(maxSoFar, dp[r][0])
        
        for c in range(1, COLS):
            dp[0][c] = int(matrix[0][c])
            maxSoFar = max(maxSoFar, dp[0][c])


        for r in range(1, ROWS):
            for c in range(1, COLS):
                bit = int(matrix[r][c])
                if bit == 0:
                    continue

                dp[r][c] = 1 + min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1])
                maxSoFar = max(maxSoFar, dp[r][c])

        return maxSoFar**2
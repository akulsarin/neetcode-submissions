class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for r in range(N - 1, -1, -1):
            for c in range(r, -1, -1):
                dp[r][c] = triangle[r][c]
                dp[r][c] += min(dp[r + 1][c], dp[r + 1][c + 1])

        return dp[0][0]
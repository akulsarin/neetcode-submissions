class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        M = (N + 1) // 2

        suffixSums = piles[:]
        for i in range(N - 2, -1, -1):
            suffixSums[i] += suffixSums[i + 1]

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for m in range(1, M + 1):
            dp[N][m] = 0

        for i in range(N - 1, -1, -1):
            for m in range(M, 0, -1):
                pilesLeft = N - i
                maxTake = 2 * m
                
                if pilesLeft <= maxTake:
                    dp[i][m] = suffixSums[i]
                    continue
                
                for x in range(1, maxTake + 1):
                    nextI = min(i + x, N)
                    nextM = min(max(m, x), M)
                    dp[i][m] = max(dp[i][m], suffixSums[i] - dp[nextI][nextM])
        
        return dp[0][1]
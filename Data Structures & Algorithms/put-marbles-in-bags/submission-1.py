class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        
        dp = [[[0, 0] for _ in range(k + 1)]  for _ in range(N)]
        for remK in range(1, k + 1):
            dp[N - 1][remK][0] = float('inf')
            dp[N - 1][remK][1] = float('-inf')

        for i in range(N - 2, -1, -1):
            for remK in range(1, k + 1):
                if remK > N - i - 1:
                    dp[i][remK][0] = float('inf')
                    dp[i][remK][1] = float('-inf')
                    continue

                # Don't split here
                dp[i][remK][0] = dp[i + 1][remK][0]
                dp[i][remK][1] = dp[i + 1][remK][1]

                # Split here
                cost = weights[i] + weights[i + 1]
                dp[i][remK][0] = min(dp[i][remK][0], cost + dp[i + 1][remK - 1][0])
                dp[i][remK][1] = max(dp[i][remK][1], cost + dp[i + 1][remK - 1][1])

        return dp[0][k - 1][1] - dp[0][k - 1][0]
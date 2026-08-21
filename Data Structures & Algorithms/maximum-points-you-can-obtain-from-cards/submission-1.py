class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        # dp = [[[0] * (k + 1) for _ in range(N)] for _ in range(N)]

        # for l in range(N)

        dp = {}

        def dfs(l: int, r: int, remK: int) -> int:
            if remK == 0 or remK > r - l + 1:
                return 0

            if l == r:
                return cardPoints[l]

            if (l, r, remK) in dp:
                return dp[(l, r, remK)]

            takeL = cardPoints[l] + dfs(l + 1, r, remK - 1)
            takeR = cardPoints[r] + dfs(l ,r - 1, remK - 1)

            dp[(l, r, remK)] = max(takeL, takeR)
            return dp[(l, r, remK)]
        
        return dfs(0, N - 1, k)
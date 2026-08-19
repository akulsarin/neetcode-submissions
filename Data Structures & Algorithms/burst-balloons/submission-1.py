class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        paddedNums = [1] + nums + [1]
        N = len(paddedNums)
        dp = {}

        def dfs(l: int, r: int) -> int:
            if (l, r) in dp:
                return dp[(l, r)]
            if l > r:
                return 0

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = paddedNums[l - 1] * paddedNums[i] * paddedNums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        return dfs(1, N - 2)
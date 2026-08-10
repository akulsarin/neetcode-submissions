class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(l: int, r: int) -> int:
            if (l, r) in dp:
                return dp[(l, r)]

            if l == r:
                dp[(l, r)] = piles[l]
            else:
                dp[(l, r)] = max(piles[l] - dfs(l + 1, r), piles[r] - dfs(l, r - 1))

            return dp[(l, r)]

        return dfs(0, len(piles) - 1) >= 0
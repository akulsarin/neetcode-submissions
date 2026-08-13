class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        
        dp = [[float('inf')] * 3 for _ in range(N + 1)]
        dp[-1] = [0, 0, 0]

        for i in range(N - 1, -1, -1):
            for color in range(3):
                dp[i][color] = costs[i][color] + min([dp[i + 1][c] for c in range(3) if c != color])

        return min(dp[0])




        # def dfs(i: int, lastColor: int) -> int:
        #     if i == N:
        #         return 0
            
        #     res = float('inf')
        #     for color in range(3):
        #         if color != lastColor:
        #             res = min(res, costs[i][color] + dfs(i + 1, color))

        #     return res

        # return dfs(0, -1)
        
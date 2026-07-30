import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n)]

        for t in range(target + 1):
            if stones[0] <= t:
                dp[0][t] = stones[0]

        for i in range(1, n):
            for t in range(target + 1):
                # Exclude
                exclude = dp[i - 1][t]

                # Include
                include = 0
                if t - stones[i] >= 0:
                    include = stones[i] + dp[i - 1][t - stones[i]]
                
                dp[i][t] = max(exclude, include)

        return stoneSum - 2 * dp[-1][-1]







        


        
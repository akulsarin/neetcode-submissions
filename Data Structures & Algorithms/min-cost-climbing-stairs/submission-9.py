class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costPrev, costCurr = 0, 0
        for i in range(2, len(cost) + 1):
            costPrev, costCurr = costCurr, min(costPrev + cost[i - 2], costCurr + cost[i - 1])
        return costCurr
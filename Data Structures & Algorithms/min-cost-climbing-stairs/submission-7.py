class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costPrev, costCurr = 0, 0
        for i, c in enumerate(cost[2:], start=2):
            costPrev, costCurr = costCurr, min(costPrev + cost[i - 2], costCurr + cost[i - 1])
        return min(costPrev + cost[-2], costCurr + cost[-1])
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        numDays = len(prices)
        cache = {}

        def dfs(day: int, canBuy: bool) -> int:
            if day >= numDays:
                return 0

            if (day, canBuy) in cache:
                return cache[(day, canBuy)]

            if canBuy:
                buy = dfs(day + 1, False) - prices[day]
                cooldown = dfs(day + 1, True)
                cache[(day, canBuy)] = max(buy, cooldown)
                return max(buy, cooldown)
            else:
                sell = dfs(day + 2, True) + prices[day]
                cooldown = dfs(day + 1, False)
                cache[(day, canBuy)] = max(sell, cooldown)
                return max(sell, cooldown)

        return dfs(0, True)
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N == 1:
            return 0

        l, r = 0, 1
        maxProfit = 0
        while r < N:
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxProfit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        l, r = 0, 1
        currMax = 0
        while r < N:
            if prices[r] <= prices[l]:
                l = r
            else:
                currMax = max(prices[r] - prices[l], currMax)
            r += 1
        return currMax
            

        
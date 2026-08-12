class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        hold, noHold = prices[-1], 0
        for i in range(N - 2, -1, -1):
            maxHold = max(prices[i] + noHold, hold)
            maxNoHold = max(-prices[i] + hold, noHold)
            hold, noHold = maxHold, maxNoHold
        return noHold
        
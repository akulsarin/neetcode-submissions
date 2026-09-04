class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, no_hold = float('-inf'), 0
        for price in prices:
            hold = max(no_hold - price, hold)
            no_hold = max(hold + price, no_hold)
        return max(hold, no_hold)
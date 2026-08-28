class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prevHold, prevSell, prevCool = float('-inf'), float('-inf'), 0

        for price in prices:
            currHold = max(prevHold, -price + prevCool)
            currSell = price + prevHold
            currCool = max(prevCool, prevSell)
            prevHold, prevSell, prevCool = currHold, currSell, currCool
        
        return max(prevHold, prevSell, prevCool)
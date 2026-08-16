class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        currTotal = 0
        for i, numCust in enumerate(customers):
            if not grumpy[i]:
                currTotal += numCust
        
        currGain = 0
        l = r =0
        while r < minutes:
            if grumpy[r]:
                currGain += customers[r]
            r += 1
        
        maxGain = currGain
        for i in range(minutes, len(customers)):
            if grumpy[i]:
                currGain += customers[i]
            if grumpy[i - minutes]:
                currGain -= customers[i - minutes]
            maxGain = max(maxGain, currGain)
        
        return currTotal + maxGain
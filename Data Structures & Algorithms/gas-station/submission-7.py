class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        start_idx = 0
        remaining_gas = 0
        for i in range(len(gas)):
            remaining_gas += gas[i] - cost[i]
            if remaining_gas < 0:
                remaining_gas = 0
                start_idx = i + 1
        
        return start_idx
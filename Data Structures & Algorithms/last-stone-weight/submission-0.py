class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            largest = heapq.heappop_max(stones)
            second_largest = heapq.heappop_max(stones)
            if largest > second_largest:
                new_weight = largest - second_largest
                heapq.heappush_max(stones, new_weight)

        if stones:
            return stones[0]
        
        return 0

        
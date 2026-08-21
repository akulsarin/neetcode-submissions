class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        minHeap = []
        maxHeap = []
        
        for i in range(N - 1):
            cost = weights[i + 1] + weights[i]
            
            heapq.heappush(minHeap, cost)
            while len(minHeap) > k - 1:
                heapq.heappop(minHeap)

            heapq.heappush(maxHeap, -cost)
            while len(maxHeap) > k - 1:
                heapq.heappop(maxHeap)

        return sum(minHeap) + sum(maxHeap)
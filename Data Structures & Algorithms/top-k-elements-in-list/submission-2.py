class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        min_heap = []
        for num, count in counts.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [num for _, num in min_heap]
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(minHeap, [dist, x, y])

        result = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            result.append([x, y])

        return result


        
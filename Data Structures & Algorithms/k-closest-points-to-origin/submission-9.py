class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for i, point in enumerate(points):
            x, y = point
            dist = x**2 + y**2
            heapq.heappush(max_heap, (-dist, i))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        closest_points = []
        for _, i in max_heap:
            closest_points.append(points[i])
        
        return closest_points
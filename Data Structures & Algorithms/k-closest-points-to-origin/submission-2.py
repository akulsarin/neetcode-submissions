class Solution:
    def dist_to_origin(self, point: List[int]) -> float:
        return (point[0])**2 + (point[1])**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        for point in points:
            dist = self.dist_to_origin(point)
            if dist in distances:
                distances[dist].append(point)
            else:
                distances[dist] = [point]

        dist_list = list(distances.keys())
        heapq.heapify(dist_list)

        min_k = []
        added = 0
        while added < k:
            min_dist = heapq.heappop(dist_list)
            point = distances[min_dist].pop()
            if distances[min_dist]:
                heapq.heappush(dist_list, min_dist)
            min_k.append(point)
            added += 1

        return min_k

        
        
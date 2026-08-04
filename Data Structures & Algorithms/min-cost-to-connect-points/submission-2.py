class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)
        for i in range(N):
            for j in range(i, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visit = {0}
        cost = 0
        minHeap = []
        for dist, j in adj[0]:
            heapq.heappush(minHeap, (dist, 0, j))

        cost = 0
        while minHeap and len(visit) < N:
            dist, i, j = heapq.heappop(minHeap)
            if j in visit:
                continue
            visit.add(j)
            cost += dist
            for nextDist, k in adj[j]:
                heapq.heappush(minHeap, (nextDist, j, k))

        return cost
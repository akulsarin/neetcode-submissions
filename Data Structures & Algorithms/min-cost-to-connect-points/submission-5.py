class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                cost = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                adj[i].append((cost, j))
                adj[j].append((cost, i))

        min_heap = [(0, 0)]
        visited = [False] * n
        min_cost = 0
        while min_heap:
            cost, idx = heapq.heappop(min_heap)
            if visited[idx]:
                continue
            visited[idx] = True
            min_cost += cost
            for next_cost, next_idx in adj[idx]:
                if not visited[next_idx]:
                    heapq.heappush(min_heap, (next_cost, next_idx))

        return min_cost
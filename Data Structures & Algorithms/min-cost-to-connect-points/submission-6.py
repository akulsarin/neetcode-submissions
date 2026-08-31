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
        
        visit = set()
        min_heap = [(0, 0)]
        cost = 0

        while len(visit) < n:
            curr_cost, node_idx = heapq.heappop(min_heap)
            if node_idx in visit:
                continue
            visit.add(node_idx)
            cost += curr_cost

            for next_cost, neighbor in adj[node_idx]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, (next_cost, neighbor))

        return cost
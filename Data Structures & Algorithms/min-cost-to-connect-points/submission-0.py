class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        adj = {}
        for i in range(len(points)):
            neighbors = []
            pi = points[i]
            for j in range(len(points)):
                if j != i:
                    pj = tuple(points[j])
                    weight = dist(pi, pj)
                    neighbors.append([pj, weight])
            adj[tuple(pi)] = neighbors

        minHeap = []
        visit = set()
        startNode = tuple(points[0])
        for dstNode, weight in adj[startNode]:
            heapq.heappush(minHeap, [weight, startNode, dstNode])
        visit.add(startNode)

        result = 0
        while minHeap:
            weight, src, dst = heapq.heappop(minHeap)
            if dst in visit:
                continue

            result += weight
            visit.add(dst)
            for neighbor, weight in adj[dst]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, dst, neighbor])

        return result
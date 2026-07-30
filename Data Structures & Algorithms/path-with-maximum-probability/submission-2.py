class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}
        for i, edge in enumerate(edges):
            src, dst = edge[0], edge[1]
            adj[src].append((succProb[i], dst))
            adj[dst].append((succProb[i], src))

        maxHeap = [(-1, start_node)]
        longest = {}
        while maxHeap:
            p, u = heapq.heappop(maxHeap)
            if u in longest:
                continue
            
            if u == end_node:
                return -p

            longest[u] = p

            for dp, v in adj[u]:
                if v not in longest:
                    heapq.heappush(maxHeap, (p * dp, v))

        return 0


        
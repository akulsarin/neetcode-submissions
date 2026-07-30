class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the adjacency list: O(E) == O(V^2)
        adj = {i: [] for i in range(1, n + 1)}
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        minHeap = [(0, k)]
        shortest = {}
        currMax = 0
        while minHeap:
            t, v = heapq.heappop(minHeap)
            if v in shortest:
                continue
            shortest[v] = t
            currMax = max(currMax, t)

            for v2, dt in adj[v]:
                if v2 not in shortest:
                    heapq.heappush(minHeap, (t + dt, v2))

        if len(shortest) != n:
            return -1

        return currMax
            

        
        
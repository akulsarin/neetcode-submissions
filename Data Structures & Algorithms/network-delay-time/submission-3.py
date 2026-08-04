class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((ti, vi))
            if ui == k:
                heapq.heappush(minHeap, (ti, vi))

        timings = {k: 0}
        timeRequired = 0
        while minHeap and len(timings) < n:
            t, v = heapq.heappop(minHeap)
            if v in timings:
                continue
            timings[v] = t
            timeRequired = max(timeRequired, t)
            for t2, v2 in adj[v]:
                heapq.heappush(minHeap, (t + t2, v2))

        if len(timings) < n:
            return -1
        
        return timeRequired
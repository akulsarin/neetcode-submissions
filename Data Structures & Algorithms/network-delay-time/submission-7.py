class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((t, v))

        min_heap = [(0, k)]
        signal_times = {}
        min_time = 0

        while min_heap:
            t, n1 = heapq.heappop(min_heap)
            if n1 in signal_times:
                continue
            signal_times[n1] = t
            min_time = max(min_time, t)

            for dt, n2 in adj[n1]:
                heapq.heappush(min_heap, (t + dt, n2))
        
        return min_time if len(signal_times) == n else -1
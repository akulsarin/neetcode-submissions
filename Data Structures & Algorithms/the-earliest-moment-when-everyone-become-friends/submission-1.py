class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        adj = defaultdict(list)
        for time, x, y in logs:
            adj[x].append((time, y))
            adj[y].append((time, x))

        minHeap = []
        for time, friend in adj[0]:
            heapq.heappush(minHeap, (time, 0, friend))

        minTime = 0
        visited = {0}
        while minHeap and len(visited) < n:
            time, friend1, friend2 = heapq.heappop(minHeap)
            if friend2 in visited:
                continue

            visited.add(friend2)
            minTime = max(minTime, time)
            for nextTime, nextFriend in adj[friend2]:
                heapq.heappush(minHeap, (nextTime, friend2, nextFriend))
        
        return minTime if len(visited) == n else -1
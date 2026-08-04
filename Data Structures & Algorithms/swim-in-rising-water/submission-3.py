class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        N = len(grid)

        minTimes = {(0, 0): 0}
        minHeap = []
        for dr, dc in DIRS:
            if min(dr, dc) >= 0 and max(dr, dc) < N:
                time = max(grid[0][0], grid[dr][dc])
                heapq.heappush(minHeap, (time, dr, dc))

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in minTimes:
                continue

            if (r, c) == (N - 1, N - 1):
                return time

            minTimes[(r, c)] = time
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) >= 0 and max(r2, c2) < N:
                    neighborTime = max(time, grid[r2][c2])
                    heapq.heappush(minHeap, (neighborTime, r2, c2))

        return minTimes[(N - 1, N - 1)]
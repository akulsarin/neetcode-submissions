class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minHeap = [(grid[0][0], (0, 0))]
        shortest = {}

        while minHeap:
            maxEl, coords = heapq.heappop(minHeap)
            if coords in shortest:
                continue

            r, c = coords
            if min(r, c) == n - 1:
                return maxEl

            shortest[(r, c)] = maxEl
            for dr, dc in dirs:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) < 0 or max(r2, c2) == n or (r2, c2) in shortest:
                    continue

                dEl = max(maxEl, grid[r2][c2])
                heapq.heappush(minHeap, (dEl, (r2, c2)))

        return shortest[(n-1, n-1)]
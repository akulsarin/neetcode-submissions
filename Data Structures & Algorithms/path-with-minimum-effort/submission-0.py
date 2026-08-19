class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # minHeap stores (cost, r, c)
        minHeap = []
        heapq.heappush(minHeap, (0, 0, 0))
        visited = set()

        while minHeap:
            cost, r, c = heapq.heappop(minHeap)
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost

            if (r, c) in visited:
                continue
            visited.add((r, c))
            
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS:
                    continue
                nextCost = max(cost, abs(heights[r][c] - heights[r2][c2]))
                heapq.heappush(minHeap, (nextCost, r2, c2))
        
        return -1
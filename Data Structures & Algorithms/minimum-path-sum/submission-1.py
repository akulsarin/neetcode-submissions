class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        minHeap = [(0, 0, grid[0][0])]
        while minHeap:
            r, c, total = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return total
            if grid[r][c] == float('inf'):
                continue
            grid[r][c] = float('inf')

            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] == float('inf'):
                    continue
                heapq.heappush(minHeap, (r2, c2, total + grid[r2][c2]))

        return -1
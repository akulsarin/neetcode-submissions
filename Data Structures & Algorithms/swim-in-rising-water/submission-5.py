class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        min_heap = [(grid[0][0], 0, 0)]
        while min_heap:
            height, r, c = heapq.heappop(min_heap)
            if r == rows - 1 and c == cols - 1:
                return height
            if grid[r][c] == -1:
                continue
            grid[r][c] = -1
            for dr, dc in dirs:
                r2, c2 = r + dr, c + dc
                if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] != -1:
                    max_val = max(height, grid[r2][c2])
                    heapq.heappush(min_heap, (max_val, r2, c2))
        
        return -1
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        num_fresh = 0
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        time = 0
        while num_fresh > 0 and queue:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    r2, c2 = r + dr, c + dc
                    if 0 <= r2 < rows and 0 <= c2 < cols and grid[r2][c2] == 1:
                        queue.append((r2, c2))
                        grid[r2][c2] = 2
                        num_fresh -= 1
        
        return time if num_fresh == 0 else -1
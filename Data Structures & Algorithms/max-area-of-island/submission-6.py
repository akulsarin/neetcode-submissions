class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        ans = 0

        def bfs(r: int, c: int) -> int:
            queue = deque([(r, c)])
            count = 0
            grid[r][c] = 0

            while queue:
                curr = queue.popleft()
                count += 1
                for dr, dc in DIRS:
                    r2, c2 = curr[0] + dr, curr[1] + dc
                    if 0 <= r2 < ROWS and 0 <= c2 < COLS and grid[r2][c2]:
                        queue.append((r2, c2))
                        grid[r2][c2] = 0
            
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    ans = max(ans, bfs(r, c))
        
        return ans
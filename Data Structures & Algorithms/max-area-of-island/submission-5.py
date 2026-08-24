class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        ans = 0

        def bfs(r: int, c: int) -> None:
            nonlocal ans

            queue = deque([(r, c)])
            count = 0
            grid[r][c] = 0

            while queue:
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    count += 1
                    ans = max(ans, count)
                    for dr, dc in DIRS:
                        r2, c2 = curr[0] + dr, curr[1] + dc
                        if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] == 0:
                            continue
                        queue.append((r2, c2))
                        grid[r2][c2] = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    bfs(r, c)
        
        return ans
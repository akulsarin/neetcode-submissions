class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([])
        visited = set()
        level = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        while queue:
            level += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] <= 0 or (r2, c2) in visited:
                        continue
                    grid[r2][c2] = level
                    queue.append((r2, c2))
                    visited.add((r2, c2))
        
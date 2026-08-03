class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r1: int, c1: int):
            if grid[r1][c1] != 0:
                return

            queue = deque([(r1, c1)])
            visited = {(r1, c1)}
            level = 0

            while queue:
                level += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in DIRS:
                        r2, c2 = r + dr, c + dc
                        if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] <= 0 or (r2, c2) in visited:
                            continue
                        grid[r2][c2] = min(grid[r2][c2], level)
                        queue.append((r2, c2))
                        visited.add((r2, c2))

        for r in range(ROWS):
            for c in range(COLS):
                bfs(r, c)

        
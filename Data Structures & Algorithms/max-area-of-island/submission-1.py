class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        currMax = 0

        def bfs(r: int, c: int) -> int:
            if (r, c) in visited or grid[r][c] == 0:
                return 0

            queue = deque([(r, c)])
            visited.add((r, c))
            count = 1
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in DIRS:
                        r2, c2 = r + dr, c + dc
                        if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or (r2, c2) in visited or grid[r2][c2] == 0:
                            continue
                        queue.append((r2, c2))
                        visited.add((r2, c2))
                        count += 1
            return count

        for r in range(ROWS):
            for c in range(COLS):
                currMax = max(currMax, bfs(r, c))

        return currMax
                    


        
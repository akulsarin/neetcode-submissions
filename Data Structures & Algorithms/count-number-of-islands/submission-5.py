class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set()

        def bfs(r: int, c: int) -> bool:
            if (r, c) in visit or grid[r][c] == "0":
                return False

            queue = deque([(r, c)])
            visit.add((r, c))
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in DIRS:
                        row2, col2 = row + dr, col + dc
                        if min(row2, col2) < 0 or row2 == ROWS or col2 == COLS or grid[row2][col2] == "0" or (row2, col2) in visit:
                            continue
                        queue.append((row2, col2))
                        visit.add((row2, col2))

            return True

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if bfs(r, c):
                    count += 1
        return count

                        






        
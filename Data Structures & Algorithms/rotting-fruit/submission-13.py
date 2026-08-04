class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque([])
        visited = set()
        numFreshFruits = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFreshFruits += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))

        mins = -1
        while queue:
            mins += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or (r2, c2) in visited or grid[r2][c2] != 1:
                        continue
                    numFreshFruits -= 1
                    queue.append((r2, c2))
                    visited.add((r2, c2))
        
        return -1 if numFreshFruits > 0 else max(0, mins)

                    

        
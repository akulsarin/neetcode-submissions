class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque([])
        bridgeQueue = deque([])
        for r in range(ROWS):
            if len(queue) > 0:
                break
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 2
                    bridgeQueue.append((r, c))
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] != 1:
                        continue
                    queue.append((r2, c2))
                    grid[r2][c2] = 2
                    bridgeQueue.append((r2, c2))
        level = 0
        while bridgeQueue:
            for _ in range(len(bridgeQueue)):
                r, c = bridgeQueue.popleft()
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] == 2:
                        continue
                    if grid[r2][c2] == 1:
                        return level
                    bridgeQueue.append((r2, c2))
                    grid[r2][c2] = 2
            level += 1
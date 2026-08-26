class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r, c))

        distance = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    r2, c2 = r + dr, c + dc
                    if 0 <= r2 < m and 0 <= c2 < n and grid[r2][c2] > distance:
                        queue.append((r2, c2))
                        grid[r2][c2] = distance
            distance += 1
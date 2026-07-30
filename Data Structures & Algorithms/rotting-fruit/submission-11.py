from collections import deque

class Solution:
    def isValidLoc(self, r: int, c: int, m: int, n: int) -> bool:
        return min(r, c) >= 0 and r < m and c < n

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        queue = deque()
        visited = set()
        num_fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1

        mins = -1
        while queue:
            layer_count = len(queue)
            for _ in range(layer_count):
                r, c = queue.popleft()

                if grid[r][c] == 1:
                    grid[r][c] = 2
                    num_fresh -= 1

                for dr, dc in directions:
                    tr, tc = r + dr, c + dc
                    if (tr, tc) in visited or not self.isValidLoc(tr, tc, m, n) or grid[tr][tc] != 1:
                        continue
                    queue.append((tr, tc))
                    visited.add((tr, tc))

            mins += 1

        if num_fresh:
            return -1
        
        return max(0, mins)

                

        
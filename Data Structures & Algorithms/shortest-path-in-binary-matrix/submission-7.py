from collections import deque

class Solution:
    def isValidLoc(self, r: int, c: int, grid_size: int) -> bool:
        return min(r, c) >= 0 and max(r, c) < grid_size

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        queue = deque()
        visited = set()
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        queue.append((0, 0))
        visited.add((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == n - 1 and c == n - 1:
                    return length + 1

                for dr, dc in directions:
                    tr, tc = r + dr, c + dc
                    if (tr, tc) in visited or not self.isValidLoc(tr, tc, n) or grid[tr][tc] == 1:
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r, c))

            length += 1

        return -1
                



        
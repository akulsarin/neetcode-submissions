from collections import deque

class Solution:
    def isValidLoc(self, r: int, c: int, grid_size: int) -> bool:
        return min(r, c) >= 0 and max(r, c) < grid_size

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visited = set()
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        queue.append((0, 0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if (r, c) in visited or not self.isValidLoc(r, c, n) or grid[r][c] == 1:
                    continue

                if r == n - 1 and c == n - 1:
                    return length + 1

                for dr, dc in directions:
                    tr, tc = r + dr, c + dc
                    queue.append((r + dr, c + dc))
                    visited.add((r, c))

            length += 1

        return -1
                



        
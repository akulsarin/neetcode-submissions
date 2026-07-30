class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        num_rows, num_cols = len(grid), len(grid[0])
        curr_max = 0

        def is_valid_loc(r: int, c: int):
            return r >= 0 and c >= 0 and r < num_rows and c < num_cols

        def dfs(r: int, c: int, curr_size: int = 0) -> int:
            if not is_valid_loc(r, c) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            curr_size += 1
            for dr, dc in directions:
                curr_size += dfs(r + dr, c + dc)

            return curr_size

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    curr_max = max(curr_max, dfs(r, c))

        return curr_max

            

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        count = 0
        visited = set()

        def is_valid_loc(r: int, c: int)-> bool: 
            return r >= 0 and r < num_rows and c >= 0 and c < num_cols

        def dfs_on_land(r: int, c: int):
            # Check boundaries
            if not is_valid_loc(r, c):
                return

            # Check visited
            if (r, c) in visited:
                return False

            # Check for water
            if grid[r][c] == "0":
                return

            # Add to visited
            visited.add((r, c))

            dfs_on_land(r - 1, c)
            dfs_on_land(r + 1, c)
            dfs_on_land(r, c - 1)
            dfs_on_land(r, c + 1)

        for r in range(num_rows):
            for c in range(num_cols):
                # Check visited
                if (r, c) in visited:
                    continue

                # Check for land
                if grid[r][c] != "0":
                    count += 1
                    dfs_on_land(r, c)

        return count
                




        
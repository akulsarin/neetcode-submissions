class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        num_rows, num_cols = len(image), len(image[0])
        visited = set()

        def dfs(r: int, c: int) -> None:
            # Check for bounds
            if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                return

            # Check if visited
            # if (r, c) in visited:
            #     return

            # Check for color:
            if image[r][c] != original_color:
                return

            # Mark as visited
            # visited.add((r, c))

            # Modify the color in-place
            image[r][c] = color

            # Recurse
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        dfs(sr, sc)
        return image
        
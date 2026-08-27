class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(start_queue: List[List[int]]) -> set[Tuple[int]]:
            queue = deque(start_queue)
            visit = set(start_queue)
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    r2, c2 = r + dr, c + dc
                    if 0 <= r2 < rows and 0 <= c2 < cols and (r2, c2) not in visit and heights[r2][c2] >= heights[r][c]: 
                        queue.append((r2, c2))
                        visit.add((r2, c2))
            return visit

        atlantic_edges = []
        pacific_edges = []
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific_edges.append((r, c))
                if r == rows - 1 or c == cols - 1:
                    atlantic_edges.append((r, c))

        atlantic_flows = bfs(atlantic_edges)
        pacific_flows = bfs(pacific_edges)

        return list(atlantic_flows & pacific_flows)
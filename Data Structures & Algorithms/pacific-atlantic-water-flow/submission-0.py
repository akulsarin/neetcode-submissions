class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(waterAdjacent: List[Tuple[int]]) -> set:
            queue = deque([])
            visited = set()
            for cell in waterAdjacent:
                queue.append(cell)
                visited.add(cell)
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in DIRS:
                        r2, c2 = r + dr, c + dc
                        if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or (r2, c2) in visited:
                            continue
                        if heights[r2][c2] < heights[r][c]:
                            continue
                        queue.append((r2, c2))
                        visited.add((r2, c2))
            
            return visited

        pacificAdjacent = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(1, ROWS)]
        atlanticAdjacent = [(ROWS - 1, c) for c in range(COLS)] + [(r, COLS - 1) for r in range(ROWS - 1)]

        flowToPacific = bfs(pacificAdjacent)
        flowToAtlantic = bfs(atlanticAdjacent)
        combined = flowToPacific & flowToAtlantic
        print(combined)
        return [list(tup) for tup in combined]

        
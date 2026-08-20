class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # For each land cell, maps (i, j) -> (numReached, totalDist)
        distances = {}

        # For each building cell, maps (i, j) -> {cellsVisited}
        visit = defaultdict(set)

        # Multi-Source BFS Queue
        queue = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c, r, c))
                    visit[(r, c)].add((r, c))
                elif grid[r][c] == 0:
                    distances[(r, c)] = [0, 0]
        numBuildings = len(queue)

        dist = 0
        while queue:
            for _ in range(len(queue)):
                sr, sc, r, c = queue.popleft()
                if grid[r][c] == 0:
                    distances[(r, c)][0] += 1
                    distances[(r, c)][1] += dist
                
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == ROWS or c2 == COLS or grid[r2][c2] != 0:
                        continue
                    if (r2, c2) in visit[(sr, sc)]:
                        continue
                    visit[(sr, sc)].add((r2, c2))
                    queue.append((sr, sc, r2, c2))
            dist += 1
        print([distances])

        valid_distances = [dist for numReached, dist in distances.values() if numReached == numBuildings]
        return min(valid_distances) if valid_distances else -1
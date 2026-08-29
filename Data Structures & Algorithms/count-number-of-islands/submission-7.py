class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, i: int) -> int:
        p = i
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, i1: int, i2: int) -> bool:
        p1, p2 = self.find(i1), self.find(i2)
        if p1 == p2:
            return False
        
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p2] += 1
        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num_islands += 1
                    grid[r][c] = str(num_islands)
        
        uf = UnionFind(num_islands)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    continue
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if 0 <= r2 < ROWS and 0 <= c2 < COLS and grid[r2][c2] != "0":
                        if uf.union(int(grid[r][c]), int(grid[r2][c2])):
                            num_islands -= 1
        
        return num_islands
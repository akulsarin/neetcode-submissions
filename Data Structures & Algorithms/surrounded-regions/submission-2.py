class UnionFind:
    def __init__(self, rows: int, cols: int):
        self.par = {}
        self.rank = {}
        self.edge_connected = {}

        for r in range(rows):
            for c in range(cols):
                self.par[(r, c)] = (r, c)
                self.rank[(r, c)] = (r, c)
                is_edge_cell = r in {0, rows - 1} or c in (0, cols - 1)
                self.edge_connected[(r, c)] = is_edge_cell

    def find(self, r: int, c: int) -> Tuple[int, int]:
        p = (r, c)
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, coord_1: Tuple[int, int], coord_2: Tuple[int, int]) -> bool:
        r1, c1 = coord_1
        r2, c2 = coord_2
        p1, p2 = self.find(r1, c1), self.find(r2, c2)
        if p1 == p2:
            return False
        
        if self.edge_connected[p1] or self.edge_connected[p2]:
            self.edge_connected[p1] = self.edge_connected[p2] = True
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        
        return True


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        uf = UnionFind(rows, cols)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    continue
                for dr, dc in dirs:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == rows or c2 == cols or board[r2][c2] == "X":
                        continue
                    uf.union((r, c), (r2, c2))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    p = uf.find(r, c)
                    if not uf.edge_connected[p]:
                        board[r][c] = "X"
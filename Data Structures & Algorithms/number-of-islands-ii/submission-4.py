class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.connectedComponents = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n: int) -> int:
        p = n
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        uf = UnionFind(len(positions))
        positionsAdded = {}
        res = [0]

        for i, pos in enumerate(positions):
            r, c = pos
            if (r, c) in positionsAdded:
                res.append(res[-1])
                continue
            positionsAdded[(r, c)] = i
            numIslands = res[-1] + 1
            for dr, dc in DIRS:
                r2, c2 = r + dr, c + dc
                if min(r2, c2) < 0 or r2 == m or c2 == n or (r2, c2) not in positionsAdded:
                    continue
                j = positionsAdded[(r2, c2)]
                if uf.union(i, j):
                    numIslands -= 1
            res.append(numIslands)
        
        return res[1:]
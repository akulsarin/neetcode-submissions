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
            self.rank[p1] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))

        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        
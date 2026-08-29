class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1

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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        num_edges = len(edges)
        if num_edges != n - 1:
            return False
        
        uf = UnionFind(n)
        connected_components = n
        for u, v in edges:
            if uf.union(u, v):
                connected_components -= 1
        
        return connected_components == 1
class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, k: int) -> int:
        p = self.par[k]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, k1: int, k2: int) -> bool:
        p1, p2 = self.find(k1), self.find(k2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = UnionFind(n)
        for k1, k2 in edges:
            graph.union(k1, k2)

        anchors = set()
        for i in range(n):
            anchor = graph.find(i)
            if anchor not in anchors:
                anchors.add(anchor)

        return len(anchors)
        
class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = {}
        self.rank = {}
        self.counts = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0
            self.counts[i] = 1

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
            self.counts[p1] += self.counts[p2]
            # del self.counts[p2]
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.counts[p2] += self.counts[p1]
            # del self.counts[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
            self.counts[p1] += self.counts[p2]
            # del self.counts[p2]

        # print(self.counts)

        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        graph = UnionFind(len(nums))
        numToIdx = {}
        nums = list(set(nums))

        for idx, num in enumerate(nums):
            numToIdx[num] = idx

        for idx, num in enumerate(nums):
            if num - 1 in numToIdx:
                newIdx = numToIdx[num - 1]
                graph.union(idx, newIdx)

        return max(graph.counts.values())



            
        
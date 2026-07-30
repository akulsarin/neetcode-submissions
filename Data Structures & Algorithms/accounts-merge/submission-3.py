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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = UnionFind(len(accounts))
        emailToId = {}
        for i, account in enumerate(accounts):
            curIdx = i
            for email in account[1:]:
                if email in emailToId:
                    curIdx = emailToId[email]
                    graph.union(i, curIdx)
                else:
                    emailToId[email] = curIdx

        idToEmails = defaultdict(set)
        for i in range(len(accounts)):
            p = graph.find(i)
            idToEmails[p].update(accounts[i][1:])

        result = []
        for idx, emailSet in idToEmails.items():
            name = accounts[idx][0]
            emails = sorted(list(emailSet))
            result.append([name, *emails])

        return result



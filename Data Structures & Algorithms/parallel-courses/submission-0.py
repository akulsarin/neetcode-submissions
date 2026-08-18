class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj = defaultdict(list)
        inDegrees = [0] * (n + 1)
        for prevCrs, nextCrs in relations:
            adj[prevCrs].append(nextCrs)
            inDegrees[nextCrs] += 1
        
        queue = deque([crs for crs, cnt in enumerate(inDegrees) if cnt == 0])
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                crs = queue.popleft()
                for nextCrs in adj[crs]:
                    inDegrees[nextCrs] -= 1
                    if inDegrees[nextCrs] == 0:
                        queue.append(nextCrs)
        
        if max(inDegrees) > 0:
            print(inDegrees)
            return -1
        
        return ans
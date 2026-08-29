class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for succ, prereq in prerequisites:
            adj[succ].append(prereq)

        visit = set()
        def dfs(crs: int, path: set) -> bool:
            if crs in path:
                return False
            if crs in visit:
                return True

            visit.add(crs)
            path.add(crs)
            for prereq in adj[crs]:
                if not dfs(prereq, path):
                    return False
            path.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs, set()):
                return False
        
        return True
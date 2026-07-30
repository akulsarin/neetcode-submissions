class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for curr, pre in prerequisites:
            adj[curr].append(pre)

        path = set()
        visit = set()
        result = []

        def dfs(i: int) -> bool:
            if i in path:
                return False
            
            if i in visit:
                return True

            visit.add(i)
            path.add(i)

            for neighbor in adj[i]:
                if not dfs(neighbor):
                    return False
            
            path.remove(i)
            result.append(i)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return result



        
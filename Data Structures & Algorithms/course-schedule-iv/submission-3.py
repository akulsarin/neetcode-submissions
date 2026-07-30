class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: set() for i in range(numCourses)}
        for prereq, succ in prerequisites:
            adj[succ].add(prereq)

        visit = set()
        prereqs = {i: set() for i in range(numCourses)}

        def dfs(curr: int):
            if curr in visit:
                return

            visit.add(curr)

            for prereq in adj[curr]:
                prereqs[curr].add(prereq)
                dfs(prereq)
                prereqs[curr] |= prereqs[prereq]

        for i in range(numCourses):
            dfs(i)

        result = []
        for uj, vj in queries:
            if uj in prereqs[vj]:
                result.append(True)
            else:
                result.append(False)
        
        return result



            

            
        
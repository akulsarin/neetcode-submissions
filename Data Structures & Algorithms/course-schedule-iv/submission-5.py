class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for prereq, succ in prerequisites:
            adj[succ].append(prereq)

        prereqs = [set() for i in range(numCourses)]

        def dfs(curr: int):
            if prereqs[curr]:
                return

            prereqs[curr].add(curr)

            for prereq in adj[curr]:
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



            

            
        
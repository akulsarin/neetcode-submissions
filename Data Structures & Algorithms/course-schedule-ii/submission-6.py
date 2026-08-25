class Solution:
    def dfs(self, src: int, adj: List[List[int]], visit: set[int], path: set[int], order: List[int]) -> bool:
        if src in path:
            return False
        if src in visit:
            return True
        
        path.add(src)
        visit.add(src)

        for nxt in adj[src]:
            if not self.dfs(nxt, adj, visit, path, order):
                return False
        order.append(src)
        path.remove(src)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for succ, prereq in prerequisites:
            adj[succ].append(prereq)

        visit = set()
        course_order = []
        for i in range(numCourses):
            path = set()
            if not self.dfs(i, adj, visit, path, course_order):
                return []
        return course_order
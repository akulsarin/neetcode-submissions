class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses
        for succ, prereq in prerequisites:
            adj[prereq].append(succ)
            in_degrees[succ] += 1

        course_order = []
        q = deque([c for c in range(numCourses) if in_degrees[c] == 0])

        while q:
            for _ in range(len(q)):
                c = q.popleft()
                course_order.append(c)
                for nxt in adj[c]:
                    in_degrees[nxt] -= 1
                    if in_degrees[nxt] == 0:
                        q.append(nxt)

        if len(course_order) != numCourses:
            return []
        
        return course_order
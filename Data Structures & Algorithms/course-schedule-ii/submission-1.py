class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        inDegree = [0] * numCourses
        for succ, prereq in prerequisites:
            adj[prereq].append(succ)
            inDegree[succ] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        courseOrder = []
        
        while queue:
            currCourse = queue.popleft()
            courseOrder.append(currCourse)
            for succ in adj[currCourse]:
                inDegree[succ] -= 1
                if inDegree[succ] == 0:
                    queue.append(succ)

        if len(courseOrder) == numCourses:
            return courseOrder
        
        return []
        
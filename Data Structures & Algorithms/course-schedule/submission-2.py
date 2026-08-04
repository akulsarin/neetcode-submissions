class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        inDegree = [0] * numCourses
        for succ, prereq in prerequisites:
            adj[prereq].append(succ)
            inDegree[succ] += 1

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])

        coursesTaken = 0
        while queue:
            curr = queue.popleft()
            coursesTaken += 1
            for succ in adj[curr]:
                inDegree[succ] -= 1
                if inDegree[succ] == 0:
                    queue.append(succ)
        
        return coursesTaken == numCourses




        
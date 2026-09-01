class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        in_degrees = defaultdict(int)
        for prereq, crs in prerequisites:
            adj[prereq].append(crs)
            in_degrees[crs] += 1

        prereq_map = defaultdict(set)
        queue = deque([i for i in range(numCourses) if in_degrees[i] == 0])
        while queue:
            crs = queue.popleft()
            for next_crs in adj[crs]:
                in_degrees[next_crs] -= 1
                prereq_map[next_crs].update(prereq_map[crs])
                prereq_map[next_crs].add(crs)
                if in_degrees[next_crs] == 0:
                    queue.append(next_crs)

        output = []
        for u, v in queries:
            if u in prereq_map[v]:
                output.append(True)
            else:
                output.append(False)
        return output
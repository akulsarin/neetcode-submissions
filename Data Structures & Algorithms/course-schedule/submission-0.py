class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create graph as adjacency list
        adjList = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        # Initialize DFS traversal
        visited = set()

        def canFinishCourse(course: int) -> bool:
            if course in visited:
                return False

            prereqs = adjList[course]
            if len(prereqs) == 0:
                return True

            visited.add(course)

            for prereq in prereqs:
                if not canFinishCourse(prereq):
                    return False

            visited.remove(course)
            adjList[course] = []
            return True

        for course in range(numCourses):
            if not canFinishCourse(course):
                return False

        return True

        
        
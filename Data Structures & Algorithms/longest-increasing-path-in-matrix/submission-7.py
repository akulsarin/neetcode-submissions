class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        indegrees = {}
        for r in range(M):
            for c in range(N):
                indegrees[(r, c)] = 0
                for dr, dc in DIRS:
                    r2, c2 = r + dr, c + dc
                    if min(r2, c2) < 0 or r2 == M or c2 == N:
                        continue
                    if matrix[r2][c2] < matrix[r][c]:
                        indegrees[(r, c)] += 1
        
        queue = deque([(r, c) for (r, c) in indegrees if indegrees[(r, c)] == 0])
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc, in DIRS:
                    r2, c2 = r + dr, c + dc
                    if (r2, c2) in indegrees and matrix[r][c] < matrix[r2][c2]:
                        indegrees[(r2, c2)] -= 1
                        if indegrees[(r2, c2)] == 0:
                            queue.append((r2, c2))

        return count
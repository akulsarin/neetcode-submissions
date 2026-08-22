class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        prev = points[0]
        
        for r in range(1, ROWS):
            curr = prev.copy()
            for c in range(1, COLS):
                curr[c] = max(curr[c], curr[c - 1] - 1)
            for c in range(COLS - 2, -1, -1):
                curr[c] = max(curr[c], curr[c + 1] - 1)
            for c in range(COLS):
                curr[c] += points[r][c]
            prev = curr
        
        return max(prev)
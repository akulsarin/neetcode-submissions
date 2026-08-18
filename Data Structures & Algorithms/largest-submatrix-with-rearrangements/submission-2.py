class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        ans = 0
        heights = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                currHeight = 0 if matrix[r][c] == 0 else heights[c] + 1
                heights[c] = currHeight
            sorted_heights = sorted(heights, reverse=True)
            for i in range(COLS):
                area = sorted_heights[i] * (i + 1)
                ans = max(ans, area)

        return ans
class Solution:
    def calcArea(self, heights: List[int]) -> int:
        N = len(heights)
        stack = []
        maxArea = 0

        for i, height in enumerate(heights):
            tmpIdx, tmpHeight = i, height
            while stack and height <= stack[-1][1]:
                tmpIdx, tmpHeight = stack.pop()
                area = (i - tmpIdx) * tmpHeight
                maxArea = max(maxArea, area)
            stack.append((tmpIdx, height))

        for idx, height in stack:
            area = (N - idx) * height
            maxArea = max(maxArea, area)

        return maxArea

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        ans = 0
        heights = [0] * COLS
        for r in range(ROWS):
            for c in range(COLS):
                currHeight = 0 if matrix[r][c] == 0 else heights[c] + 1
                heights[c] = currHeight
            ans = max(ans, self.calcArea(sorted(heights, reverse=True)))
        return ans
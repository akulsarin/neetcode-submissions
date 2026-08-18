class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
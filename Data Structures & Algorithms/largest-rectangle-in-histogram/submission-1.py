class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        stack = []

        maxArea = 0
        for i, height in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((i, height))
                continue

            newIdx = i
            while stack and height <= stack[-1][1]:
                prevIdx, prevHeight = stack.pop()
                prevArea = (i - prevIdx) * prevHeight
                maxArea = max(maxArea, prevArea)
                newIdx = prevIdx

            stack.append((newIdx, height))

        for idx, height in stack:
            area = (N - idx) * height
            maxArea = max(maxArea, area)

        return maxArea



        
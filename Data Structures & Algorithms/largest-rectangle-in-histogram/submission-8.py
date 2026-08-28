class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_area = 0
        
        for i, height in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((i, height))
                continue
            
            farthest_idx = i
            while stack and height <= stack[-1][1]:
                farthest_idx, last_height = stack.pop()
                area = last_height * (i - farthest_idx)
                largest_area = max(largest_area, area)
            
            stack.append((farthest_idx, height))

        stack_len = len(heights)
        for i, height in stack:
            area = height * (stack_len - i)
            largest_area = max(largest_area, area)

        return largest_area
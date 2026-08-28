class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        largest_area = 0
        
        for i, height in enumerate(heights):           
            farthest_idx = i
            while stack and height <= stack[-1][1]:
                farthest_idx, last_height = stack.pop()
                area = last_height * (i - farthest_idx)
                largest_area = max(largest_area, area)
            
            stack.append((farthest_idx, height))

        for i, height in stack:
            area = height * (n - i)
            largest_area = max(largest_area, area)

        return largest_area
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1

        while l <= r:
            mid_idx = (l + r) // 2
            mid_row = mid_idx // n
            mid_col = mid_idx % n
            mid_el = matrix[mid_row][mid_col]

            if target > mid_el:
                l = mid_idx + 1
            elif target < mid_el:
                r = mid_idx - 1
            else:
                return True
        
        return False
        
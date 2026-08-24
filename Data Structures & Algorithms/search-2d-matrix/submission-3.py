class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            mid = (l + r) // 2
            midRow = mid // COLS
            midCol = mid % COLS
            midNum = matrix[midRow][midCol]
            
            if midNum > target:
                r = mid - 1
            elif midNum < target:
                l = mid + 1
            else:
                return True

        return False
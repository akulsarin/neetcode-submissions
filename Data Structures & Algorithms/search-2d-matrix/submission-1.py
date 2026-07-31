class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        l, r = 0, (M * N) - 1

        while l <= r:
            print(l, r)
            midIdx = (l + r) // 2
            row, col = midIdx // N, midIdx % N
            midEl = matrix[row][col]

            if target == midEl:
                return True
            elif target > midEl:
                l = midIdx + 1
            else:
                r = midIdx - 1

        return False

        
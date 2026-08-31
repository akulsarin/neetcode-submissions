class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix = [[0] * self.cols for _ in range(self.rows)]

        total = 0
        for r in range(self.rows):
            total += matrix[r][0]
            self.prefix[r][0] = total

        total = 0
        for c in range(self.cols):
            total += matrix[0][c]
            self.prefix[0][c] = total

        for r in range(1, self.rows):
            for c in range(1, self.cols):
                self.prefix[r][c] = matrix[r][c] + self.prefix[r - 1][c] + self.prefix[r][c - 1] - self.prefix[r - 1][c - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix_bottom_right = self.prefix[row2][col2]
        prefix_top_right = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        prefix_bottom_left = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        prefix_top_left = self.prefix[row1 - 1][col1 - 1] if min(row1, col1) > 0 else 0
        return prefix_bottom_right - prefix_top_right - prefix_bottom_left + prefix_top_left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
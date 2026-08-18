class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)

        res = []
        while l < r and t < b:
            # left-top to right-top
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            
            # top-right to bottom-right
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            if l >= r or t >= b:
                break

            # bottom-right to bottom-left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1

            # left-bottom to left-top
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res
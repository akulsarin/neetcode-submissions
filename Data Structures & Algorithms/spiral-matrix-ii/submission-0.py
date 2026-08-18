class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        l = t = 0
        r = b = n
        ctr = 1

        while l < r and t < b:
            # top-left to top-right
            for i in range(l, r):
                res[t][i] = ctr
                ctr += 1
            t += 1
            
            # left-top to left-bottom
            for i in range(t, b):
                res[i][r - 1] = ctr
                ctr += 1
            r -= 1

            if l >= r or t >= b:
                break

            # bottom-right to bottom-left
            for i in range(r - 1, l - 1, -1):
                res[b - 1][i] = ctr
                ctr += 1
            b -= 1 

            # left-bottom to left-top
            for i in range(b - 1, t - 1, -1):
                res[i][l] = ctr
                ctr += 1
            l += 1
            
        return res
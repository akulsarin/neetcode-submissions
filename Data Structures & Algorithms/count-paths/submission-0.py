class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1
            for c in range(n - 2, -1, -1):
                currRow[c] = currRow[c + 1] + prevRow[c]
            prevRow = currRow

        return prevRow[0]

        
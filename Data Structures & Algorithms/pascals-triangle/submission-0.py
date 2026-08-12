class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(2, numRows + 1):
            curr = [1] * i
            for j in range(1, i - 1):
                curr[j] = dp[-1][j - 1] + dp[-1][j]
            dp.append(curr)
        return dp

        
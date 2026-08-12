class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for i in range(2, rowIndex + 2):
            curr = [1] * i
            for j in range(1, i - 1):
                curr[j] = dp[j - 1] + dp[j]
            dp = curr
        return dp
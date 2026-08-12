class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = [0] * (n + 1)
        prefix[-2] = nums[-1]
        for i in range(n - 2, -1, -1):
            prefix[i] = prefix[i + 1] + nums[i]
        
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0

        for j in range(1, k + 1):
            for i in range(n - j, -1, -1):
                startIdx = n - j + 1
                endIdx = i
                for m in range(startIdx, endIdx, -1):
                    prevMax = dp[m][j - 1]
                    currSum = prefix[i] - prefix[m]
                    dp[i][j] = min(dp[i][j], max(prevMax, currSum))

        return dp[0][k]        
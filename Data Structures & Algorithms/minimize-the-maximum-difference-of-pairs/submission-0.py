class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [[float('inf')] * (p + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n - 2, -1, -1):
            for j in range(1, p + 1):
                skip = dp[i + 1][j]
                take = max(abs(nums[i] - nums[i + 1]), dp[i + 2][j - 1])
                dp[i][j] = min(take, skip)
        
        return dp[0][p]
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2

        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            for target in range(half, num - 1, -1):
                dp[target] = dp[target] or dp[target - num]
        
        return dp[half]
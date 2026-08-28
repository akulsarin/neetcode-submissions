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
            dp_next = [False] * (half + 1)
            dp_next[0] = True
            for target in range(half + 1):
                dp_next[target] = dp[target]
                if target - num >= 0:
                    dp_next[target] = dp_next[target] or dp[target - num]
            dp = dp_next
        
        return dp[half]
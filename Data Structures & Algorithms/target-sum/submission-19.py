class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        max_sum = sum(nums)
        if abs(target) > max_sum:
            return 0
        
        M = len(nums)
        N = 2 * max_sum

        dp = [0] * (N + 1)
        dp[max_sum] = 1

        for i in range(M):
            curr = [0] * (N + 1)
            for t in range(-max_sum, max_sum + 1):
                j = t + max_sum
                num = nums[i]

                if j - num >= 0:
                    curr[j] += dp[j - num]
                if j + num <= N:
                    curr[j] += dp[j + num]
            dp = curr
        
        return dp[target + max_sum]
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        dp = [[0] * (target + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for t in range(1, target + 1):
            for i in range(1, N + 1):
                # Exclude current num
                dp[i][t] += dp[i - 1][t]

                # Include current num
                num = nums[i - 1]
                if t - num >= 0:
                    dp[i][t] += dp[N][t - num]
        
        return dp[N][target]
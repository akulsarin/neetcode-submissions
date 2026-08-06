class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        M = len(nums)
        N = sum(nums)
        if abs(target) > N:
            return 0

        dp = [[0] * (N + N + 1) for _ in range(M)]

        dp[0][nums[0] + N] += 1
        dp[0][-nums[0] + N] += 1

        for i in range(1, M):
            for t in range(-N, N + 1):
                j = t + N
                num = nums[i]

                if t - num >= -N:
                    dp[i][j] += dp[i - 1][t - num + N]
                
                if t + num <= N:
                    dp[i][j] += dp[i - 1][t + num + N]

        return dp[M - 1][target + N]
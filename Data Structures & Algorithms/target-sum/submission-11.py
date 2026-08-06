class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        M = len(nums)
        N = sum(nums)
        if abs(target) > N:
            return 0

        dp = [[0] * (N + N + 1) for _ in range(M)]
        targetToIdx = {t : t + N for t in range(-N, N + 1)}

        dp[0][targetToIdx[nums[0]]] += 1
        dp[0][targetToIdx[-nums[0]]] += 1

        for i in range(1, M):
            for t in range(-N, N + 1):
                j = targetToIdx[t]
                num = nums[i]

                # If we add, we must use dp[i - 1][t - currNum]
                if t - num >= -N:
                    diffIdx = targetToIdx[t - num]
                    dp[i][j] += dp[i - 1][diffIdx]
                
                # If we subtract, we must use dp[i - 1][t + currNum]
                if t + num <= N:
                    sumIdx = targetToIdx[t + num]
                    dp[i][j] += dp[i - 1][sumIdx]
        # print(dp)
        return dp[M - 1][targetToIdx[target]]
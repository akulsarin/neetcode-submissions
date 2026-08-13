class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        
        dp = [1] * N

        total = 1
        for i in range(N - 2, -1, -1):
            print(dp)
            if nums[i] < nums[i + 1]:
                dp[i] += dp[i + 1]
            total += dp[i]

        return total        
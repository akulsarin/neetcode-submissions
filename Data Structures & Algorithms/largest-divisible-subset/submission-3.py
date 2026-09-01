class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)

        dp = [1] * N
        prev = [-1] * N
        max_idx = 0
        for i in range(1, N):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] != 0:
                    continue
                if 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i
        
        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        return res
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        nums.sort()
        dp = [1] * N
        prev = [-1] * N
        
        maxSeen = 0
        maxIdx = 0
        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = 1 + dp[j]
                        prev[i] = j

            if dp[i] > maxSeen:
                maxSeen = dp[i]
                maxIdx = i

        res = []
        curr = maxIdx
        while curr != -1:
            res.append(nums[curr])
            curr = prev[curr]

        return res
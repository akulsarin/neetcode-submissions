class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        numZeros = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1
                while numZeros > k:
                    numZeros -= (1 - nums[l]) 
                    l += 1
            res = max(res, r - l + 1)
        return res
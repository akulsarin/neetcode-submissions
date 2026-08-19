class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums.sort()
        mod = 10**9 + 7

        res = 0
        l, r = 0, N - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                res = (res + (2 ** (r - l))) % mod
                l += 1
            else:
                r -= 1
        
        return res
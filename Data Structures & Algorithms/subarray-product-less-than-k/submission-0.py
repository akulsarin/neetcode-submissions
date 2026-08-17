class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        N = len(nums)

        currProd = 1
        res = 0
        l = 0
        for r in range(N):
            currProd *= nums[r]

            while currProd >= k:
                currProd /= nums[l]
                l += 1

            res += r - l + 1
        return res
        
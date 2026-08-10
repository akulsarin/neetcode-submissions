class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l, r = 0, N - 1

        while l <= r:
            mid = (l + r) // 2
            numMissing = nums[mid] - nums[0] - mid
            if k <= numMissing:
                r = mid - 1
            else:
                l = mid + 1

        return nums[0] + k + l - 1    
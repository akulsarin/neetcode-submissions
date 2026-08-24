class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        maxWithPrev, maxNoPrev = 0, 0
        for num in nums[:-1]:
            maxNoPrev, maxWithPrev = max(maxWithPrev, maxNoPrev), num + maxNoPrev
        maxExcludingLast = max(maxWithPrev, maxNoPrev)

        maxWithPrev, maxNoPrev = 0, 0
        for num in nums[1:]:
            maxNoPrev, maxWithPrev = max(maxWithPrev, maxNoPrev), num + maxNoPrev
        maxExcludingFirst = max(maxWithPrev, maxNoPrev)

        return max(maxExcludingFirst, maxExcludingLast)
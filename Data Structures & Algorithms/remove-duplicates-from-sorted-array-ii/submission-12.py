class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(1, len(nums)):
            num = nums[i]
            if num != nums[l] or l == 0 or nums[l] != nums[l - 1]:
                l += 1
                nums[l] = num
        return l + 1
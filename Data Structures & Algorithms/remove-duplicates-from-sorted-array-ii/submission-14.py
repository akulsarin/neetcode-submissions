class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        l = 2
        for num in nums[2:]:
            if num != nums[l - 2]:
                nums[l] = num
                l += 1
        
        return l
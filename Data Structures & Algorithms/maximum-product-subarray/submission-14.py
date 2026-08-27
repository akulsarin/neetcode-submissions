class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = glob_max = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            max_prod, min_prod = curr_max * num, curr_min * num
            curr_max = max(num, max_prod, min_prod)
            curr_min = min(num, max_prod, min_prod)
            glob_max = max(glob_max, curr_max)
        return glob_max
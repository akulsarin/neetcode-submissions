class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        target_sum = (n * (n + 1)) // 2 
        return target_sum - sum_nums
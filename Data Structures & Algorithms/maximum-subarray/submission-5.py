class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curr_sum = max(num, num + curr_sum)
            max_sum = max(max_sum, curr_sum)
        return max_sum
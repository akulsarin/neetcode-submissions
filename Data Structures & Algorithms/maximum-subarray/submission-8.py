class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = float('-inf')

        left = 0
        max_left = max_right = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            if nums[right] > curr_sum:
                left = right
                curr_sum = nums[right]
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_left, max_right = left, right
        
        return sum(nums[max_left : max_right + 1])
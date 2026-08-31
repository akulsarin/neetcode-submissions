class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sum = 0
        left = 0
        min_size = float('inf')

        for right, num in enumerate(nums):
            window_sum += num

            while window_sum >= target:
                min_size = min(min_size, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return 0 if min_size == float('inf') else min_size
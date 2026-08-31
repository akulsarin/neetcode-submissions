class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)

        def max_subarray_sum(start_idx: int) -> int:
            curr_sum = 0
            max_sum = float('-inf')

            for i in range(start_idx, start_idx + N):
                idx = i % N
                num = nums[idx]
                curr_sum = max(curr_sum + num, num)
                max_sum = max(max_sum, curr_sum)
            
            return max_sum

        maximum = float('-inf')
        for i in range(N):
            maximum = max(maximum, max_subarray_sum(i))
        return maximum
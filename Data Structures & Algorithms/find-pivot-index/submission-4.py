class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix_total = 0
        
        for i, num in enumerate(nums):
            sum_left = prefix_total
            prefix_total += num
            sum_right = total - prefix_total

            if sum_left == sum_right:
                return i

        return -1
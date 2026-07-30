class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        curr_tracker = 0
        for num in nums:
            if num == 0:
                max_so_far = max(max_so_far, curr_tracker)
                curr_tracker = 0
                continue
            curr_tracker += 1
        return max(max_so_far, curr_tracker)
        
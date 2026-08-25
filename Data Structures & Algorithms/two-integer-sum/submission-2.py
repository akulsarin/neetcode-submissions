class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_to_index = {}
        for i, num in enumerate(nums):
            if num in diff_to_index:
                return [diff_to_index[num], i]
            diff_to_index[target - num] = i
        return []
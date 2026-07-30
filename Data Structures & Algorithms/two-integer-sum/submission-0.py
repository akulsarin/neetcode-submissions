class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {num: i for i, num in enumerate(nums)}
        
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in targets and targets[diff] != i:
                return [i, targets[diff]]

        return []
        
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        pivotIndex = -1
            
        prefix = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        postfix = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] + nums[i + 1]
            if postfix[i] == prefix[i]:
                pivotIndex = i

        if pivotIndex == -1 and postfix[-1] == prefix[-1]:
            return len(nums) - 1

        return pivotIndex

        
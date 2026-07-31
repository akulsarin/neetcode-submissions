class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1

        slowIdx, fastIdx = 0, 0
        while True:
            slowIdx = nums[slowIdx]
            fastIdx = nums[nums[fastIdx]]

            if fastIdx == slowIdx:
                break
        
        slowIdx2 = 0
        while True:
            slowIdx = nums[slowIdx]
            slowIdx2 = nums[slowIdx2]
            if slowIdx == slowIdx2:
                return slowIdx
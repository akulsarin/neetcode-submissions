class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        els = set(nums)
        visited = set()
        currMax = 0
        for i in range(len(nums)):
            currNum = nums[i] 
            if currNum in visited:
                continue
            maxFromNum = 0
            while currNum in els:
                currNum += 1
                maxFromNum += 1
            currMax = max(maxFromNum, currMax)
        return currMax


        
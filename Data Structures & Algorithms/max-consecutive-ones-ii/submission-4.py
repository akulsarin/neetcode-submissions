class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        N = len(nums)
        maxOnes = 0
        flipIdx = -1

        l = 0
        for r in range(N):
            currNum = nums[r]
            if currNum == 1:
                maxOnes = max(maxOnes, r - l + 1)
                continue
            
            if flipIdx < 0:
                maxOnes = max(maxOnes, r - l + 1)
                flipIdx = r
            else:
                maxOnes = max(maxOnes, r - l)
                l = flipIdx + 1
                flipIdx = r

        return maxOnes
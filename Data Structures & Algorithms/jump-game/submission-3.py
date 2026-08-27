class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = r = 0
        while r < len(nums) - 1:
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            if farthest == r:
                return False
            l, r = r + 1, farthest
        return True
        
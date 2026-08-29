class Solution:
    def rob(self, nums: List[int]) -> int:
        rob, no_rob = 0, 0
        for money in nums:
            rob, no_rob = no_rob + money, max(rob, no_rob)
        return max(rob, no_rob)
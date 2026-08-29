class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_prev = 0
        rob_curr = nums[0]
        for i in range(1, len(nums)):
            money = nums[i]
            rob_prev, rob_curr = rob_curr, max(rob_curr, rob_prev + money)
        return max(rob_prev, rob_curr)
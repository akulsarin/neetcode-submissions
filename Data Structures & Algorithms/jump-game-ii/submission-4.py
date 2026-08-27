class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)

        l = r = 0
        num_jumps = 0
        while r < N - 1:
            num_jumps += 1
            min_jump = max_jump = r + 1
            for i in range(l, r + 1):
                max_jump = max(max_jump, i + nums[i])
            l, r = min_jump, max_jump
        
        return num_jumps
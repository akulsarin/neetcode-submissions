class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        
        dpNext = 1
        total = 1
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dpNext += 1
            else:
                dpNext = 1
            total += dpNext

        return total        
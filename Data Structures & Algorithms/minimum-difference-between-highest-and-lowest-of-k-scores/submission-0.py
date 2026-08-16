class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = nums[-1]
        for i in range(len(nums) - k + 1):
            print(nums[i], nums[i + k - 1])
            minDiff = min(minDiff, nums[i + k - 1] - nums[i])
        
        return minDiff
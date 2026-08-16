class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        l = 0
        minLen = len(nums) + 1
        for r in range(len(prefix)):
            while prefix[r] - prefix[l] >= target:
                minLen = min(minLen, r - l)
                l += 1

        return minLen if minLen <= len(nums) else 0
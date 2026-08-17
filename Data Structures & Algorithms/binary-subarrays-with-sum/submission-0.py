class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = 0
        needed = {goal: 1}
        count = 0
        for num in nums:
            prefixSum += num
            count += needed.get(prefixSum, 0)
            needed[prefixSum + goal] = needed.get(prefixSum + goal, 0) + 1
        return count

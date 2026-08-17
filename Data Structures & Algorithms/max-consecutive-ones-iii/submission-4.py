class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flippedIndices = deque([])
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flippedIndices.append(r)
                if len(flippedIndices) > k:
                    l = flippedIndices.popleft() + 1
            res = max(res, r - l + 1)
        return res
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        currMax = 0
        flipped = deque([])

        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                continue

            flipped.append(r)
            if len(flipped) > k:
                currMax = max(currMax, r - l)
                l = flipped.popleft() + 1
        
        return max(currMax, r - l + 1)
        
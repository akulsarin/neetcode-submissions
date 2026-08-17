class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        descStack = deque([])
        ascStack = deque([])
        res = 1
        l = 0
        for r in range(len(nums)):
            while descStack and nums[r] >= descStack[-1][1]:
                descStack.pop()
            descStack.append((r, nums[r]))
            while ascStack and nums[r] <= ascStack[-1][1]:
                ascStack.pop()
            ascStack.append((r, nums[r]))
            
            while descStack[0][1] - ascStack[0][1] > limit:
                l += 1
                if descStack and descStack[0][0] < l:
                    descStack.popleft()
                if ascStack and ascStack[0][0] < l:
                    ascStack.popleft()

            res = max(res, r - l + 1)

        return res
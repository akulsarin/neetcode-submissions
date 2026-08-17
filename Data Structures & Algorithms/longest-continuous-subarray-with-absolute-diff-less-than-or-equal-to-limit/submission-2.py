class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQ = deque([])
        minQ = deque([])
        res = 1
        l = 0
        for r in range(len(nums)):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[r])
            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            minQ.append(nums[r])
            
            while maxQ[0] - minQ[0] > limit:
                if maxQ[0] == nums[l]:
                    maxQ.popleft()
                if minQ[0] == nums[l]:
                    minQ.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        dq = deque([])
        for i in range(k):
            num = nums[i]
            while dq and num > dq[-1][1]:
                dq.pop()
            dq.append((i, num))

        res = [dq[0][1]]
        for i in range(k, N):
            l = i - k
            while dq and dq[0][0] <= l:
                dq.popleft()
            
            num = nums[i]
            while dq and num > dq[-1][1]:
                dq.pop()
            dq.append((i, num)) 
            res.append(dq[0][1])

        return res
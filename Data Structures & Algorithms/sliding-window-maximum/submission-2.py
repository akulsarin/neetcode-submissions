class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_dcr = deque([])

        for i in range(k):
            num = nums[i]
            while window_dcr and num >= nums[window_dcr[-1]]:
                window_dcr.pop()
            window_dcr.append(i)

        maximums = [nums[window_dcr[0]]]
        for r in range(k, n):
            num = nums[r]
            
            l = r - k
            if window_dcr[0] <= l:
                window_dcr.popleft()

            while window_dcr and num >= nums[window_dcr[-1]]:
                window_dcr.pop()
            window_dcr.append(r)

            maximums.append(nums[window_dcr[0]])
        
        return maximums
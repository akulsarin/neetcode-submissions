class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = deque([])
        maximums = []

        for i in range(n):
            if window and window[0] <= i - k:
                window.popleft()
            
            num = nums[i]
            while window and num >= nums[window[-1]]:
                window.pop()
            window.append(i)

            if i >= k - 1:
                maximums.append(nums[window[0]])
            
        return maximums
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        maxHeap = []
        result = []

        for r in range(k):
            num = nums[r]
            heapq.heappush(maxHeap, (-num, r))

        l = 0
        for r in range(k - 1, N):
            windowMaxEl, windowMaxIdx = heapq.heappop(maxHeap)
            while windowMaxIdx < l:
                windowMaxEl, windowMaxIdx = heapq.heappop(maxHeap)

            if windowMaxIdx > l:
                heapq.heappush(maxHeap, (windowMaxEl, windowMaxIdx))

            windowMaxEl = -windowMaxEl
            result.append(windowMaxEl)
            l += 1

            if r < N - 1:
                heapq.heappush(maxHeap, (-nums[r + 1], r + 1))

        return result

        
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        
        count = 0
        window_sum = 0
        l = 0
        
        for r, num in enumerate(arr):
            window_sum += num
            if r - l + 1 > k:
                window_sum -= arr[l]
                l += 1
            if r >= k - 1 and window_sum >= threshold:
                count += 1
        return count
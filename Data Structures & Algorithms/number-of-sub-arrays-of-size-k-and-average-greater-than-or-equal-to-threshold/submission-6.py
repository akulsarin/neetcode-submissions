class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        
        count = 0
        window_sum = 0
        
        for r, num in enumerate(arr):
            window_sum += num
            if r >= k:
                window_sum -= arr[r - k]
            if r >= k - 1 and window_sum >= threshold:
                count += 1
        
        return count
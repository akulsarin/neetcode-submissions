class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sumThresh = threshold * k
        
        prefix = [0]
        for num in arr:
            prefix.append(num + prefix[-1])
        
        count = 0
        for i in range(k, len(prefix)):
            if prefix[i] - prefix[i - k] >= sumThresh:
                count += 1

        return count
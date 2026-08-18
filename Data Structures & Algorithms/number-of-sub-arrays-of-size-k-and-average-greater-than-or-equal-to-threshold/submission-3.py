class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sumThresh = threshold * k
        currSum = 0
        for num in arr[:k]:
            currSum += num

        res = 1 if currSum >= sumThresh else 0
        for i in range(k, len(arr)):
            currSum += arr[i] - arr[i - k]
            if currSum >= sumThresh:
                res += 1

        return res
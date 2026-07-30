class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n < k:
            return 0

        l = 0
        runningSum = 0
        count = 0
        for r in range(0, n):
            windowLen = r - l + 1
            runningSum += arr[r]
            if windowLen == k:
                avg = runningSum / k
                if avg >= threshold:
                    count += 1
                runningSum -= arr[l]
                l += 1

        return count


        
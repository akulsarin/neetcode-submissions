class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        N = len(nums)
        nums.sort(reverse=True)
        maxFreq = 0
        l = r = 0
        tempK = k
        while r < N:
            tempK -= (nums[l] - nums[r])

            if tempK < 0:
                if l == N - 1:
                    break
                diff = nums[l] - nums[l + 1]
                tempK += diff * (r - l)
                l += 1
            else:
                maxFreq = max(maxFreq, r - l + 1)
            
            r += 1

        return maxFreq
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        N = len(nums)

        def numSubarraysLeqSum(target: int) -> int:
            if target < 0:
                return 0

            currSum = 0
            res = 0
            l = 0
            for r in range(N):
                currSum += nums[r]
                while currSum > target:
                    currSum -= nums[l]
                    l += 1
                res += r - l + 1

            return res

        return numSubarraysLeqSum(goal) - numSubarraysLeqSum(goal - 1)
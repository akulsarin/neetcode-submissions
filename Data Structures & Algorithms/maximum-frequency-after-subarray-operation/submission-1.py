class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        dp = [0] * 51
        netGain = 0
        for num in nums:
            dp[num] = max(dp[num], dp[k]) + 1
            netGain = max(netGain, dp[num] - dp[k])

        return dp[k] + netGain


        
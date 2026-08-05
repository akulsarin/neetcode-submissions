class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        # dp[0] is ways to decode with last item being standalone
        # dp[1] is ways to decode with last item being merged with previous
        dp = [0, 0] 
        if s[0] != "0":
            dp[0] = 1
        for i in range(1, N):
            if s[i] == "0":
                # Must be merged
                mergedNum = int(s[i - 1] + s[i])
                numWithMerge = dp[0] if 1 <= mergedNum <= 26 else 0
                dp[0], dp[1] = 0, numWithMerge
            elif s[i - 1] == "0":
                # Must be standalone
                dp[0], dp[1] = dp[0] + dp[1], 0
            else:
                # Can be either
                # If merge, we must merge with standalone
                mergedNum = int(s[i - 1] + s[i])
                numWithMerge = dp[0] if 1 <= mergedNum <= 26 else 0
                # If we don't merge, all previous combinations are acceptable
                numWithStandalone = dp[0] + dp[1]
                dp[0], dp[1] = numWithStandalone, numWithMerge

        return sum(dp)

                

            


"""
Example 1:
num=1012
i == 0: [1, 0]
i == 1: [0, 1]
i == 2: [1, 0]
i == 3: [1, 1]

Example 2:
num=12
i == 0: [1, 0]
i == 1: [1, 1]

Example 3:
num=301
i == 0: [1, 0]
i == 1: [1, 1]
"""
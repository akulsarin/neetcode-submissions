class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        [[2,3],[4,4],[5,8],[6,4],[6,7],[6, 10]]
        dp_0 = [0, 0, 0, 0]
        
        """
        N = len(envelopes)
        envelopes.sort()
        dp = [1 for _ in range(N)]
        maxSeen = 1
        for i in range(N - 2, -1, -1):
            wi, hi = envelopes[i]
            for j in range(i + 1, N):
                wj, hj = envelopes[j]
                # print(f"{envelopes[i]} | {envelopes[j]}")
                if wi == wj or hi >= hj:
                    continue
                dp[i] = max(dp[i], 1 + dp[j])
                maxSeen = max(maxSeen, dp[i])
        return maxSeen
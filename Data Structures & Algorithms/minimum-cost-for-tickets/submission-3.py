import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        
        dp = [0] * (N + 1)

        idx7 = N
        idx30 = N

        for i in range(N - 1, -1, -1):
            while idx7 - 1 > i and days[idx7 - 1] >= days[i] + 7:
                idx7 -= 1
            while idx30 - 1 > i and days[idx30 - 1] >= days[i] + 30:
                idx30 -= 1

            dp[i] = min(
                costs[0] + dp[i + 1],
                costs[1] + dp[idx7],
                costs[2] + dp[idx30]
            )

        return dp[0]
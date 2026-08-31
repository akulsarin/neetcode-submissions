import bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        
        dp = [float('inf')] * N
        dp[N - 1] = min(costs)

        for i in range(N - 2, -1, -1):
            for j, day_count in enumerate([0, 6, 29]):
                next_idx = bisect.bisect(days, days[i] + day_count)
                next_cost = dp[next_idx] if next_idx < N else 0
                dp[i] = min(dp[i], costs[j] + next_cost)

        return dp[0]
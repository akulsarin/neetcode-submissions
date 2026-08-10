import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        N = len(jobs)

        jobs.sort()
        dp = [0] * N # dp[i] := maximum achievable profit when considering jobs[i:]
        dp[-1] = jobs[-1][-1]

        for i in range(N - 2, -1, -1):
            currStart, currEnd, currProfit = jobs[i]

            # Take current job => add profit to max of next non-overlapping job
            nextIdx = bisect.bisect_left(jobs, currEnd, key=lambda j: j[0])
            nextProfit = 0 if nextIdx >= N else dp[nextIdx]
            profitWithCurr = currProfit + nextProfit

            # Don't take current job => take the next job's max profit
            profitWithoutCurr = dp[i + 1]

            dp[i] = max(profitWithoutCurr, profitWithCurr)

        return dp[0]        
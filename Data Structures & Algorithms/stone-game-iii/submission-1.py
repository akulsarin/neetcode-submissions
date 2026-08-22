class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        N = len(stoneValue)
        
        dp = [float('-inf')] * N
        dp[-1] = stoneValue[-1]

        for i in range(N - 2, -1, -1):
            score = 0
            maxRange = min(N, i + 3)
            for j in range(i, maxRange):
                score += stoneValue[j]
                oppScore = 0 if j + 1 >= N  else dp[j + 1]
                dp[i] = max(dp[i], score - oppScore)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
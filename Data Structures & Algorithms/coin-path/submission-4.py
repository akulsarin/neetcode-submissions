class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        N = len(coins)
        
        dp = [float('inf')] * N
        dp[-1] = 0 if coins[-1] != -1 else dp[-1]
        nextIdx = [-1] * N

        for i in range(N - 2, -1, -1):
            if coins[i] == -1:
                continue

            maxRange = min(N, i + maxJump + 1)
            for k in range(i + 1, maxRange):
                cost = coins[i] + dp[k]
                if cost < dp[i]:
                    dp[i] = cost
                    nextIdx[i] = k
        
        res = []
        if dp[0] == float('inf'):
            return res
        
        curr = 0
        while curr != -1:
            res.append(curr + 1)
            curr = nextIdx[curr]
    
        return res
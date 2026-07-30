class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countOccurrence(binStr: str) -> List[int]:
            res = [0, 0]
            for c in binStr:
                res[int(c)] += 1
            return res
        
        counts = {binStr: countOccurrence(binStr) for binStr in strs}

        # dp.shape = (len(strs), m + 1, n + 1)
        # dp[i][j][k] := size of largest subset up to i-th index s.t. there
        #                are at most j 0's and k 1's
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in strs]
        
        for j in range(m + 1):
            for k in range(n + 1):
                numZeros, numOnes = counts[strs[0]]
                if numZeros <= j and numOnes <= k:
                    dp[0][j][k] = 1

        for i in range(1, len(strs)):
            for j in range(m + 1):
                for k in range(n + 1):
                    # Exclude
                    exclude = dp[i - 1][j][k]

                    # Include
                    include = 0
                    numZeros, numOnes = counts[strs[i]]
                    remZeros, remOnes = j - numZeros, k - numOnes
                    if remZeros >= 0 and remOnes >= 0:
                        include = dp[i - 1][remZeros][remOnes] + 1
                    
                    # Pick the max
                    dp[i][j][k] = max(exclude, include)

        return dp[-1][-1][-1]

        
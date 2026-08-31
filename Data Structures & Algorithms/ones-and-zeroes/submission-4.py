class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(L + 1)]

        for i in range(L - 1, -1, -1):
            counts = Counter(strs[i])
            for m_left in range(m + 1):
                for n_left in range(n + 1):
                    if m_left == n_left == 0:
                        continue
                    
                    dp[i][m_left][n_left] = dp[i + 1][m_left][n_left]
                    if counts["0"] <= m_left and counts["1"] <= n_left:
                        dp[i][m_left][n_left] = max(
                            dp[i][m_left][n_left],
                            1 + dp[i + 1][m_left - counts["0"]][n_left-counts["1"]]
                        )
        
        return dp[0][m][n]
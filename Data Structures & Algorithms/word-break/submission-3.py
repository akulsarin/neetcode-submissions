class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        
        dp = [False] * (m + 1)
        dp[m] = True

        for i in range(m - 1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if s[i : i + word_len] == word:
                    dp[i] |= dp[i + word_len]
                if dp[i]:
                    break
        
        return dp[0]
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        N = len(sentence)
        dp = [0] * N

        for i in range(N):
            remainingCols = cols
            j = i
            while remainingCols > 0:
                word = sentence[j % N]
                wordLen = len(word)
                if wordLen > remainingCols:
                    break
                remainingCols -= (wordLen + 1)
                dp[i] += 1
                j += 1
        
        wordsPlaced = 0
        start = 0
        for i in range(rows):
            wordsPlaced += dp[start]
            start = (start + dp[start]) % N

        return wordsPlaced // N

        
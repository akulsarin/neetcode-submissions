class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqMap = defaultdict(int)
        maxFreq = 0
        result = 0
        l = 0
        for r in range(len(s)):
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])
            
            windowLen = r - l + 1
            replacements = windowLen - maxFreq
            if replacements <= k:
                result = max(result, windowLen)
            elif replacements > k:
                freqMap[s[l]] -= 1
                l += 1

        return result